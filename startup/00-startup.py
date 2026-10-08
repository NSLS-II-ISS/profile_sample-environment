"""Shared IPython namespace and local IOC lifecycle."""

import os
import sys
import time as ttime
from datetime import datetime
from pathlib import Path

import bluesky.plan_stubs as bps
import numpy as np
from bluesky import RunEngine
from databroker.v0 import Broker
from ophyd import Component as Cpt, Device, EpicsSignal
from ophyd.signal import EpicsSignalBase

# Also support loading this directory as a conventional IPython profile.
_profile_root = Path(__file__).resolve().parents[1]
if str(_profile_root) not in sys.path:
    sys.path.insert(0, str(_profile_root))
from sample_environment.process import start_ioc, stop_ioc


def time_now_str():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


def print_to_gui(msg, tag='', add_timestamp=False, ntabs=0, stdout_alt=None):
    gui = globals().get('xlive_gui')
    stdout = getattr(gui, 'emitstream_out', None) or stdout_alt or sys.stdout
    msg = '\t' * ntabs + msg
    if add_timestamp:
        msg = f'({time_now_str()}) {msg}'
    if tag:
        msg = f'[{tag}] {msg}'
    print(msg, file=stdout, flush=True)


# Current Ophyd implements connection handling without the historical patch.
EpicsSignalBase.set_defaults(timeout=10, connection_timeout=10)
RE = RunEngine({})
db_archiver = Broker.named('iss-archiver')
arch_iss = db_archiver.event_sources_by_name['arch_iss']

# Set to 0 when an independently managed ramping IOC is already running.
ioc_process = start_ioc() if os.environ.get('SAMPLE_ENV_START_IOC', '1') == '1' else None


def kill_pid_ioc():
    stop_ioc(ioc_process)
