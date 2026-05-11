# Build a structured NumPy array to store 10 radar signal samples,
# each with amp (float32, 0-100), freq (float32, 0-1000) and
# ch (ubyte, 0-255). Use a seeded generator.
# Print all amplitudes, the third sample, and samples where
# channel exceeds 50.

import numpy as np

rng = np.random.default_rng(42)

signal = np.dtype([("amp", np.float32), ("freq", np.float32), ("ch", np.ubyte)])

amp = (rng.random(10) * 100).astype(
    np.float32
)  # float32 saves memory over float64 on large data
freq = (rng.random(10) * 1000).astype(
    np.float32
)  # float32 saves memory over float64 on large data
ch = rng.integers(0, 255, (10)).astype(
    np.ubyte
)  # ubyte uses 1 byte vs 8 bytes per value

arr = np.array(list(zip(amp, freq, ch)), dtype=signal)

# task 1 — all amplitudes
print(arr["amp"])

# task 2 — third sample
print(arr[2])

# task 3 — samples where ch > 50
print(arr[arr["ch"] > 50])
print(arr)