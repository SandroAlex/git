#!/usr/bin/env python

# Load packages.
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Plot time series.
data = np.cumsum(np.random.randn(52 * 5 * 30))
plt.plot(data)
plt.xlabel("Time")
plt.ylabel("Return")
plt.title("Asset Evolution")
plt.grid()

# Moving average. 
ma = pd.Series(data=data).rolling(window=5 * 52).mean().values
plt.plot(ma, color="green")

# Show final figure.
plt.show()