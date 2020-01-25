


class MFC1(Device):
    flow = Cpt(EpicsSignal, 'I}MFC1_FB', write_pv='O}MFC1_SP')

class MFC2(Device):
    flow = Cpt(EpicsSignal, 'I}MFC2_FB', write_pv='O}MFC2_SP')

class MFC3(Device):
    flow = Cpt(EpicsSignal, 'I}MFC3_FB', write_pv='O}MFC3_SP')


mfc_cart_CH4 = MFC1('XF:08IDB-CT{MFC-A', name='mfc_cart_CH4')

mfc_cart_CH4.flow.tolerance = 0.1
mfc_cart_CO  = MFC2('XF:08IDB-CT{MFC-A', name='mfc_cart_CO')
mfc_cart_CO.flow.tolerance = 0.1

mfc_cart_H2  = MFC3('XF:08IDB-CT{MFC-A', name='mfc_cart_H2')
mfc_cart_H2.flow.tolerance = 0.1

