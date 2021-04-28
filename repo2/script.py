#!/usr/bin/env python

# Load packages.
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Plot time series.
data = np.cumsum(np.random.randn(52 * 5 * 30))
plt.plot(data, color="black")
plt.xlabel("Time")
plt.ylabel("Return")
plt.title("Asset Evolution")
plt.grid()

# Moving average. 
ma1 = pd.Series(data=data).rolling(window=5 * 52).mean().values
ma2 = pd.Series(data=data).rolling(window=2 * 52).mean().values
ma3 = pd.Series(data=data).rolling(window=1 * 52).mean().values
plt.plot(ma1, color="red", ls="--", label="MA 1")
plt.plot(ma2, color="green", ls="--", label="MA 2")
plt.plot(ma3, color="blue", ls="--", label="MA 3")
plt.legend()

# Show final figure.
plt.show()