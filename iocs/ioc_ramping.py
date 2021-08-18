from textwrap import dedent

from caproto import ChannelType
from caproto._dbr import _LongStringChannelType
from caproto.server import PVGroup, ioc_arg_parser, pvproperty, run
import time as ttime
import numpy as np
from ophyd import Component as Cpt, Device, EpicsSignal, Kind

class RamperIOC(PVGroup):
    """
    An IOC for executing ramps of pv_setpoints

    """
    pv_sp = pvproperty(
        value=25.0,
        doc='pv setpoint',
    )

    go = pvproperty(
        value=0,
        doc='flag indicating whether ramping is actually taking place'
    )

    # pause = pvproperty(
    #     value=0,
    #     doc='flag indicating whether ramping is paused'
    # )


    tprog = pvproperty(
        value=[0.0, 60.0],
        doc='time array of the ramp program',
        max_length=100
    )

    pvprog = pvproperty(
        value=[25.0, 25.0],
        doc='pv setpoint array of the ramp program',
        max_length=100
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
        value=30.0,
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

    pid_output_name_ext = pvproperty(
        value='',
        dtype=ChannelType.STRING,
        # dtype=_LongStringChannelType.LONG_STRING,
        doc='pv name for pid output (extension)'
    )

    pv_test = pvproperty(
        value=0,
        doc='pv for output testing'
    )

    time_start = None
    time_paused = 0
    pid_enable = None
    pid_output = None


    @pv_sp.startup
    async def pv_sp(self, instance, async_lib):
        """This is a startup hook which periodically updates the value."""
        while True:
            if self.go.value == 1:
                # step_start_time = ttime.time()

                # if self.pause.value == 0:
                if self.time_start is None:
                    self.time_start = ttime.time()

                # self.pause_program() # pauses the program if needed
                dt = ttime.time() - self.time_start - self.time_paused

                if dt < np.max(self.tprog.value):
                    pv_sp = np.interp(dt, self.tprog.value, self.pvprog.value)
                else:
                    pv_sp = self.pvprog.value[-1]
                await instance.write(value=pv_sp)
                # else:
                #     self.time_paused += (ttime.time - step_start_time)
            else:
                self.time_start = None
            await async_lib.sleep(self.dwell.value)


    @pid_enable_name.startup
    async def pid_enable_name(self, instance, async_lib):
        while self.pid_enable_name.value == '':
            await async_lib.sleep(1)

        self.pid_enable = EpicsSignal(self.pid_enable_name.value, name='pid_enable')
        def subscription(value, **kwargs):
            if value == 0:
                if self.pid_output is not None:
                    self.pid_output.put(0)

        self.pid_enable.subscribe(subscription)


    @pid_output_name.startup
    async def pid_output_name(self, instance, async_lib):
        while (self.pid_output_name.value == ''):
            await async_lib.sleep(1)

        await async_lib.sleep(0.2)
        pid_output_name = self.pid_output_name.value + self.pid_output_name_ext.value
        self.pid_output = EpicsSignal(pid_output_name, name='pid_output')




    @safety_timer.startup
    async def safety_timer(self, instance, async_lib):
        while self.safety_timer.value < self.safety_thresh.value:
            safety_timer = self.safety_timer.value + 1
            await instance.write(value=safety_timer)
            await async_lib.sleep(1)
        if self.pid_enable is not None:
            self.pid_enable.put(0)






    # def pause_program(self):
    #     cur_time = ttime.time()
    #     if self.pause.value == 1:
    #         while True:
    #             if self.pause.value == 0:
    #                 break
    #             ttime.sleep(0.05)
    #         self.time_paused += (ttime.time() - cur_time)







if __name__ == '__main__':
    ioc_options, run_options = ioc_arg_parser(
        default_prefix='XF:08IDB-Ramping:',
        desc=dedent(RamperIOC.__doc__))
    ioc = RamperIOC(**ioc_options)
    run(ioc.pvdb, **run_options)