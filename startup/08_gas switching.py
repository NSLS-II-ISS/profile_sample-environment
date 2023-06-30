
class SwitchValve(Device):
    state = Cpt(EpicsSignal, -Sel)

    def to_reactor():
        state.set(1)

    def to_exhaust():
        state.set(0)


switch_valve_1 = SwitchValve('XF:08IDB-CT{DIODE-Box_B1:1}Out:0-', name='switch_valve_1')
switch_valve_2 = SwitchValve('XF:08IDB-CT{DIODE-Box_B1:1}Out:1', name='switch_valve_1')
switch_valve_3 = SwitchValve('XF:08IDB-CT{DIODE-Box_B1:1}Out:2', name='switch_valve_1')