"""Validated ramp programs and a clock independent of EPICS."""

from bisect import bisect_right
from dataclasses import dataclass
from math import isfinite


class RampProgram:
    """Snapshot a program once; interpolate without per-tick array allocation."""

    def __init__(self, times, setpoints):
        self.times = tuple(float(t) for t in times)
        self.setpoints = tuple(float(p) for p in setpoints)
        if not 2 <= len(self.times) <= 25 or len(self.times) != len(self.setpoints):
            raise ValueError("A ramp requires 2–25 matching times and setpoints")
        if not all(isfinite(v) for v in (*self.times, *self.setpoints)):
            raise ValueError("Ramp values must be finite")
        if self.times[0] < 0 or any(
            b <= a for a, b in zip(self.times, self.times[1:])
        ):
            raise ValueError("Ramp times must be nonnegative and strictly increasing")

    def sample(self, elapsed):
        """Return setpoint and the original right-hand segment index."""
        step = bisect_right(self.times, elapsed)
        if step == 0:
            return self.setpoints[0], 0
        if step == len(self.times):
            return self.setpoints[-1], step - 1
        fraction = (elapsed - self.times[step - 1]) / (
            self.times[step] - self.times[step - 1]
        )
        value = self.setpoints[step - 1] + fraction * (
            self.setpoints[step] - self.setpoints[step - 1]
        )
        return value, step


@dataclass
class RampClock:
    elapsed: float = 0.0
    paused: float = 0.0
    previous: float | None = None
    was_paused: bool = False

    def update(self, now, running, paused):
        if not running:
            self.elapsed = self.paused = 0.0
            self.previous = None
            self.was_paused = False
            return
        if self.previous is not None:
            interval = max(0.0, now - self.previous)
            if self.was_paused:
                self.paused += interval
            else:
                self.elapsed += interval
        self.previous = now
        self.was_paused = bool(paused)
