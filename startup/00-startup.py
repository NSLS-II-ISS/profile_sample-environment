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
rga_ch2 = EpicsSignal('XF:08IDB-VA{RGA:2}P:MID1-I',name ='rga_ch2')
rga_ch3 = EpicsSignal('XF:08IDB-VA{RGA:3}P:MID1-I',name ='rga_ch3')
rga_ch4 = EpicsSignal('XF:08IDB-VA{RGA:4}P:MID1-I',name ='rga_ch4')
rga_ch5 = EpicsSignal('XF:08IDB-VA{RGA:5}P:MID1-I',name ='rga_ch5')
rga_ch6 = EpicsSignal('XF:08IDB-VA{RGA:6}P:MID1-I',name ='rga_ch6')
rga_ch7 = EpicsSignal('XF:08IDB-VA{RGA:7}P:MID1-I',name ='rga_ch7')
rga_ch8 = EpicsSignal('XF:08IDB-VA{RGA:8}P:MID1-I',name ='rga_ch8')
rga_ch9 = EpicsSignal('XF:08IDB-VA{RGA:9}P:MID1-I',name ='rga_ch9')


for pv in [rga_ch1]:
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
# # d = arch_iss.tables_given_times(some_time_ago, now)
# # d['rga1'].plot(x='time', y='data')
# # d['rga_ch1'].plot(x='time', y='data')
