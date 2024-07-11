import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import seaborn as sns

if __name__ == '__main__':
    # Some settings
    matplotlib.use('TkAgg')

    # Read the feather file into a DataFrame
    df = pd.read_feather('data/working/1_Structure.output.feather')

    # Select only the columns with numerical (float64) data types
    numeric_df = df.select_dtypes(include=['float64'])

    # Create subplots for the boxplots, with 2 rows and 4 columns
    fig3, ax3 = plt.subplots(nrows=3, ncols=3, figsize=(8, 8))
    ax3 = ax3.flatten()  # Flatten the 2D array of axes to make it easier to iterate
    # over. It avoids the use of nested loop.

    # Loop through each numeric column and create a boxplot
    for i, col in enumerate(numeric_df.columns):
        sns.boxplot(
            y=numeric_df[col],
            ax=ax3[i]
        )
        col_title = f"{col.split('_')[0].upper() + ' ' + col.split('_')[1].upper()}"
        ax3[i].set_title(col_title)
        ax3[i].set_ylabel('')

    # If there are more subplots than columns, remove the empty subplots
    for j in range(i + 1, len(ax3)):
        fig3.delaxes(ax3[j])

    # Adjust the layout to prevent overlapping subplots
    plt.tight_layout()

    # Save the figure to a file / display the plot
    plt.savefig('./fig/3_Boxplot_numeric_variables.png')
    plt.show()

    # Distribution of release_year variable
    fig4, ax4 = plt.subplots(figsize=(14, 8))
    sns.histplot(
        x=df['release_year'],
        ax=ax4,
        binwidth=1,
        color='steelblue',
        edgecolor='white'
    )
    plt.title('Evolution of Video Game Releases Over Time')
    ax4.set_xlabel('Release Years')

    # Save the figure to a file / display the plot
    plt.savefig('./fig/4_Distribution_release_over_time.png')
    plt.show()

    # Count of console variable
    fig5, ax5 = plt.subplots(figsize=(14, 8))
    sns.countplot(
        x=df['console'],
        ax=ax5,
        color='#c86f7f',
        edgecolor='white',
        order=df['console'].value_counts().sort_values(ascending=False).index
    )
    plt.yscale('log')
    plt.gca().yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: '{:,.0f}'.format(x))
    )
    plt.xticks(rotation=90)
    plt.title('Number of Video Game Releases by Support')
    ax5.set_xlabel('')
    ax5.set_ylabel('Counts (log scaled)')

    # Save the figure to a file / display the plot
    plt.savefig('./fig/5_Number_of_games_by_support.png')
    plt.show()

    # Sales by console (top15)
    top15_consoles = df.groupby('console')['total_sales'].sum().nlargest(15)
    pc_highlight_palette = np.where(
        top15_consoles.index == 'PC',
        '#c86f7f',
        'steelblue'
    )
    fig6, ax6 = plt.subplots(figsize=(12, 8))
    sns.barplot(
        y=top15_consoles,
        x=top15_consoles.index,
        palette=pc_highlight_palette,
        edgecolor='white'
    )
    plt.xticks(rotation=90)
    plt.title('Sales by console (Top 15)')
    ax6.set_xlabel('')
    ax6.set_ylabel('Total Sales')

    # Save the figure to a file / display the plot
    plt.savefig('./fig/6_Top15_Sales_by_support.png')
    plt.show()

    # Count of genre variable
    fig7, ax7 = plt.subplots(figsize=(12, 8))
    sns.countplot(
        x=df['genre'],
        ax=ax7,
        color='steelblue',
        edgecolor='white',
        order=df['genre'].value_counts().sort_values(ascending=False).index
    )
    plt.yscale('log')
    plt.gca().yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: '{:,.0f}'.format(x))
    )
    plt.xticks(rotation=90)
    plt.title('Number of Video Game Releases by Genre')
    ax7.set_xlabel('')
    ax7.set_ylabel('Counts (log scaled)')

    # Save the figure to a file / display the plot
    plt.savefig('./fig/7_Number_of_games_by_genre.png')
    plt.show()

    # Okay then, we have a lot of information yet. We can see that we have a lot of
    # missing values. It will be a bit problematic but not yet. We see that PC are
    # overrepresented in the dataset, and most games recorded where released in 2009.
    # We show also that even if PC are the support with the most released games, it's
    # only at the 12th position of sales by support.
