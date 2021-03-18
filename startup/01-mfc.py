

class MFC(Device):
    rb = Cpt(EpicsSignal, '-I', write_pv='-SP')
    sp = Cpt(EpicsSignal,'-SP')


mfc_cart_1 = MFC('XF:08IDB-CT{GC:1-MFC:1}Gas:Flow', name='mfc_cart_CH4')
mfc_cart_1.rb.tolerance = 0.1

mfc_cart_2 = MFC('XF:08IDB-CT{GC:1-MFC:2}Gas:Flow', name='mfc_cart_CO')
mfc_cart_2.rb.tolerance = 0.1

mfc_cart_3  = MFC('XF:08IDB-CT{GC:1-MFC:3}Gas:Flow', name='mfc_cart_H2')
mfc_cart_3.rb.tolerance = 0.1



mfcs_cart= [mfc_cart_1,
            mfc_cart_2,
            mfc_cart_3,
            ]