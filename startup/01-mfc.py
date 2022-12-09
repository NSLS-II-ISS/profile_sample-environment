

class MFC(Device):
    rb = Cpt(EpicsSignal, '-I', write_pv='-SP')
    sp = Cpt(EpicsSignal,'-SP')


mfc_cart_1 = MFC('XF:08IDB-CT{GC:1-MFC:1}Gas:Flow', name='mfc_cart_CH4')
mfc_cart_1.rb.tolerance = 0.1

mfc_cart_2 = MFC('XF:08IDB-CT{GC:1-MFC:2}Gas:Flow', name='mfc_cart_CO')
mfc_cart_2.rb.tolerance = 0.1

mfc_cart_3  = MFC('XF:08IDB-CT{GC:1-MFC:3}Gas:Flow', name='mfc_cart_H2')
mfc_cart_3.rb.tolerance = 0.1

total_flow_meter = MFC('XF:08IDB-CT{GC:1-MFC:4}Gas:Flow', name='mfc_cart_H2')
total_flow_meter.rb.tolerance = 0.1




class ShutoffValve(Device):
    open = Cpt(EpicsSignal, 'Cmd:Opn-Cmd')
    close = Cpt(EpicsSignal, 'Cmd:Cls-Cmd')
    status =Cpt(EpicsSignal, 'Pos-Sts')

valve_ch4 = ShutoffValve('XF:08IDB-VA{LDOCK-BV:1}', name = 'valve_CH4')
valve_co = ShutoffValve('XF:08IDB-VA{SPEC:2-BV:1}', name = 'valve_CO')
valve_h2 = ShutoffValve('XF:08IDB-VA{SCHM-BV:1}', name = 'valve_H2')


gas_cart= [mfc_cart_1,
            mfc_cart_2,
            mfc_cart_3,
            valve_ch4,
            valve_co,
            valve_h2 ]