
from simple_pid import PID
import h5py
import bluesky.plan_stubs as bps
import numpy as np


#
#
#
#
# class Heater:
#
#     def __init__(self, enable_pv, override_pv, temprb_pv, output_pv):
#         self.enable_pv = enable_pv
#         self.override_pv = override_pv
#         self.temprb_pv = temprb_pv
#         self.output_pv = output_pv
#
#     def set_pid(self, p, i, d):
#         t_init = self.temprb_pv.get()
#         self.pid = PID(p, i, d, setpoint=t_init)
#
#
#     def update_setpoint(self, setpoint):
#         self.pid.setpoint = setpoint
#
#     def update_output(self):
#         current_temp = self.temprb_pv.get()
#         output_value = self.pid(current_emp)
#         bps.mv(self.output_pv, output_value)
#
#
# heater_cartridge = Heater(heater1_enable, heater1_override, temp1, heater1_curr)
# heater_spiral = Heater(heater2_enable, heater2_override, temp2, heater2_volt)
#
# heater_spiral.set_pid(p=0.01, i=0.00031622776601683794, d=0)
#
#
# def begin_temperature_control_plan(heater : Heater):
#     yield from bps.mv(heater.override_pv, 1)
#     yield from bps.mv(heater.enable_pv, 1)
#
#
# def end_temperature_control_plan(heater : Heater):
#     yield from bps.mv(heater.override_pv, 0)
#     yield from bps.mv(heater.enable_pv, 0)
#
#
# def execute_temperature_control_plan(heater, times, temps, end_program_flag=False):
#     yield from begin_temperature_control_plan(heater)
#
#     time_start = ttime.time()
#
#     while True:
#         dt = ttime.time() - time_start
#         idxs = np.argsort(np.abs(dt - times))
#         temp_before, temp_after = temps[idxs[0]], temps[idxs[1]]
#         time_before, time_after = temps[idxs[0]], temps[idxs[1]]
#         rate = (temp_after - temp_before) / (time_after - time_before)
#         temp_setpoint = temp_before + rate * dt
#         heater.update_setpoint(temp_setpoint)
#         heater.update_output()
#         if dt > times.max():
#             break
#
#     if end_program_flag:
#         yield from end_temperature_control_plan(heater)
#
#
#
#
#
#
#
#
#
#
#
# def ramp_temperature_plan(t_ramp=3*60, T=400, p=0.01, i=0.01, d=0.001):
#     time, temp_rb, volt_out = [], [], []
#
#     pid = PID(p, i, d, setpoint=T_init)
#     pid.sample_time = 0.01
#     pid.output_limits = (0, 3.5)
#
#
#     time_start = ttime.time()
#     ramp_rate = (T - T_init) / t_ramp
#     while True:
#         dt = ttime.time() - time_start
#         if dt < t_ramp:
#             pid.setpoint = ramp_rate * dt + T_init
#         else:
#             pid.setpoint = T
#         print(pid.setpoint)
#         current_value = temp2.value
#         output = pid(current_value)
#         time.append(dt)
#         temp_rb.append(current_value)
#         volt_out.append(output)
#         RE(bps.mv(volt_override, output))
#
#         if dt > max_time:
#             break
#         # ttime.sleep(0.1)
#
#     RE(bps.mv(volt_override, 0))
#     RE(bps.mv(heater_enable2, 0))
#     RE(bps.mv(heater_override2, 0))