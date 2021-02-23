

temp1 = EpicsSignal('XF:08IDB-CT{ES-TC}T1-I', name='temp1')
temp2 = EpicsSignal('XF:08IDB-CT{ES-TC}T2-I', name='temp2')

temps = [temp1, temp2]

for temp in temps:
    arch_iss.pvs.update({temp.name: temp.pvname})


heater_enable1 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}T-HtrEna-Cmd', name='heater_enable1')
pid_p1 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}T-Kp', name='pid_p1')
pid_i1 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}T-Ki', name='pid_i1')
pid_d1 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}T-Kd', name='pid_d1')
curr_rb = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}A-AI', name='curr_rb')


heater_enable2 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-HtrEna-Cmd', name='heater_enable2')
heater_override2 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-HtrOverR-Cmd', name='heater_override2')
pid_p2 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-Kp', name='pid_p2')
pid_i2 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-Ki', name='pid_i2')
pid_d2 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-Kd', name='pid_d2')
volt_rb = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}V-AI', name='volt_rb')
volt_override = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}V-AO', name='volt_override')


temp_sp1 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:1}T-SP', name='temp_sp1')
temp_sp2 = EpicsSignal('XF:08IDB-OP{Smpl-Heater:2}T-SP', name='temp_sp2')
arch_iss.pvs.update({temp_sp1.name: temp_sp1.pvname})

temps_sp = [temp_sp1] #, temp_sp2]
#
# for temp in temps_sp:
#     arch_iss.pvs.update({temp.name: temp.pvname})