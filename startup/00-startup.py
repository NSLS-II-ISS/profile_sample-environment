import time as ttime

from databroker import Broker


from ophyd import (ProsilicaDetector, SingleTrigger, Component as Cpt, Device,
                   EpicsSignal, EpicsSignalRO, ImagePlugin, StatsPlugin, ROIPlugin,
                   DeviceStatus)


db_archiver = Broker.named('iss-archiver')
arch_iss  = db_archiver.event_sources_by_name['arch_iss']


from bluesky import RunEngine

from bluesky.utils import get_history
RE = RunEngine({})


from bluesky.utils import ts_msg_hook

RE.msg_hook = ts_msg_hook


temp1 = EpicsSignal('XF:08IDB-CT{ES-TC}T2-I', name='temp1')


rga_ch1 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID1-I',name ='rga_ch1')
rga_ch2 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID2-I',name ='rga_ch2')
rga_ch3 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID3-I',name ='rga_ch3')
rga_ch4 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID4-I',name ='rga_ch4')
rga_ch5 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID5-I',name ='rga_ch5')
rga_ch6 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID6-I',name ='rga_ch6')
rga_ch7 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID7-I',name ='rga_ch7')
rga_ch8 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID8-I',name ='rga_ch8')
rga_ch9 = EpicsSignal('XF:08IDB-VA{RGA:1}P:MID9-I',name ='rga_ch9')




mass1=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID1-SP', name='mass1')
mass2=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID2-SP', name='mass1')
mass3=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID3-SP', name='mass1')
mass4=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID4-SP', name='mass1')
mass5=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID5-SP', name='mass1')
mass6=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID6-SP', name='mass1')
mass7=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID7-SP', name='mass1')
mass8=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID8-SP', name='mass1')
mass9=EpicsSignal('XF:08IDB-VA{RGA:1}Mass:MID9-SP', name='mass1')

rga_channels = [rga_ch1,
                rga_ch2,
                rga_ch3,
                rga_ch4,
                rga_ch5,
                rga_ch6,
                rga_ch7,
                rga_ch8,
                rga_ch9,
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
                ]
for pv in rga_channels:
    arch_iss.pvs.update({pv.name: pv.pvname})


# # month_ago = ttime.time()-1*24*3600now = ttime.time()
# # some_time_ago = ttime.time()-1*24*3600
# # now = ttime.time()
# # d = arch_iss.tables_given_times(month_ago, now)
# # d
# # d = arch_iss.tables_given_times(some_time_ago, now)
# # d
# # !vi /etc/databroker/iss-archiver.yml
# # from pandas import DataFrame
# # df = DataFrame
# # df = DataFrame()
# # df
# # df?
# # import pandas as pd
# # pd.to_datetime
# # pd.to_datetime?

# now = ttime.time()
# some_time_ago = now-3600/2
# d = arch_iss.tables_given_times(some_time_ago, now)

