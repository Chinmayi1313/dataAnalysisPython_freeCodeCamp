#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

df_cleaned = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def draw_line_plot():
    plt.figure(figsize=(14, 6))
    plt.plot(df_cleaned.index, df_cleaned['value'], color='r', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.grid(True)
    plt.savefig('line_plot.png')
    plt.show()

def draw_bar_plot():
    df['Year'] = df.index.year
    df['Month'] = df.index.strftime('%B')

    df_pivot = df.pivot_table(values='value', index='Year', columns='Month', aggfunc='mean')
    df_pivot = df_pivot[months_order]

    ax = df_pivot.plot(kind='bar', figsize=(14, 8))
    plt.title('Average Daily Page Views for Each Month Grouped by Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', loc='upper left')
    plt.grid(True)
    plt.savefig('bar_plot.png')
    plt.show()

def draw_box_plot():
    df_box = df_cleaned.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box['date']]
    df_box['Month'] = [d.strftime('%B') for d in df_box['date']]

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))
    sns.boxplot(x='Year', y='value', data=df_box, ax=axes[0])
    sns.boxplot(x='Month', y='value', data=df_box, ax=axes[1], order=months_order)

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.savefig('box_plot.png')
    plt.show()

draw_line_plot()
draw_bar_plot()
draw_box_plot()


