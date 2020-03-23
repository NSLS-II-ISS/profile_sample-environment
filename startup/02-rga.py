
rga_ch1 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID1-I',name ='rga_ch1')
rga_ch2 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID2-I',name ='rga_ch2')
rga_ch3 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID3-I',name ='rga_ch3')
rga_ch4 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID4-I',name ='rga_ch4')
rga_ch5 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID5-I',name ='rga_ch5')
rga_ch6 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID6-I',name ='rga_ch6')
rga_ch7 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID7-I',name ='rga_ch7')
rga_ch8 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID8-I',name ='rga_ch8')
#rga_ch9 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID9-I',name ='rga_ch9')




mass1=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID1-SP', name='mass1')
mass2=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID2-SP', name='mass1')
mass3=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID3-SP', name='mass1')
mass4=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID4-SP', name='mass1')
mass5=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID5-SP', name='mass1')
mass6=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID6-SP', name='mass1')
mass7=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID7-SP', name='mass1')
mass8=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID8-SP', name='mass1')
#mass9=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID9-SP', name='mass1')

rga_channels = [rga_ch1,
                rga_ch2,
                rga_ch3,
                rga_ch4,
                rga_ch5,
                rga_ch6,
                rga_ch7,
                rga_ch8,
                #rga_ch9,
                ]

rga_masses =   [mass1,
                mass2,
                mass3,
                mass4,
                mass5,
                mass6,
                mass7,
                mass8,
                #mass9,
                ]

for pv in rga_channels:
    arch_iss.pvs.update({pv.name: pv.pvname})