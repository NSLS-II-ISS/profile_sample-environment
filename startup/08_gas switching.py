
class SwitchValve(Device):
    state = Cpt(EpicsSignal, '-Sel')

    @property
    def status(self):
        return self.state.get()

    @property
    def direction(self):
        if self.status == 1:
            return 'reactor'
        else:
            return 'exhaust'

    def set(self, new_status):
        st = None
        for i in range(50):
            print_to_gui(f'Changing {self.name} valve status to {new_status} (attempt {i + 1})', tag='Gas program', add_timestamp=True)
            if self.status != new_status:
                st = self.state.set(new_status)
                st.wait()
                ttime.sleep(0.25)
            else:
                break
        if st is None:
            st = NullStatus()
        return st

    def set_to_reactor(self):
        # self.state.set(1)
        return self.set(1)

    def set_to_exhaust(self):
        # self.state.set(0)
        return self.set(0)

    def to_reactor(self):
        self.state.put(1)

    def to_exhaust(self):
        self.state.put(0)

    def put(self, value):
        self.set(value)
        # print_to_gui(f'Changing {self.name} valve status to {value}', tag='Gas program',
        #              add_timestamp=True)
        # self.state.put(value)



switch_valve_ghs_ch1 = SwitchValve('XF:08IDB-CT{DIODE-Box_B1:1}Out:0', name='switch_valve_ghs_ch1')
switch_valve_ghs_ch2 = SwitchValve('XF:08IDB-CT{DIODE-Box_B1:1}Out:2', name='switch_valve_ghs_ch2')
switch_valve_cart = SwitchValve('XF:08IDB-CT{DIODE-Box_B1:1}Out:1', name='switch_valve_cart')



switch_manifold = {'ghs_ch1': switch_valve_ghs_ch1,
                   'ghs_ch2': switch_valve_ghs_ch2,
                   'cart': switch_valve_cart}