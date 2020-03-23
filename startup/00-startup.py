import time as ttime

from databroker import Broker
import bluesky.plan_stubs as bps
import numpy as np

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
# some_time_ago = now-1*1*3600
# d = arch_iss.tables_given_times(some_time_ago, now)
# print(d)