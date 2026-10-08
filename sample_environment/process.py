"""Launch and stop only the ramping IOC owned by this session."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def start_ioc():
    return subprocess.Popen(
        [sys.executable, "-m", "iocs.ioc_ramping"], cwd=ROOT,
    )


def stop_ioc(process, timeout=5):
    if process is None or process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=timeout)
