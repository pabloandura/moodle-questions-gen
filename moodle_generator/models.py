# moodle_generator/models.py

import random

def calculate_half_wave(V_EF_SEC, RL, FR):
    """
    Calculate parameters for a half-wave rectifier.
    Return:
        Correct value (Voltage across RL) and plausible distractors.
    """
    # Example calculation: peak voltage
    Vm = V_EF_SEC * (2**0.5)  # Convert RMS to peak
    Vr = Vm * (FR / 100)  # Ripple voltage (example)
    VL = Vm - Vr  # Voltage across RL (example)

    # Generate plausible distractors
    distractors = [
        round(VL * random.uniform(0.9, 1.1), 2),
        round(VL * random.uniform(0.8, 1.2), 2),
    ]

    return round(VL, 2), distractors

def calculate_full_wave(V_EF_SEC, RL):
    """
    Calculate parameters for a full-wave rectifier.
    Return:
        Correct value (Voltage across RL) and plausible distractors.
    """
    # Example calculation: average voltage
    Vm = V_EF_SEC * (2**0.5)  # Convert RMS to peak
    VL = 0.9 * Vm  # Average output voltage (example)

    # Generate plausible distractors
    distractors = [
        round(VL * random.uniform(0.9, 1.1), 2),
        round(VL * random.uniform(0.8, 1.2), 2),
    ]

    return round(VL, 2), distractors
