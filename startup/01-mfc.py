


class MFC(Device):
    flow = Cpt(EpicsSignal, 'I}MFC1_FB', write_pv='O}MFC1_SP')




mfc_cart_CH4 = MFC('XF:08IDB-CT{MFC-A', name='mfc_cart_CH4')

mfc_cart_CH4.flow.tolerance = 0.1
mfc_cart_CO  = MFC('XF:08IDB-CT{MFC-A', name='mfc_cart_CO')
mfc_cart_CO.flow.tolerance = 0.1

mfc_cart_H2  = MFC('XF:08IDB-CT{MFC-A', name='mfc_cart_H2')
mfc_cart_H2.flow.tolerance = 0.1

