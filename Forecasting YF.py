import pandas as pd
import yfinance as yf
import math
import numpy as np
import matplotlib.pyplot as plt

df = yf.download("AAP", start="2025-01-01", end="2025-01-10")

print(df.head(), df)

plt.plot(df)
plt.title("Yahoo Finance Performance")
plt.ylabel("Performance")
plt.xlabel("Days")
plt.legend()
plt.fill()
plt.show()