

class MFC(Device):
    flow = Cpt(EpicsSignal, '}F-FB', write_pv='}F-SP')


mfc_cart_CH4 = MFC('XF:08IDB-CT{GC:01-MFC:01', name='mfc_cart_CH4')
mfc_cart_CH4.flow.tolerance = 0.1

mfc_cart_CO = MFC('XF:08IDB-CT{GC:01-MFC:02', name='mfc_cart_CO')
mfc_cart_CO.flow.tolerance = 0.1

mfc_cart_H2  = MFC('XF:08IDB-CT{GC:01-MFC:03', name='mfc_cart_H2')
mfc_cart_H2.flow.tolerance = 0.1



mfcs_cart= [mfc_cart_CH4,
            mfc_cart_CO,
            mfc_cart_H2,
            ]