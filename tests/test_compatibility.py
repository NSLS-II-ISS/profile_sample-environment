"""Offline contracts between the profile, GUI, and supported scientific stack."""

import ast
import inspect
from pathlib import Path

import pytest

from sample_environment.ramping import RampProgram


def test_profile_keywords_match_installed_gui():
    from iss_xsample.xsample import XsampleGui

    source = Path(__file__).resolve().parents[1] / "startup/99_run.py"
    tree = ast.parse(source.read_text())
    call = next(n for n in ast.walk(tree) if isinstance(n, ast.Call)
                and isinstance(n.func, ast.Attribute) and n.func.attr == "XsampleGui")
    keywords = {kw.arg: None for kw in call.keywords}
    inspect.signature(XsampleGui).bind(**keywords)


def test_ramp_snapshot_interpolates_without_mutating_inputs():
    times, values = [0, 10, 20], [20, 100, 50]
    program = RampProgram(times, values)
    values[1] = 999
    assert program.sample(5) == (60, 1)
    assert program.sample(15) == (75, 2)
    assert program.sample(30) == (50, 2)


@pytest.mark.parametrize("times,values", [([0, 0], [1, 2]), ([0, 1], [1, float('nan')])])
def test_invalid_ramp_is_rejected(times, values):
    with pytest.raises(ValueError):
        RampProgram(times, values)


def test_legacy_archiver_api_imports():
    from databroker.v0 import Broker

    assert hasattr(Broker, "named")
