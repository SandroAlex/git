#!/usr/bin/env python

# Load packages.
import numpy as np
from matplotlib import pyplot as plt

# Plot time series.
plt.plot(np.cumsum(np.random.randn(10000)))
plt.xlabel("Time")
plt.ylabel("Return")
plt.title("Asset Evolution")
plt.grid()
plt.show()