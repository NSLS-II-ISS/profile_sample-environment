from textwrap import dedent

from caproto import ChannelType
from caproto.server import PVGroup, ioc_arg_parser, pvproperty, run
import time as ttime
from math import isfinite

from sample_environment.ramping import RampClock, RampProgram
from ophyd import EpicsSignal


class RamperIOC(PVGroup):
    """
    An IOC for executing ramps of pv_setpoints

    """
    pv_sp = pvproperty(
        value=25.0,
        doc='pv setpoint',
    )

    pv_sp_rate = pvproperty(
        value=0.0,
        doc='pv setpoint change rate',
    )

    go = pvproperty(
        value=0,
        doc='flag indicating whether ramping is actually taking place'
    )

    time_elapsed = pvproperty(
        value=0.0,
        doc='timer for measuring the elapsed time since the beginning of the program'
    )

    pause = pvproperty(
        value=0,
        doc='flag indicating whether ramping is paused'
    )

    time_paused = pvproperty(
        value=0.0,
        doc='timer for measuring the paused time'
    )

    tprog = pvproperty(
        value=[0.0, 60.0],
        doc='time array of the ramp program',
        max_length=25
    )

    pvprog = pvproperty(
        value=[25.0, 25.0],
        doc='pv setpoint array of the pv (usually temperature) ramp program',
        max_length=25
    )

    step  = pvproperty(
        value=0,
        doc="step of the program executed right now"
        )


    dwell = pvproperty(
        value=0.05,
        doc="dwell time for the pv setpoint update"
        )


    safety_timer = pvproperty(
        value=0.0,
        doc='timer for stopping the program in case if ipython session dies'
    )

    safety_thresh = pvproperty(
        value=10.0,
        doc='time threshold for turning the heater off'
    )

    pid_enable_name = pvproperty(
        value='',
        dtype=ChannelType.STRING,
        doc='pv name for pid enable'
    )

    pid_output_name = pvproperty(
        value='',
        dtype=ChannelType.STRING,
        # dtype=_LongStringChannelType.LONG_STRING,
        doc='pv name for pid output'
    )

    # pid_output_name_ext = pvproperty(
    #     value='',
    #     dtype=ChannelType.STRING,
    #     # dtype=_LongStringChannelType.LONG_STRING,
    #     doc='pv name for pid output (extension)'
    # )

    pv_test = pvproperty(
        value=0,
        doc='pv for output testing'
    )
    pid_enable = None
    pid_output = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._clock = RampClock()
        self._program = RampProgram(self.tprog.value, self.pvprog.value)
        self._previous_sample = None

    @go.putter
    async def go(self, instance, value):
        if value not in (0, 1):
            raise ValueError("go must be 0 or 1")
        if value and not instance.value:
            self._program = RampProgram(self.tprog.value, self.pvprog.value)
        if not value:
            self._clock = RampClock()
            self._previous_sample = None
        return value

    @dwell.putter
    async def dwell(self, instance, value):
        if not isfinite(value) or value <= 0:
            raise ValueError("dwell must be finite and positive")
        return value

    @tprog.putter
    async def tprog(self, instance, value):
        if self.go.value:
            raise ValueError("Stop the ramp before editing its program")
        return value

    @pvprog.putter
    async def pvprog(self, instance, value):
        if self.go.value:
            raise ValueError("Stop the ramp before editing its program")
        return value

    async def _update_ramp(self, now):
        running, paused = bool(self.go.value), bool(self.pause.value)
        self._clock.update(now, running, paused)
        rate = 0.0
        if running and not paused:
            elapsed = self._clock.elapsed
            value, step = self._program.sample(elapsed)
            if self._previous_sample is not None:
                previous_time, previous_value = self._previous_sample
                interval = elapsed - previous_time
                if interval > 0:
                    rate = (value - previous_value) / interval * 60
            self._previous_sample = elapsed, value
            if self.step.value != step:
                await self.step.write(step)
            await self.pv_sp.write(value)
        elif not running:
            self._previous_sample = None
        for signal, value in (
            (self.time_elapsed, self._clock.elapsed + self._clock.paused),
            (self.time_paused, self._clock.paused),
            (self.pv_sp_rate, rate),
        ):
            if signal.value != value:
                await signal.write(value)

    @pv_sp.startup
    async def pv_sp(self, instance, async_lib):
        """Use one monotonic clock for ramp and pause accounting."""
        while True:
            await self._update_ramp(ttime.monotonic())
            await async_lib.sleep(self.dwell.value)

    @pid_enable_name.startup
    async def pid_enable_name(self, instance, async_lib):
        while self.pid_enable_name.value == '':
            await async_lib.sleep(1)

        self.pid_enable = EpicsSignal(self.pid_enable_name.value, name='pid_enable')
        def subscription(value, **kwargs):
            if value == 0:
                if self.pid_output is not None:
                    if self.pid_output.get() != 0:
                        self.pid_output.put(0)
        self.pid_enable.subscribe(subscription)


    @pid_output_name.startup
    async def pid_output_name(self, instance, async_lib):
        while (self.pid_output_name.value == ''):
            await async_lib.sleep(1)

        self.pid_output = EpicsSignal(self.pid_output_name.value, name='pid_output')
        def subscription(value, **kwargs):
            if value != 0:
                if self.pid_enable is not None:
                    if self.pid_enable.get() == 0:
                        self.pid_output.put(0)
        self.pid_output.subscribe(subscription)


    @safety_timer.startup
    async def safety_timer(self, instance, async_lib):
        while self.safety_timer.value < self.safety_thresh.value:
            safety_timer = self.safety_timer.value + 1
            await instance.write(value=safety_timer)
            await async_lib.sleep(1)
        if self.pid_enable is not None:
            self.pid_enable.put(0)


if __name__ == '__main__':
    print('Launching sample environment ramping IOC')
    ioc_options, run_options = ioc_arg_parser(
        default_prefix='XF:08IDB-Ramping:',
        desc=dedent(RamperIOC.__doc__))
    ioc = RamperIOC(**ioc_options)
    run(ioc.pvdb, **run_options)