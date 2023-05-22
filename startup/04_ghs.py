ghs_ch1_bypass_1 = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:BYP0301}Cmd', name='ghs_ch1_bypass_1')
ghs_ch1_bubbler1_1 = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:BII0301}Cmd', name='ghs_ch1_bypass_1') #XF:08IDB-UT{Gas:1-Vlv:BII0301}Cmd
ghs_ch1_bubbler1_2 = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:BOI0301}Cmd', name='ghs_ch1_bypass_1') #XF:08IDB-UT{Gas:1-Vlv:BOI0301}Cmd

ghs_ch1_bypass_2 = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:BYP0401}Cmd', name='ghs_ch1_bypass_2')
ghs_ch1_bubbler2_1 = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:BII0401}Cmd', name='ghs_ch1_bypass_2')
ghs_ch1_bubbler2_2 = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:BOI0401}Cmd', name='ghs_ch1_bypass_2')

ghs_ch2_bypass_1 = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:BYP0101}Cmd', name='ghs_ch2_bypass_1')
ghs_ch2_bubbler1_1 = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:BII0101}Cmd', name='ghs_ch2_bypass_1')
ghs_ch2_bubbler1_2 = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:BOI0101}Cmd', name='ghs_ch2_bypass_1')

ghs_ch2_bypass_2 = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:BYP0201}Cmd', name='ghs_ch2_bypass_2')
ghs_ch2_bubbler2_1 = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:BII0201}Cmd', name='ghs_ch2_bypass_2')
ghs_ch2_bubbler2_2 = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:BOI0201}Cmd', name='ghs_ch2_bypass_2')

ghs_ch1_reactor = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:PSV0201}Cmd', name='ghs_ch1_reactor')
ghs_ch1_exhaust = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:VSV0201}Cmd', name='ghs_ch1_reactor')
ghs_ch2_reactor = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:PSV0101}Cmd', name='ghs_ch2_reactor')
ghs_ch2_exhaust = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:VSV0101}Cmd', name='ghs_ch2_reactor')


ghs_mnf1_upstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:IIV0109}Cmd', name='ghs_mnf1_upstream')
ghs_mnf2_upstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:IIV0210}Cmd', name='ghs_mnf2_upstream')
ghs_mnf3_upstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:IIV0311}Cmd', name='ghs_mnf3_upstream')
ghs_mnf4_upstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:IIV0412}Cmd', name='ghs_mnf4_upstream')
ghs_mnf5_upstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:IIV0513}Cmd', name='ghs_mnf5_upstream')
ghs_mnf6_upstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:IIV0614}Cmd', name='ghs_mnf6_upstream')
ghs_mnf7_upstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:IIV0715}Cmd', name='ghs_mnf7_upstream')
ghs_mnf8_upstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:IIV0816}Cmd', name='ghs_mnf8_upstream')

ghs_mnf1_ch1_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV01}Cmd', name='ghs_mnf1_ch1_dnstream')
ghs_mnf2_ch1_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV02}Cmd', name='ghs_mnf2_ch1_dnstream')
ghs_mnf3_ch1_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV03}Cmd', name='ghs_mnf3_ch1_dnstream')
ghs_mnf4_ch1_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV04}Cmd', name='ghs_mnf4_ch1_dnstream')
ghs_mnf5_ch1_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV05}Cmd', name='ghs_mnf5_ch1_dnstream')
ghs_mnf6_ch1_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV06}Cmd', name='ghs_mnf6_ch1_dnstream')
ghs_mnf7_ch1_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV07}Cmd', name='ghs_mnf7_ch1_dnstream')
ghs_mnf8_ch1_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV08}Cmd', name='ghs_mnf8_ch1_dnstream')

ghs_mnf1_ch2_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV09}Cmd', name='ghs_mnf1_ch2_dnstream')
ghs_mnf2_ch2_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV10}Cmd', name='ghs_mnf2_ch2_dnstream')
ghs_mnf3_ch2_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV11}Cmd', name='ghs_mnf3_ch2_dnstream')
ghs_mnf4_ch2_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV12}Cmd', name='ghs_mnf4_ch2_dnstream')
ghs_mnf5_ch2_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV13}Cmd', name='ghs_mnf5_ch2_dnstream')
ghs_mnf6_ch2_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV14}Cmd', name='ghs_mnf6_ch2_dnstream')
ghs_mnf7_ch2_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV15}Cmd', name='ghs_mnf7_ch2_dnstream')
ghs_mnf8_ch2_dnstream = EpicsSignal('XF:08IDB-UT{Gas:1-Vlv:OIV16}Cmd', name='ghs_mnf8_ch2_dnstream')


ghs_ch1_mfc1_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:01}F:Target-SP', name='ghs_ch1_mfc1_sp')
ghs_ch1_mfc2_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:02}F:Target-SP', name='ghs_ch1_mfc2_sp')
ghs_ch1_mfc3_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:03}F:Target-SP', name='ghs_ch1_mfc3_sp')
ghs_ch1_mfc4_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:04}F:Target-SP', name='ghs_ch1_mfc4_sp')
ghs_ch1_mfc5_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:05}F:Target-SP', name='ghs_ch1_mfc5_sp')
ghs_ch1_mfc6_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:06}F:Target-SP', name='ghs_ch1_mfc6_sp')
ghs_ch1_mfc7_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:07}F:Target-SP', name='ghs_ch1_mfc7_sp')
ghs_ch1_mfc8_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:08}F:Target-SP', name='ghs_ch1_mfc8_sp')

ghs_ch2_mfc1_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:09}F:Target-SP', name='ghs_ch2_mfc1_sp')
ghs_ch2_mfc2_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:10}F:Target-SP', name='ghs_ch2_mfc2_sp')
ghs_ch2_mfc3_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:11}F:Target-SP', name='ghs_ch2_mfc3_sp')
ghs_ch2_mfc4_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:12}F:Target-SP', name='ghs_ch2_mfc4_sp')
ghs_ch2_mfc5_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:13}F:Target-SP', name='ghs_ch2_mfc5_sp')
ghs_ch2_mfc6_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:14}F:Target-SP', name='ghs_ch2_mfc6_sp')
ghs_ch2_mfc7_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:15}F:Target-SP', name='ghs_ch2_mfc7_sp')
ghs_ch2_mfc8_sp = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:16}F:Target-SP', name='ghs_ch2_mfc8_sp')


ghs_ch1_mfc1_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:01}F-I', name='ghs_ch1_mfc1_rb')
ghs_ch1_mfc2_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:02}F-I', name='ghs_ch1_mfc2_rb')
ghs_ch1_mfc3_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:03}F-I', name='ghs_ch1_mfc3_rb')
ghs_ch1_mfc4_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:04}F-I', name='ghs_ch1_mfc4_rb')
ghs_ch1_mfc5_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:05}F-I', name='ghs_ch1_mfc5_rb')
ghs_ch1_mfc6_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:06}F-I', name='ghs_ch1_mfc6_rb')
ghs_ch1_mfc7_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:07}F-I', name='ghs_ch1_mfc7_rb')
ghs_ch1_mfc8_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:08}F-I', name='ghs_ch1_mfc8_rb')

ghs_ch2_mfc1_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:09}F-I', name='ghs_ch2_mfc1_rb')
ghs_ch2_mfc2_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:10}F-I', name='ghs_ch2_mfc2_rb')
ghs_ch2_mfc3_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:11}F-I', name='ghs_ch2_mfc3_rb')
ghs_ch2_mfc4_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:12}F-I', name='ghs_ch2_mfc4_rb')
ghs_ch2_mfc5_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:13}F-I', name='ghs_ch2_mfc5_rb')
ghs_ch2_mfc6_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:14}F-I', name='ghs_ch2_mfc6_rb')
ghs_ch2_mfc7_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:15}F-I', name='ghs_ch2_mfc7_rb')
ghs_ch2_mfc8_rb = EpicsSignal('XF:08IDB-UT{Gas:1-MFC:16}F-I', name='ghs_ch2_mfc8_rb')

ghs_mnf1_gas_selector = EpicsSignal(read_pv='XF:08IDB-UT{Gas:1}Group:E-Sel', name='ghs_mnf1_gas_selector')
ghs_mnf2_gas_selector = EpicsSignal(read_pv='XF:08IDB-UT{Gas:1}Group:D-Sel', name='ghs_mnf2_gas_selector')
ghs_mnf3_gas_selector = EpicsSignal(read_pv='XF:08IDB-UT{Gas:1}Group:C-Sel', name='ghs_mnf3_gas_selector')
ghs_mnf4_gas_selector = EpicsSignal(read_pv='XF:08IDB-UT{Gas:1}Group:B-Sel', name='ghs_mnf4_gas_selector')
ghs_mnf5_gas_selector = EpicsSignal(read_pv='XF:08IDB-UT{Gas:1}Group:A-Sel', name='ghs_mnf5_gas_selector')

ghs = {'manifolds':
           {'1':
                {'gas_selector': ghs_mnf1_gas_selector,
                 'gases': {'Off': 'Close All',
                           'Helium': 'Helium - 13',
                           'Argon': 'Argon - 10',
                           'Nitrogen': 'Nitrogen - 12'}
                 },
            '2':
                {'gas_selector': ghs_mnf2_gas_selector,
                 'gases': {'Off': 'Close All',
                           'Hydrogen': 'Hydrogen - 08',
                           'Ammonia': 'Ammonia - 09'}
                 },

            '3':
                {'gas_selector': ghs_mnf3_gas_selector,
                 'gases': {'Off': 'Close All',
                           'Methane': 'Methane - 05',
                           'Ethylene': 'Ethylene - 06'}
                 },
            '4':
                {'gas_selector': ghs_mnf4_gas_selector,
                 'gases': {'Off': 'Close All',
                           'Nitric Oxide': 'Nitric Oxide - 04',
                           }
                 },
            '5':
                {'gas_selector': ghs_mnf5_gas_selector,
                 'gases': {'Off': 'Close All',
                           'Phosphine': 'Phosphine - 01',
                           'Arsine': 'Arsine - 02'
                           }
                 },

            },

       'channels':
           {'1':
                {'bypass1': ghs_ch1_bypass_1,
                 'bubbler1_1':ghs_ch1_bubbler1_1,
                 'bubbler1_2':ghs_ch1_bubbler1_2,
                 'bypass2': ghs_ch1_bypass_2,
                 'bubbler2_1':ghs_ch1_bubbler2_1,
                 'bubbler2_2':ghs_ch1_bubbler2_2,
                 'reactor': ghs_ch1_reactor,
                 'exhaust': ghs_ch1_exhaust,
                 'mnf1_vlv_upstream': ghs_mnf1_upstream,
                 'mnf2_vlv_upstream': ghs_mnf2_upstream,
                 'mnf3_vlv_upstream': ghs_mnf3_upstream,
                 'mnf4_vlv_upstream': ghs_mnf4_upstream,
                 'mnf5_vlv_upstream': ghs_mnf5_upstream,
                 'mnf6_vlv_upstream': ghs_mnf6_upstream,
                 'mnf7_vlv_upstream': ghs_mnf7_upstream,
                 'mnf8_vlv_upstream': ghs_mnf8_upstream,
                 'mnf1_vlv_dnstream': ghs_mnf1_ch1_dnstream,
                 'mnf2_vlv_dnstream': ghs_mnf2_ch1_dnstream,
                 'mnf3_vlv_dnstream': ghs_mnf3_ch1_dnstream,
                 'mnf4_vlv_dnstream': ghs_mnf4_ch1_dnstream,
                 'mnf5_vlv_dnstream': ghs_mnf5_ch1_dnstream,
                 'mnf6_vlv_dnstream': ghs_mnf6_ch1_dnstream,
                 'mnf7_vlv_dnstream': ghs_mnf7_ch1_dnstream,
                 'mnf8_vlv_dnstream': ghs_mnf8_ch1_dnstream,
                 'mfc1_sp': ghs_ch1_mfc1_sp,
                 'mfc2_sp': ghs_ch1_mfc2_sp,
                 'mfc3_sp': ghs_ch1_mfc3_sp,
                 'mfc4_sp': ghs_ch1_mfc4_sp,
                 'mfc5_sp': ghs_ch1_mfc5_sp,
                 'mfc6_sp': ghs_ch1_mfc6_sp,
                 'mfc7_sp': ghs_ch1_mfc7_sp,
                 'mfc8_sp': ghs_ch1_mfc8_sp,
                 'mfc1_rb': ghs_ch1_mfc1_rb,
                 'mfc2_rb': ghs_ch1_mfc2_rb,
                 'mfc3_rb': ghs_ch1_mfc3_rb,
                 'mfc4_rb': ghs_ch1_mfc4_rb,
                 'mfc5_rb': ghs_ch1_mfc5_rb,
                 'mfc6_rb': ghs_ch1_mfc6_rb,
                 'mfc7_rb': ghs_ch1_mfc7_rb,
                 'mfc8_rb': ghs_ch1_mfc8_rb,

                 },
            '2': {'bypass1': ghs_ch2_bypass_1,
                  'bubbler1_1': ghs_ch2_bubbler1_1,
                  'bubbler1_2': ghs_ch2_bubbler1_2,
                  'bypass2': ghs_ch2_bypass_2,
                  'bubbler2_1': ghs_ch2_bubbler2_1,
                  'bubbler2_2': ghs_ch2_bubbler2_2,
                  'reactor': ghs_ch2_reactor,
                  'exhaust': ghs_ch2_exhaust,
                  'mnf1_vlv_upstream': ghs_mnf1_upstream,
                  'mnf2_vlv_upstream': ghs_mnf2_upstream,
                  'mnf3_vlv_upstream': ghs_mnf3_upstream,
                  'mnf4_vlv_upstream': ghs_mnf4_upstream,
                  'mnf5_vlv_upstream': ghs_mnf5_upstream,
                  'mnf6_vlv_upstream': ghs_mnf6_upstream,
                  'mnf7_vlv_upstream': ghs_mnf7_upstream,
                  'mnf8_vlv_upstream': ghs_mnf8_upstream,
                  'mnf1_vlv_dnstream': ghs_mnf1_ch2_dnstream,
                  'mnf2_vlv_dnstream': ghs_mnf2_ch2_dnstream,
                  'mnf3_vlv_dnstream': ghs_mnf3_ch2_dnstream,
                  'mnf4_vlv_dnstream': ghs_mnf4_ch2_dnstream,
                  'mnf5_vlv_dnstream': ghs_mnf5_ch2_dnstream,
                  'mnf6_vlv_dnstream': ghs_mnf6_ch2_dnstream,
                  'mnf7_vlv_dnstream': ghs_mnf7_ch2_dnstream,
                  'mnf8_vlv_dnstream': ghs_mnf8_ch2_dnstream,
                  'mfc1_sp': ghs_ch2_mfc1_sp,
                  'mfc2_sp': ghs_ch2_mfc2_sp,
                  'mfc3_sp': ghs_ch2_mfc3_sp,
                  'mfc4_sp': ghs_ch2_mfc4_sp,
                  'mfc5_sp': ghs_ch2_mfc5_sp,
                  'mfc6_sp': ghs_ch2_mfc6_sp,
                  'mfc7_sp': ghs_ch2_mfc7_sp,
                  'mfc8_sp': ghs_ch2_mfc8_sp,
                  'mfc1_rb': ghs_ch2_mfc1_rb,
                  'mfc2_rb': ghs_ch2_mfc2_rb,
                  'mfc3_rb': ghs_ch2_mfc3_rb,
                  'mfc4_rb': ghs_ch2_mfc4_rb,
                  'mfc5_rb': ghs_ch2_mfc5_rb,
                  'mfc6_rb': ghs_ch2_mfc6_rb,
                  'mfc7_rb': ghs_ch2_mfc7_rb,
                  'mfc8_rb': ghs_ch2_mfc8_rb,


                  },
            }
       }

# ghs_channel =  { 1: [ghs_ch1_mfc1_rb,
#                 ghs_ch1_mfc2_rb,
#                 ghs_ch1_mfc3_rb,
#                 ghs_ch1_mfc4_rb,
#                 ghs_ch1_mfc5_rb,
#                 ghs_ch1_mfc6_rb,],
#                  2: [ghs_ch2_mfc1_rb,
#                      ghs_ch2_mfc2_rb,
#                      ghs_ch2_mfc3_rb,
#                      ghs_ch2_mfc4_rb,
#                      ghs_ch2_mfc5_rb,
#                      ghs_ch2_mfc6_rb,
#                      ghs_ch2_mfc7_rb,
#                      ghs_ch2_mfc8_rb,]}
#
# for key in ghs_channel.keys():
#     for mfc in ghs_channel[key]:
#         arch_iss.pvs.update({mfc.name: mfc.pvname})

arch_iss.pvs.update({ghs_ch1_mfc1_rb.name : ghs_ch1_mfc1_rb.pvname})
arch_iss.pvs.update({ghs_ch1_mfc2_rb.name : ghs_ch1_mfc2_rb.pvname})
arch_iss.pvs.update({ghs_ch1_mfc3_rb.name : ghs_ch1_mfc3_rb.pvname})
arch_iss.pvs.update({ghs_ch1_mfc4_rb.name : ghs_ch1_mfc4_rb.pvname})
arch_iss.pvs.update({ghs_ch1_mfc5_rb.name : ghs_ch1_mfc5_rb.pvname})
arch_iss.pvs.update({ghs_ch1_mfc6_rb.name : ghs_ch1_mfc6_rb.pvname})
arch_iss.pvs.update({ghs_ch1_mfc7_rb.name : ghs_ch1_mfc7_rb.pvname})
arch_iss.pvs.update({ghs_ch1_mfc8_rb.name : ghs_ch1_mfc8_rb.pvname})
#
#
arch_iss.pvs.update({ghs_ch2_mfc1_rb.name : ghs_ch2_mfc1_rb.pvname})
arch_iss.pvs.update({ghs_ch2_mfc2_rb.name : ghs_ch2_mfc2_rb.pvname})
arch_iss.pvs.update({ghs_ch2_mfc3_rb.name : ghs_ch2_mfc3_rb.pvname})
arch_iss.pvs.update({ghs_ch2_mfc4_rb.name : ghs_ch2_mfc4_rb.pvname})
arch_iss.pvs.update({ghs_ch2_mfc5_rb.name : ghs_ch2_mfc5_rb.pvname})
arch_iss.pvs.update({ghs_ch2_mfc6_rb.name : ghs_ch2_mfc6_rb.pvname})
arch_iss.pvs.update({ghs_ch2_mfc7_rb.name : ghs_ch2_mfc7_rb.pvname})
arch_iss.pvs.update({ghs_ch2_mfc8_rb.name : ghs_ch2_mfc8_rb.pvname})

def flow(gas, channel=0, flow_rate=0):
    if channel == 1:
        ch_name = 'ch1'
    else:
        ch_name = 'ch2'
    gases = {'He': {'ch1': {
                        'mfc':ghs_ch1_mfc1_sp,
                        'selector': ghs_mnf1_gas_selector,
                        'manifold':'1',
                        'valves': [ghs_mnf1_upstream, ghs_mnf1_ch1_dnstream]},
                    'ch2': {
                        'mfc': ghs_ch2_mfc1_sp,
                        'selector': ghs_mnf1_gas_selector,
                        'manifold': '1',
                        'valves': [ghs_mnf1_upstream, ghs_mnf1_ch2_dnstream]},
                    'full_gas_name': 'Helium'},
            'Ar': {'ch1': {
                        'mfc':ghs_ch1_mfc1_sp,
                        'selector': ghs_mnf1_gas_selector,
                        'manifold': '1',
                        'valves': [ghs_mnf1_upstream, ghs_mnf1_ch1_dnstream]},
                    'ch2': {
                        'mfc': ghs_ch2_mfc1_sp,
                        'selector': ghs_mnf1_gas_selector,
                        'manifold': '1',
                        'valves': [ghs_mnf1_upstream, ghs_mnf1_ch2_dnstream]},
                    'full_gas_name': 'Argon'},
            'N2': {'ch1': {
                       'mfc':ghs_ch1_mfc1_sp,
                       'selector': ghs_mnf1_gas_selector,
                        'manifold': '1',
                        'valves': [ghs_mnf1_upstream, ghs_mnf1_ch1_dnstream]},
                   'ch2': {
                       'mfc': ghs_ch2_mfc1_sp,
                       'selector': ghs_mnf1_gas_selector,
                       'manifold': '1',
                       'valves': [ghs_mnf1_upstream, ghs_mnf1_ch2_dnstream]},
                    'full_gas_name': 'Nitrogen'},
            'O2': {'ch1': {
                        'mfc': ghs_ch1_mfc6_sp,
                        'selector': None,
                        'manifold': None,
                        'valves': [ghs_mnf6_upstream, ghs_mnf6_ch1_dnstream]},
                    'ch2': {
                        'mfc': ghs_ch2_mfc6_sp,
                        'selector': None,
                        'manifold': None,
                        'valves': [ghs_mnf6_upstream, ghs_mnf6_ch2_dnstream]},
                    'full_gas_name': 'Oxygen'},
            'CO2': {'ch1': {
                        'mfc': ghs_ch1_mfc8_sp,
                        'selector': None,
                        'manifold': None,
                        'valves': [ghs_mnf8_upstream, ghs_mnf8_ch1_dnstream]},
                    'ch2': {
                        'mfc': ghs_ch2_mfc8_sp,
                        'selector': None,
                        'manifold': None,
                        'valves': [ghs_mnf8_upstream, ghs_mnf8_ch2_dnstream]},
                    'full_gas_name': 'Carbon Dioxide'},
            'CH4': {'ch1': {
                        'mfc': mfc_cart_1,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_ch4]},
                    'ch2': {
                        'mfc': mfc_cart_1,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_ch4]},
                    'full_gas_name': 'Methane'},
            'CO': {'ch1': {
                       'mfc': mfc_cart_2,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_co]},
                    'ch2': {
                        'mfc': mfc_cart_2,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_co]},
                    'full_gas_name': 'Carbon Monoxide'},
            'H2': {'ch1': {
                        'mfc': mfc_cart_3,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_h2]},
                    'ch2': {
                        'mfc': mfc_cart_3,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_h2]},
                    'full_gas_name': 'Hydrogen'}
    }
    #open or close valves
    for valve in gases[gas][ch_name]['valves']:
        if flow_rate > 0:
             valve.set(1)
        else:
            valve.set(0)
    if gases[gas][ch_name]['manifold']:
        indx_mnf = gases[gas][ch_name]['manifold']
        gas_command = ghs['manifolds'][indx_mnf]['gases'][gases[gas]['full_gas_name']]
        # print(f'Gas command {gas_command}')
        ghs['manifolds'][indx_mnf]['gas_selector'].set(gas_command)

    gases[gas][ch_name]['mfc'].set(flow_rate)

