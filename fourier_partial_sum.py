import numpy as np


def square_wave_partial_sum(t, num_terms, period=1.0):
    """Return the Nth partial sum of the square wave Fourier series."""
    if num_terms <= 0:
        raise ValueError("num_terms must be positive")

    total = np.zeros_like(t)
    for k in range(1, num_terms + 1, 2):
        total += (4 / np.pi) * (1 / k) * np.sin(2 * np.pi * k * t / period)

    return total


t = np.linspace(-1.0, 1.0, 5)
print(square_wave_partial_sum(t, num_terms=9))
