#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')

plt.figure(figsize=(12, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Sea Level Data', color='blue')

slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

future_years = range(1880, 2051)
predicted_sea_level = slope * future_years + intercept
plt.plot(future_years, predicted_sea_level, label='Line of Best Fit (1880-2050)', color='green')

recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

predicted_sea_level_recent = slope_recent * future_years + intercept_recent
plt.plot(future_years, predicted_sea_level_recent, label='Line of Best Fit (2000-present)', color='red')

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

plt.savefig('sea_level_rise.png')
plt.legend()
plt.show()


