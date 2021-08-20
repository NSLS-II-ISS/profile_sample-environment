
# temp1 = EpicsSignal('XF:08IDB-CT{ES-TC}T1-I', name='temp1')
# temp2 = EpicsSignal('XF:08IDB-CT{ES-TC}T2-I', name='temp2')



from simple_pid import PID
import h5py
import bluesky.plan_stubs as bps
import numpy as np
import time as ttime
from ophyd import Component as Cpt, Device, EpicsSignal, Kind


temp1 = EpicsSignal('XF:08IDB-CT{DIODE-Box_B2:5}InCh0:Data-I', name='temp1')
temp2 = EpicsSignal('XF:08IDB-CT{DIODE-Box_B2:5}InCh1:Data-I', name='temp2')


temp1_sp = EpicsSignal('XF:08IDB-CT{DIODE-HTR:1}T-SP', name='temp1_sp')
temp2_sp = EpicsSignal('XF:08IDB-CT{DIODE-HTR:2}T-SP', name='temp2_sp')
temps = [temp1, temp1_sp, temp2, temp2_sp]



for pv in temps:
    arch_iss.pvs.update({pv.name: pv.pvname})

heater1_curr_output = EpicsSignal('XF:08IDB-CT{DIODE-HTR:1}CURR:1-SP', name='curr_override')
heater2_volt_output = EpicsSignal('XF:08IDB-CT{DIODE-HTR:2}VOLT:1-SP', name='volt_override')

class Ramper(Device):
    pv_sp = Cpt(EpicsSignal, 'pv_sp', name='pv_sp')
    go = Cpt(EpicsSignal, 'go', name='go')
    pv_pause = EpicsSignal('XF:08IDB-Ramping:pause', name='pv_pause')

    tprog = Cpt(EpicsSignal, 'tprog', name='tprog')
    pvprog = Cpt(EpicsSignal, 'pvprog', name='pvprog')
    dwell = Cpt(EpicsSignal, 'dwell', name='dwell')
    safety_thresh = Cpt(EpicsSignal, 'safety_thresh', name='safety_thresh')
    safety_timer = Cpt(EpicsSignal, 'safety_timer', name='safety_timer')
    pid_enable_name = Cpt(EpicsSignal, 'pid_enable_name', name='pid_enable_name')
    pid_output_name = Cpt(EpicsSignal, 'pid_output_name', name='pid_output_name')
    # pid_output_name_ext = Cpt(EpicsSignal, 'pid_output_name_ext', name='pid_output_name_ext')

    def __init__(self, aux_pv_sp=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aux_pv_sp = aux_pv_sp
        self._subscribe_aux_pv_sp()
        self.subscribe_safety_timer_upd()

    def _subscribe_aux_pv_sp(self):
        if self.aux_pv_sp is not None:

            def subscription(value, **kwargs):
                setpoint = value
                self.aux_pv_sp.put(setpoint)
                return

            self.pv_sp.subscribe(subscription)

    def subscribe_safety_timer_upd(self):
        def subscription(value, **kwargs):
            if value>5:
                self.safety_timer.put(0)

        self.safety_timer.subscribe(subscription)


    def enable(self):
        self.pv_pause.put(0)
        self.go.put(1)

    def pause(self):
        self.pv_pause.put(1)

    def depause(self):
        self.pv_pause.put(0)

    def disable(self, pv_sp_value=25):
        self.go.put(0)
        self.pv_pause.put(0)
        ttime.sleep(0.3)
        if pv_sp_value is not None:
            self.pv_sp.put(pv_sp_value)


try:
    ramper = Ramper(aux_pv_sp=temp2_sp ,prefix='XF:08IDB-Ramping:', name='ramper')
    ramper.go.get() # to see if it is accessible
except:
    print('ramper PV is not initialized')
    ramper = None




class SamplePID(Device):
    pv = Cpt(EpicsSignal, '.CVAL', name='pv')
    pv_sp = Cpt(EpicsSignal, '.VAL', name='pv_sp')
    enabled = Cpt(EpicsSignal, ':on')
    KP = Cpt(EpicsSignal, '.KP')
    KI = Cpt(EpicsSignal, '.KI')
    KD = Cpt(EpicsSignal, '.KD')

    def __init__(self, human_name, pv_name, pv_units,
                 kp=0.05, ki=0.02, kd=0.00,
                 pv_output=None,
                 pv_output_name='',
                 pv_output_units='',
                 ramper=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.human_name = human_name
        self.pv_name = pv_name
        self.pv_units = pv_units
        self.pv_output = pv_output
        self.pv_output_name = pv_output_name
        self.pv_output_units = pv_output_units
        self.ramper = ramper
        self._subscribe_to_ramper()
        self._check_pid_values(kp, ki, kd)

    def _subscribe_to_ramper(self):
        if self.ramper is not None:

            def subscription(value, **kwargs):
                setpoint = value
                self.pv_sp.put(setpoint)
                return

            self.ramper.pv_sp.subscribe(subscription)
            self.ramper.pid_enable_name.put(self.enabled.pvname)
            self.ramper.pid_output_name.put(self.pv_output.pvname)

    def enable(self):
        self.enabled.put(1)

    def disable(self):
        self.enabled.put(0)

    def _check_pid_values(self, kp, ki, kd):
        if ((not np.isclose(self.KP.get(), kp, 1e-3)) or
            (not np.isclose(self.KI.get(), ki, 1e-3)) or
            (not np.isclose(self.KD.get(), kd, 1e-3))):
            print(f'Warning: Sample PID loop for {self.human_name} was initialized with non-standard values !!!!')

    def current_pv_reading(self, offset=5):
        return (self.pv.get() - offset)

    def ramp_start(self, times_list, pv_sp_list):
        self.ramper.disable(pv_sp_value=None)
        self.ramper.tprog.put(times_list)
        self.ramper.pvprog.put(pv_sp_list)
        self.enable()
        self.ramper.enable()

    def ramp_pause(self):
        self.ramper.pause()

    def ramp_continue(self):
        self.ramper.depause()

    def ramp_stop(self):
        self.disable()
        self.ramper.disable()




heater_spiral = SamplePID(human_name='Spiral Heater', pv_name='Temperature', pv_units='C deg',
                          kp=0.05, ki=0.02, kd=0.00,
                          pv_output=heater2_volt_output,
                          pv_output_name='Voltage',
                          pv_output_units='V',
                          ramper=ramper,
                          prefix='XF:08IDB-CT{FbPid:01}PID', name='heater_spiral')

sample_envs_dict = {'Spiral Heater' : heater_spiral}



#     def __init__(self, temprb_pv, output_pv, output_max=3.5):
#         self.temprb_pv = temprb_pv
#         self.output_pv = output_pv
#         self.output_max = output_max
#
#     def set_pid(self, p, i, d):
#         t_init = self.temprb_pv.get()
#         self.pid = PID(p, i, d, setpoint=t_init)
#         self.pid.sample_time = 0.1
#         self.pid.output_limits = (0, self.output_max)
#
#     def update_setpoint(self, setpoint):
#         self.pid.setpoint = setpoint
#
#
# heater_cartridge = Heater(temp1, heater1_curr)
# heater_spiral = Heater(temp2, heater2_volt)
# heater_furnace = Heater(temp2, heater2_volt)


# heater_spiral.set_pid(p=0.01, i=0.00031622776601683794, d=0)
# heater_furnace.set_pid(p=0.01, i=0.00031622776601683794, d=0)


# def end_temperature_control_plan(heater : Heater):
#     yield from bps.mv(heater.output_pv, 0)


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
        if t_print >0.1:
            print(temp_setpoint)
            t_print = ttime.time()


# def test_plan():
#     yield from bps.open_run()
#     yield from bps.monitor(temp1, name='temp1')
#     yield from bps.sleep(2)
#     yield from bps.unmonitor(temp1)
#     yield from bps.close_run()







# def test_pid_values_plan(p_range, i_range, npt, heater):
#     hf = h5py.File(r'/nsls2/xf08id/Sandbox/pid_temp_data/2020_12_29_data_high_temp.h5', 'w')
#     p_grid = 10**np.linspace(np.log10(p_range[0]), np.log10(p_range[1]), npt)
#     i_grid = 10**np.linspace(np.log10(i_range[0]), np.log10(i_range[1]), npt)
#     n = p_grid.size * i_grid.size
#     idx = 1
#     for _p in p_grid:
#         for _i in i_grid:
#             print(f'checking p={_p}, i={_i} | progress = {round(idx / n * 100)}')
#
#
#
#     p_grid = 10 ** np.linspace(-2.7, -1.9, 5)
#     i_grid = 10 ** np.linspace(-3.25, -3.75, 5)
#     n = p_grid.size * i_grid.size
#     idx = 1
#     for _p in p_grid:
#         for _i in i_grid:
#             print(f'checking p={_p}, i={_i} | progress = {round(idx / n * 100)}')
#             _t, _T, _V = pid_testing(max_time=exec_time, p=_p, i=_i, d=0, setpoint=setpoint, plotting=False)
#             R = np.sum(((_T[_t > 0.33 * exec_time] - setpoint) / setpoint) ** 2)
#
#             g = hf.create_group(str(idx))
#             g.create_dataset('t', data=_t)
#             g.create_dataset('T', data=_T)
#             g.create_dataset('V', data=_V)
#             g.create_dataset('P', data=_p)
#             g.create_dataset('I', data=_i)
#             g.create_dataset('R', data=R)
#             idx += 1
#             ttime.sleep(sleep_time)
#
#     hf.close()

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
