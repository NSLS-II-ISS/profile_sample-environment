from textwrap import dedent

from caproto.server import PVGroup, ioc_arg_parser, pvproperty, run
import time as ttime
import numpy as np

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

    dwell = pvproperty(value=0.05,
                    doc="dwell time for the pv setpoint update")

    time_start = None
    time_paused = 0


    @pv_sp.startup
    async def pv_sp(self, instance, async_lib):
        """This is a startup hook which periodically updates the value."""
        while True:
            if self.go.value == 1:
                # step_start_time = ttime.time()

                # if self.pause.value == 0:
                if self.time_start is None:
                    self.time_start = ttime.time()

                self.pause_program() # pauses the program if needed
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