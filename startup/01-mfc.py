

class MFC(Device):
    rb = Cpt(EpicsSignal, '-I', write_pv='-SP')
    sp = Cpt(EpicsSignal,'-SP')

    def set(self, flow_rate):
        return self.sp.set(flow_rate)

    def put(self, flow_rate):
        self.sp.put(flow_rate)


mfc_cart_1 = MFC('XF:08IDB-CT{GC:1-MFC:1}Gas:Flow', name='mfc_cart_CH4')
mfc_cart_1.rb.tolerance = 0.1

mfc_cart_2 = MFC('XF:08IDB-CT{GC:1-MFC:2}Gas:Flow', name='mfc_cart_CO')
mfc_cart_2.rb.tolerance = 0.1

mfc_cart_3  = MFC('XF:08IDB-CT{GC:1-MFC:3}Gas:Flow', name='mfc_cart_H2')
mfc_cart_3.rb.tolerance = 0.1

mfc_cart_inert = MFC('XF:08IDB-CT{GC:1-MFC:6}Gas:Flow', name='mfc_cart_iner')
mfc_cart_inert.rb.tolerance = 0.1

total_flow_meter = MFC('XF:08IDB-CT{GC:1-MFC:4}Gas:Flow', name='mfc_total_flow_meter')
total_flow_meter.rb.tolerance = 0.1



from ophyd.sim import NullStatus
class ShutoffValve(Device):
    open = Cpt(EpicsSignal, 'Cmd:Opn-Cmd')
    close = Cpt(EpicsSignal, 'Cmd:Cls-Cmd')
    status =Cpt(EpicsSignal, 'Pos-Sts')

    def set(self, status):
        st = None
        for i in range(50):
            print_to_gui(f'Changing {self.name} valve status to {status} (attempt {i + 1})', tag='Gas program', add_timestamp=True)
            if self.status.get() != status:
                if status == 0:
                    st = self.close.set(1)
                else:
                    st = self.open.set(1)
                st.wait()
                ttime.sleep(0.25)
            else:
                break
        if st is None:
            st = NullStatus()
        return st

    def put(self, status):
        self.set(status)

# valve_ch4 = ShutoffValve('XF:08IDB-VA{LDOCK-BV:1}', name = 'valve_CH4')
# valve_co = ShutoffValve('XF:08IDB-VA{SPEC:2-BV:1}', name = 'valve_CO')
# valve_h2 = ShutoffValve('XF:08IDB-VA{SCHM-BV:1}', name = 'valve_H2')

valve_ch4 = ShutoffValve('XF:08IDB-CT{GC:01-BV:2}', name = 'valve_CH4')
valve_co = ShutoffValve('XF:08IDB-CT{GC:01-BV:3}', name = 'valve_CO')
valve_h2 = ShutoffValve('XF:08IDB-CT{GC:01-BV:1}', name = 'valve_H2')


gas_cart= {1: {'mfc': mfc_cart_1, 'vlv': valve_ch4},
           2: {'mfc': mfc_cart_2, 'vlv': valve_co},
           3: {'mfc': mfc_cart_3, 'vlv': valve_h2},
           4: {'mfc': mfc_cart_inert, 'vlv': None}}

class MobileGasSystem(Device):

    reset_module1 = Cpt(EpicsSignal,'XF:08IDB-CT{DIODE-Box_B3:1}ModuleReconfig-Cmd')
    reset_module2 = Cpt(EpicsSignal, 'XF:08IDB-CT{DIODE-Box_B3:2}ModuleReconfig-Cmd')
    reset_module3 = Cpt(EpicsSignal, 'XF:08IDB-CT{DIODE-Box_B3:3}ModuleReconfig-Cmd')
    reset_module4 = Cpt(EpicsSignal, 'XF:08IDB-CT{DIODE-Box_B3:4}ModuleReconfig-Cmd')


    def reset(self):
        self.reset_module1.set(1)
        self.reset_module2.set(1)
        self.reset_module3.set(1)
        self.reset_module4.set(1)


mobile_gh_system =  MobileGasSystem(name='mghs')

arch_iss.pvs.update({mfc_cart_1.rb.name : mfc_cart_1.rb.pvname})
arch_iss.pvs.update({mfc_cart_2.rb.name : mfc_cart_2.rb.pvname})
arch_iss.pvs.update({mfc_cart_3.rb.name : mfc_cart_3.rb.pvname})
arch_iss.pvs.update({total_flow_meter.rb.name : total_flow_meter.rb.pvname})



class FlowConditionValves(Device):

    valve1 = Cpt(EpicsSignal, 'Out:3-Sel', name='valve1')
    valve2 = Cpt(EpicsSignal, 'Out:4-Sel', name='valve2')
    valve3 = Cpt(EpicsSignal, 'Out:5-Sel', name='valve3')
    valve4 = Cpt(EpicsSignal, 'Out:6-Sel', name='valve4')



flow_condition_valves = FlowConditionValves('XF:08IDB-CT{DIODE-Box_B1:1}', name='flow_condition_valves')

class PDU(Device):
    module1 = Cpt(EpicsSignal, 'Sw:1-Sel', name='module1')
    module2 = Cpt(EpicsSignal, 'Sw:2-Sel', name='module2')
    module3 = Cpt(EpicsSignal, 'Sw:3-Sel', name='module3')
    module4 = Cpt(EpicsSignal, 'Sw:4-Sel', name='module4')
    module5 = Cpt(EpicsSignal, 'Sw:5-Sel', name='module5')
    module6 = Cpt(EpicsSignal, 'Sw:6-Sel', name='module6')
    module7 = Cpt(EpicsSignal, 'Sw:7-Sel', name='module7')
    module8 = Cpt(EpicsSignal, 'Sw:8-Sel', name='module8')

pdu3 = PDU('XF:08IDB-CT{PDU:3}', name='pdu3')