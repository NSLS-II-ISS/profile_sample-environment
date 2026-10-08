"""Run the repository as an IPython profile, after checking site dependencies."""

import argparse
import importlib
import inspect

from .process import ROOT


def check_dependencies():
    """Check imports and configuration without constructing hardware devices."""
    from databroker.v0 import Broker

    for module in ("caproto", "ophyd", "bluesky", "PyQt5.QtWidgets"):
        importlib.import_module(module)
    try:
        from iss_xsample.xsample import XsampleGui
    except ImportError as exc:
        raise RuntimeError(
            "Install the site's iss-xsample and isstools checkouts in the beamline "
            "environment, or add their repository roots to PYTHONPATH. See README.md."
        ) from exc
    if "rga_channels" not in inspect.signature(XsampleGui.__init__).parameters:
        raise RuntimeError(
            "This xsample revision lacks RGA support. Use the site's RGA-capable checkout."
        )
    broker = Broker.named("iss-archiver")
    broker.event_sources_by_name["arch_iss"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check site prerequisites only")
    args, ipython_args = parser.parse_known_args()
    try:
        check_dependencies()
    except Exception as exc:
        parser.exit(1, f"Sample environment preflight failed: {exc}\n")
    if args.check:
        print("Site dependencies and iss-archiver configuration are available.")
        return
    from IPython import start_ipython

    start_ipython(argv=[f"--profile-dir={ROOT}", "--gui=qt5", *ipython_args])


if __name__ == "__main__":
    main()
