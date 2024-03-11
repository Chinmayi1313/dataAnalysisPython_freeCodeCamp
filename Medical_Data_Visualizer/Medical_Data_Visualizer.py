#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')


# In[3]:


df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)


# In[4]:


df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# In[5]:


df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'alco', 'active', 'smoke'])


# In[6]:


g = sns.catplot(x='variable', hue='value', col='cardio', kind='count', data=df_cat)
g.set_axis_labels('Variables', 'Total')
g.set_titles('{col_name} value counts for Cardio {col_var}')
plt.show()


# In[7]:


df = df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]


# In[8]:


corr_matrix = df.corr()


# In[9]:


mask = np.triu(np.ones_like(corr_matrix, dtype=bool))


# In[11]:


plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt=".2f", cmap='rocket_r', vmax=0.3, center=0, square=True, linewidths=.5)

