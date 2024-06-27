import os

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

# Some settings
matplotlib.use('TkAgg')

# Read the feather file into a DataFrame
df = pd.read_feather('data/working/1_Structure.output.feather')

# Select only the columns with numerical (float64) data types
numeric_df = df.select_dtypes(include=['float64'])

# Create subplots for the boxplots, with 2 rows and 4 columns
fig1, ax1 = plt.subplots(nrows=2, ncols=4, figsize=(16, 8))
ax1 = ax1.flatten()  # Flatten the 2D array of axes to make it easier to iterate over. It allows us to avoid use of nested loop.

# Loop through each numeric column and create a boxplot
for i, col in enumerate(numeric_df.columns):
    sns.boxplot(y=numeric_df[col], ax=ax1[i])
    ax1[i].set_title(f"{col.split('_')[0].upper() + ' ' + col.split('_')[1].upper()}")
    ax1[i].set_ylabel('')

# If there are more subplots than columns, remove the empty subplots
for j in range(i + 1, len(ax1)):
    fig1.delaxes(ax1[j])

# Adjust the layout to prevent overlapping subplots
plt.tight_layout()

# Save the figure to a file / display the plot
plt.savefig('./fig/3_Boxplot_numeric_variables.png')
plt.show()

# Distribution of release_year variable
fig2, ax2 = plt.subplots()
sns.histplot(x=df['release_year'], ax=ax2, binwidth=1, color='steelblue', edgecolor='white')
plt.title('Evolution of Video Game Releases Over Time')
ax2.set_xlabel('Release Years')

# Save the figure to a file / display the plot
plt.savefig('./fig/4_Distribution_release_over_time.png')
plt.show()

# Count of console variable
fig3, ax3 = plt.subplots(figsize=(12, 8))
sns.countplot(x=df['console'], ax=ax3, color='steelblue', edgecolor='white',
              order=df['console'].value_counts().sort_values(ascending=False).index)
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:,.0f}'.format(x)))
plt.xticks(rotation=90)
plt.title('Number of Video Game Releases by Support')
ax3.set_xlabel('')

# Save the figure to a file / display the plot
plt.savefig('./fig/5_Number_of_games_by_support.png')
plt.show()