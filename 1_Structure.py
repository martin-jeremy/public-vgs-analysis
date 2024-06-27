import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Make some dirs
os.makedirs(name='./data/working', exist_ok=True)
os.makedirs(name='./fig', exist_ok=True)

# Load df
df = pd.read_csv('./data/raw/vgchartz-2024.csv')

# Convert some variable
df['release_date'] = pd.to_datetime(df['release_date'])
df['last_update'] = pd.to_datetime(df['last_update'])

# Datetime could be informative, but they are not very easy to manipulate with, we will create a column keeping only release year
df['release_year'] = df['release_date'].dt.year.astype('float64')

# Get some information about our dataset
df.info()
df.describe()

# Keep an eye on variables
eda_df = pd.DataFrame()
eda_df['type'] = df.dtypes
eda_df['NULL'] = df.isnull().sum()
eda_df['NULL_PCT'] = round(df.isnull().sum() / len(df) * 100, 2)

# Plot the pie chart of variable types
fig1, ax1 = plt.subplots()
ax1.pie(eda_df['type'].value_counts(),
        labels=eda_df['type'].value_counts().index.tolist(),
        colors=['lightsteelblue', 'turquoise', 'thistle'],
        wedgeprops={'linewidth': 2, 'edgecolor': 'white'},
        autopct='%1.1f%%')
plt.title('Proportion of types in the dataset')
plt.savefig('./fig/1_PieChartVariable.png')
plt.show()

# Plot the heatmap of missing values
fig2, ax2 = plt.subplots(figsize=(10, 10))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='coolwarm', ax=ax2, vmax=.3, center=0)
plt.title('Missing Values Heatmap')
plt.savefig('./fig/2_MissingValuesHeatmap.png')
plt.show()

# The img column is useless for our analyse
df = df.drop(columns=['img'])

# Save work
df.to_feather('./data/working/1_Structure.output.feather')
