
#WIP
rga_ch1 = EpicsSignal('XF:08IDB-SE{RGA:1}P:MID1-I',name ='rga_ch1')
rga_ch2 = EpicsSignal('XF:08IDB-SE{RGA:1}P:MID2-I',name ='rga_ch2')
rga_ch3 = EpicsSignal('XF:08IDB-SE{RGA:1}P:MID3-I',name ='rga_ch3')
rga_ch4 = EpicsSignal('XF:08IDB-SE{RGA:1}P:MID4-I',name ='rga_ch4')
rga_ch5 = EpicsSignal('XF:08IDB-SE{RGA:1}P:MID5-I',name ='rga_ch5')
rga_ch6 = EpicsSignal('XF:08IDB-SE{RGA:1}P:MID6-I',name ='rga_ch6')
rga_ch7 = EpicsSignal('XF:08IDB-SE{RGA:1}P:MID7-I',name ='rga_ch7')
rga_ch8 = EpicsSignal('XF:08IDB-SE{RGA:1}P:MID8-I',name ='rga_ch8')
rga_ch9 = EpicsSignal('XF:08IDB-SE{RGA:1}P:MID9-I',name ='rga_ch9')
rga_ch10 = EpicsSignal('XF:08IDB-SE{RGA:1}P:MID10-I',name ='rga_ch10')




mass1=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID1', name='mass1')
mass2=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID2', name='mass2')
mass3=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID3', name='mass3')
mass4=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID4', name='mass4')
mass5=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID5', name='mass5')
mass6=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID6', name='mass6')
mass7=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID7', name='mass7')
mass8=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID8', name='mass8')
mass9=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID9', name='mass9')
mass10=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID10', name='mass10')

rga_channels = [rga_ch1,
                rga_ch2,
                rga_ch3,
                rga_ch4,
                rga_ch5,
                rga_ch6,
                rga_ch7,
                rga_ch8,
                rga_ch9,
                rga_ch10,
                ]

rga_masses =   [mass1,
                mass2,
                mass3,
                mass4,
                mass5,
                mass6,
                mass7,
                mass8,
                mass9,
                mass10,
                ]



for pv in rga_channels:
    arch_iss.pvs.update({pv.name: pv.pvname})

rga_ch_on = [EpicsSignal('XF:08IDB-VA{RGA:1}Cmd:MID1Set-Cmd_', name='rga_ch1_status'),
            EpicsSignal('XF:08IDB-VA{RGA:1}Cmd:MID2Set-Cmd_', name='rga_ch2_status'),
            EpicsSignal('XF:08IDB-VA{RGA:1}Cmd:MID3Set-Cmd_', name='rga_ch3_status'),
            EpicsSignal('XF:08IDB-VA{RGA:1}Cmd:MID4Set-Cmd_', name='rga_ch4_status'),
            EpicsSignal('XF:08IDB-VA{RGA:1}Cmd:MID5Set-Cmd_', name='rga_ch5_status'),
            EpicsSignal('XF:08IDB-VA{RGA:1}Cmd:MID6Set-Cmd_', name='rga_ch6_status'),
            EpicsSignal('XF:08IDB-VA{RGA:1}Cmd:MID7Set-Cmd_', name='rga_ch7_status'),
            EpicsSignal('XF:08IDB-VA{RGA:1}Cmd:MID8Set-Cmd_', name='rga_ch8_status'),
            EpicsSignal('XF:08IDB-VA{RGA:1}Cmd:MID9Set-Cmd_', name='rga_ch9_status'),
             ]

rga_ch_type = [EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID1Detr-Sel', name='rga_ch1_type'),
               EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID2Detr-Sel', name='rga_ch2_type'),
               EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID3Detr-Sel', name='rga_ch3_type'),
               EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID4Detr-Sel', name='rga_ch4_type'),
               EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID5Detr-Sel', name='rga_ch5_type'),
               EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID6Detr-Sel', name='rga_ch6_type'),
               EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID7Detr-Sel', name='rga_ch7_type'),
               EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID8Detr-Sel', name='rga_ch8_type'),
               EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID9Detr-Sel', name='rga_ch9_type'),
               ]


rga_detectors = [EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID1Detr-Sel', name='rga_ch1_detector'),
                EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID1Detr-Sel', name='rga_ch2_detector'),
                EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID1Detr-Sel', name='rga_ch3_detector'),
                EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID1Detr-Sel', name='rga_ch4_detector'),
                EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID1Detr-Sel', name='rga_ch5_detector'),
                EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID1Detr-Sel', name='rga_ch6_detector'),
                EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID1Detr-Sel', name='rga_ch7_detector'),
                EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID1Detr-Sel', name='rga_ch8_detector'),
                EpicsSignal('XF:08IDB-VA{RGA:1}Type:MID1Detr-Sel', name='rga_ch9_detector'),
                 ]





rga_ioc_reset = EpicsSignal('XF:08IDB-CT{IOC:RGA1}:SysReset')
rga_reset_environment = EpicsSignal('XF:08IDB-VA{RGA:1}Cmd:Env-Cmd',name='rga_reset_environment')
rga_start_mid_scan = EpicsSignal('XF:08IDB-VA{RGA:1}Cmd:MID_Start-Cmd',name='rga_start_mid_scan')

class RGA(Device):
    open_exp = Cpt(EpicsSignal, 'OpenExp', name='open_exp')
    experiment_name = Cpt(EpicsSignal,'ExpName', name='experiment_name')
    acquire = Cpt(EpicsSignal,'Acquire', name='acquire')
    run_exp = Cpt(EpicsSignal, 'RunExp', name='run_exp')
    abort_exp = Cpt(EpicsSignal, 'AbortExp', name='abort_exp')
    close_exp = Cpt(EpicsSignal, 'CloseExp', name='close_exp')


    def start(self, filename=None, **kwargs):
        self.experiment_name.set(filename)
        print(f"Starting the RAG using following template file: {filename}.....................")
        ttime.sleep(1)
        self.open_exp.set(1)
        ttime.sleep(5)
        self.run_exp.set(1)
        ttime.sleep(5)
        self.acquire.set(1)

    def stop(self):
        print("Stopping the RGA....................")
        self.acquire.set(0)
        ttime.sleep(1)
        self.abort_exp.set(1)
        ttime.sleep(5)
        self.close_exp.set(1)
        ttime.sleep(1)

rga = RGA('XF:08IDB-SE{RGA:1}:', name = 'rga')

def reset_rga(masses_sp = [2,4,12,16,18,28,32,40,44]):
    yield from bps.mv(rga_ioc_reset, 1)
    yield from bps.sleep(5)
    yield from bps.mv(rga_reset_environment,1)
    for signal in rga_ch_on:
        yield from bps.mv(signal,1)

    for mass, mass_ch in zip(masses_sp,rga_masses):
        yield from bps.mv(mass_ch,mass)

    for ch in rga_ch_type:
        yield from bps.mv(ch,0)

    yield from bps.sleep(2)
    yield from bps.mv(rga_start_mid_scan,1)


     # def reset(self):
     #     XF:08IDB-VA{RGA: 1}Mass:MID1-SP
#
#     @property
#     def status(self):
#         return self.state.get()
#
#     @property
#     def direction(self):
#         if self.status == 1:
#             return 'reactor'
#         else:
#             return 'exhaust'
#
#     def set(self, new_status):
#         st = None
#         for i in range(50):
#             print_to_gui(f'Changing {self.name} valve status to {new_status} (attempt {i + 1})', tag='Gas program', add_timestamp=True)
#             if self.status != new_status:
#                 st = self.state.set(new_status)
#                 st.wait()
#                 ttime.sleep(0.25)
#             else:
#                 break
#         if st is None:
#             st = NullStatus()
#         return st
#
#     def set_to_reactor(self):
#         # self.state.set(1)
#         return self.set(1)
#
#     def set_to_exhaust(self):
#         # self.state.set(0)
#         return self.set(0)
#
#     def to_reactor(self):
#         self.state.put(1)
#
#     def to_exhaust(self):
#         self.state.put(0)
#
#     def put(self, value):
#         self.set(value)
#         # print_to_gui(f'Changing {self.name} valve status to {value}', tag='Gas program',
#         #              add_timestamp=True)
#         # self.state.put(value)
#
#
#
# switch_valve_ghs_ch1 = SwitchValve('XF:08IDB-CT{DIODE-Box_B1:1}Out:0', name='switch_valve_ghs_ch1')
# switch_valve_ghs_ch2 = SwitchValve('XF:08IDB-CT{DIODE-Box_B1:1}Out:2', name='switch_valve_ghs_ch2')
# switch_valve_cart = SwitchValve('XF:08IDB-CT{DIODE-Box_B1:1}Out:1', name='switch_valve_cart')
#
#
#
# switch_manifold = {'ghs_ch1': switch_valve_ghs_ch1,
#                    'ghs_ch2': switch_valve_ghs_ch2,
#                    'cart': switch_valve_cart}