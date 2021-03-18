import time as ttime

from databroker.v0 import Broker

import bluesky
from distutils.version import LooseVersion
from datetime import datetime
import time
from pathlib import Path
from timeit import default_timer as timer





import bluesky.plan_stubs as bps
import numpy as np

from ophyd import (ProsilicaDetector, SingleTrigger, Component as Cpt, Device,
                   EpicsSignal, EpicsSignalRO, ImagePlugin, StatsPlugin, ROIPlugin,
                   DeviceStatus)


db_archiver = Broker.named('iss-archiver')
arch_iss  = db_archiver.event_sources_by_name['arch_iss']



if bluesky.__version__ < LooseVersion('1.6'):
    OLD_BLUESKY = True
else:
    OLD_BLUESKY = False


###############################################################################
# TODO: remove this block once https://github.com/bluesky/ophyd/pull/959 is
# merged/released.
from ophyd.signal import EpicsSignalBase, EpicsSignal, DEFAULT_CONNECTION_TIMEOUT

def wait_for_connection_base(self, timeout=DEFAULT_CONNECTION_TIMEOUT):
    '''Wait for the underlying signals to initialize or connect'''
    if timeout is DEFAULT_CONNECTION_TIMEOUT:
        timeout = self.connection_timeout
    # print(f'{print_now()}: waiting for {self.name} to connect within {timeout:.4f} s...')
    start = time.time()
    try:
        self._ensure_connected(self._read_pv, timeout=timeout)
        # print(f'{print_now()}: waited for {self.name} to connect for {time.time() - start:.4f} s.')
    except TimeoutError:
        if self._destroyed:
            raise DestroyedError('Signal has been destroyed')
        raise

def wait_for_connection(self, timeout=DEFAULT_CONNECTION_TIMEOUT):
    '''Wait for the underlying signals to initialize or connect'''
    if timeout is DEFAULT_CONNECTION_TIMEOUT:
        timeout = self.connection_timeout
    # print(f'{print_now()}: waiting for {self.name} to connect within {timeout:.4f} s...')
    start = time.time()
    self._ensure_connected(self._read_pv, self._write_pv, timeout=timeout)
    # print(f'{print_now()}: waited for {self.name} to connect for {time.time() - start:.4f} s.')

EpicsSignalBase.wait_for_connection = wait_for_connection_base
EpicsSignal.wait_for_connection = wait_for_connection
###############################################################################

from ophyd.signal import EpicsSignalBase
if not OLD_BLUESKY:
    EpicsSignalBase.set_defaults(timeout=10, connection_timeout=10)







from bluesky import RunEngine

from bluesky.utils import get_history
RE = RunEngine({})


# from bluesky.utils import ts_msg_hook
#
# RE.msg_hook = ts_msg_hook


# temp1 = EpicsSignal('XF:08IDB-CT{ES-TC}T2-I', name='temp1')




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