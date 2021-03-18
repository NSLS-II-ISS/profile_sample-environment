

# temp1 = EpicsSignal('XF:08IDB-CT{ES-TC}T1-I', name='temp1')
# temp2 = EpicsSignal('XF:08IDB-CT{ES-TC}T2-I', name='temp2')



from simple_pid import PID
import h5py
import bluesky.plan_stubs as bps
import numpy as np
import time as ttime

temp1 = EpicsSignal('XF:08IDB-CT{DIODE-Box_B2:5}InCh0:Data-I', name='temp1')
temp2 = EpicsSignal('XF:08IDB-CT{DIODE-Box_B2:5}InCh1:Data-I', name='temp2')


heater1_curr = EpicsSignal('XF:08IDB-CT{DIODE-Box_B2:3}OutCh0:Data-SP', name='curr_override')
heater2_volt = EpicsSignal('XF:08IDB-CT{DIODE-Box_B1:11}OutCh0:Data-SP', name='volt_override')

class Heater:

    def __init__(self, temprb_pv, output_pv, output_max=3.5):
        self.temprb_pv = temprb_pv
        self.output_pv = output_pv
        self.output_max = output_max

    def set_pid(self, p, i, d):
        t_init = self.temprb_pv.get()
        self.pid = PID(p, i, d, setpoint=t_init)
        self.pid.sample_time = 0.1
        self.pid.output_limits = (0, self.output_max)

    def update_setpoint(self, setpoint):
        self.pid.setpoint = setpoint


heater_cartridge = Heater(temp1, heater1_curr)
heater_spiral = Heater(temp2, heater2_volt)
heater_furnace = Heater(temp2, heater2_volt)


heater_spiral.set_pid(p=0.01, i=0.00031622776601683794, d=0)
heater_furnace.set_pid(p=0.01, i=0.00031622776601683794, d=0)


def end_temperature_control_plan(heater : Heater):
    yield from bps.mv(heater.output_pv, 0)


def update_output_plan(heater, warmedup=True):
    current_temp = heater.temprb_pv.get()
    output_value = heater.pid(current_temp)
    if not warmedup:
        if output_value > 0.01 * heater.output_max:
            output_value = 0.01 * heater.output_max
    yield from bps.mv(heater.output_pv, output_value)



# def execute_temperature_control_plan(heater, times, temps, end_program_flag=False, record_data=False, sampling_time=0.1):
#
#     if record_data:
#         _time, _temp_rb, _output = [], [], []
#         sampling_time_start = ttime.time()
#
#     time_start = ttime.time()
#
#     while True:
#         dt = ttime.time() - time_start
#         if dt < np.max(times):
#             temp_setpoint = np.interp(dt, times, temps)
#         else:
#             temp_setpoint = temps[-1]
#
#         heater.update_setpoint(temp_setpoint)
#         yield from update_output_plan(heater)
#
#         if record_data:
#             dt_sampling = ttime.time() - sampling_time_start
#             if dt_sampling > sampling_time:
#                 _time.append(dt)
#                 _temp_rb.append(heater.temprb_pv.get())
#                 _output.append(heater.output_pv.get())
#                 sampling_time_start = ttime.time()

def execute_temperature_control_plan(heater, times, temps, end_program_flag=False, warmup_time=30):
    warmedup = False
    time_start = ttime.time()
    t_print = ttime.time()
    while True:
        ttime.sleep(0.05)
        dt = ttime.time() - time_start

        if dt < np.max(times):
            temp_setpoint = np.interp(dt, times, temps)
        else:
            temp_setpoint = temps[-1]
        if dt > warmup_time:
            warmedup = True
        heater.update_setpoint(temp_setpoint)
        yield from update_output_plan(heater, warmedup)
        if t_print>0.1:
            print(temp_setpoint)
            t_print = ttime.time()


# def test_plan():
#     yield from bps.open_run()
#     yield from bps.monitor(temp1, name='temp1')
#     yield from bps.sleep(2)
#     yield from bps.unmonitor(temp1)
#     yield from bps.close_run()







def test_pid_values_plan(p_range, i_range, npt, heater):
    hf = h5py.File(r'/nsls2/xf08id/Sandbox/pid_temp_data/2020_12_29_data_high_temp.h5', 'w')
    p_grid = 10**np.linspace(np.log10(p_range[0]), np.log10(p_range[1]), npt)
    i_grid = 10**np.linspace(np.log10(i_range[0]), np.log10(i_range[1]), npt)
    n = p_grid.size * i_grid.size
    idx = 1
    for _p in p_grid:
        for _i in i_grid:
            print(f'checking p={_p}, i={_i} | progress = {round(idx / n * 100)}')



    p_grid = 10 ** np.linspace(-2.7, -1.9, 5)
    i_grid = 10 ** np.linspace(-3.25, -3.75, 5)
    n = p_grid.size * i_grid.size
    idx = 1
    for _p in p_grid:
        for _i in i_grid:
            print(f'checking p={_p}, i={_i} | progress = {round(idx / n * 100)}')
            _t, _T, _V = pid_testing(max_time=exec_time, p=_p, i=_i, d=0, setpoint=setpoint, plotting=False)
            R = np.sum(((_T[_t > 0.33 * exec_time] - setpoint) / setpoint) ** 2)

            g = hf.create_group(str(idx))
            g.create_dataset('t', data=_t)
            g.create_dataset('T', data=_T)
            g.create_dataset('V', data=_V)
            g.create_dataset('P', data=_p)
            g.create_dataset('I', data=_i)
            g.create_dataset('R', data=R)
            idx += 1
            ttime.sleep(sleep_time)

    hf.close()

#
#
#
# temps = [temp1, temp2]
#
# for temp in temps:
#     arch_iss.pvs.update({temp.name: temp.pvname})
#
#
# # cartridge heater
# heater1_enable = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}T-HtrEna-Cmd', name='heater_enable1')
# heater1_override = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}T-HtrOverR-Cmd', name='heater_override1')
# # pid_p1 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}T-Kp', name='pid_p1')
# # pid_i1 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}T-Ki', name='pid_i1')
# # pid_d1 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}T-Kd', name='pid_d1')
# heater1_curr = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}A-AO', name='curr_override')
# # curr_rb = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}A-AI', name='curr_rb')
# # curr_override = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}A-AO', name='curr_override')
#
#
# # spiral heater
# heater2_enable = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-HtrEna-Cmd', name='heater_enable2')
# heater2_override = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-HtrOverR-Cmd', name='heater_override2')
# # pid_p2 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-Kp', name='pid_p2')
# # pid_i2 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-Ki', name='pid_i2')
# # pid_d2 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-Kd', name='pid_d2')
# # volt_rb = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}V-AI', name='volt_rb')
# heater2_volt = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}V-AO', name='volt_override')
# # volt_override = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-HtrOverR-Cmd', name='volt_override')
#
#
#
# heater1_temp_sp = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}T-SP', name='temp_sp1')
# heater2_temp_sp = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-SP', name='temp_sp2')
# arch_iss.pvs.update({heater1_temp_sp.name: heater1_temp_sp.pvname})
#
# temps_sp = [heater1_temp_sp] #, temp_sp2]
# #
# # for temp in temps_sp:
# #     arch_iss.pvs.update({temp.name: temp.pvname})