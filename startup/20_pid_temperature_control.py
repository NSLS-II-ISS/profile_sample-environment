
from simple_pid import PID
import h5py








class Heater:

    def __init__(self, enable_pv, override_pv, temprb_pv, output_pv):
        self.enable_pv = enable_pv
        self.override_pv = override_pv
        self.temprb_pv = temprb_pv
        self.output_pv = output_pv


    def begin_temperature_control_plan(self):
        yield from bps.mv(override_pv, 1)
        yield from bps.mv(enable_pv, 1)
        # yield from bps.mv(heater_override2, 1)

    # def



# def initalize_pid(p=0.01, i=0.01, d=0.001, kind='egg_boiler'):
#     if kind == 'egg_boiler':
#         p, i, d = 0.01, 0.00031622776601683794, 0
#         T_init = temp2.value # second controller!
#         pid = PID(p, i, d, setpoint=T_init)
#     else:
#         raise KeyError('unknown heater kind')
#
#     return pid
#
#
#
# def begin_temperature_control_plan():
#     yield from bps.mv(volt_override, 1)
#     yield from bps.mv(heater_enable2, 1)
#     yield from bps.mv(heater_override2, 1)
#
#
# def end_temperature_control_plan():
#     yield from bps.mv(volt_override, 0)
#     yield from bps.mv(heater_enable2, 0)
#     yield from bps.mv(heater_override2, 0)





def ramp_temperature_plan(t_ramp=3*60, T=400, p=0.01, i=0.01, d=0.001):
    time, temp_rb, volt_out = [], [], []

    pid = PID(p, i, d, setpoint=T_init)
    pid.sample_time = 0.01
    pid.output_limits = (0, 3.5)


    time_start = ttime.time()
    ramp_rate = (T - T_init) / t_ramp
    while True:
        dt = ttime.time() - time_start
        if dt < t_ramp:
            pid.setpoint = ramp_rate * dt + T_init
        else:
            pid.setpoint = T
        print(pid.setpoint)
        current_value = temp2.value
        output = pid(current_value)
        time.append(dt)
        temp_rb.append(current_value)
        volt_out.append(output)
        RE(bps.mv(volt_override, output))

        if dt > max_time:
            break
        # ttime.sleep(0.1)

    RE(bps.mv(volt_override, 0))
    RE(bps.mv(heater_enable2, 0))
    RE(bps.mv(heater_override2, 0))