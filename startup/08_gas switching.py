'''


class SwitchValve(Device):
    open = Cpt(EpicsSignal, 'Cmd:Opn-Cmd')

switch_valve_1 = EpicsSignal('XF:08IDB-CT{DIODE-Box_B1:1}Out:1-Sel', name='switch_valve_1')
switch_valve_2 = EpicsSignal('XF:08IDB-CT{DIODE-Box_B1:1}Out:1-Sel', name='switch_valve_1')
switch_valve_3 = EpicsSignal('XF:08IDB-CT{DIODE-Box_B1:1}Out:1-Sel', name='switch_valve_1')
ghs_ch1_reactor = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:PSV0201}Cmd', name='ghs_ch1_reactor')
XF:08IDB-CT{DIODE-Box_B1:1}Out:1-Sel
'''