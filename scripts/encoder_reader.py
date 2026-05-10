#!/usr/bin/env python3
"""Quadrature rotary encoder reader for Raspberry Pi.

Phase A -> BCM GPIO 17
Phase B -> BCM GPIO 27
"""

from collections import deque
from datetime import datetime
from signal import pause
from time import monotonic

from gpiozero import RotaryEncoder

PIN_A = 17
PIN_B = 27
STEPS_PER_REV = 11  # set to your encoder's pulses-per-revolution (check datasheet)

total = 0
_last_time = monotonic()
_speed_history = deque(maxlen=20)


def on_rotate():
    global total, _last_time

    now = monotonic()
    dt = now - _last_time
    _last_time = now

    delta = encoder.steps
    encoder.steps = 0
    total += delta

    rpm = (delta / STEPS_PER_REV) / dt * 60
    _speed_history.append(rpm)
    avg_rpm = sum(_speed_history) / len(_speed_history)

    ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{ts}]  steps: {total:+d}  speed: {rpm:+.1f} RPM  avg(20): {avg_rpm:+.1f} RPM")


encoder = RotaryEncoder(PIN_A, PIN_B, max_steps=100)
encoder.when_rotated = on_rotate

print(f"Listening on GPIO {PIN_A} (A) and {PIN_B} (B). Press Ctrl+C to stop.")
pause()
