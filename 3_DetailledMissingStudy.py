from locale import str

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def top_n_barplots(data: pd.DataFrame, category: str, n: int, save: bool):
    topn_games = data.groupby(category)['total_sales'].sum().nlargest(n)
    fig10, ax10 = plt.subplots(figsize=(5, 5))
    sns.barplot(x=topn_games.index, y=topn_games, ax=ax10)
    plt.xticks(rotation=90)
    plt.title(f"Top {n} Most Sold Games")
    ax10.set_xlabel(category.title())
    ax10.set_ylabel('Total Sales')
    plt.subplots_adjust(bottom=0.5)
    plt.savefig(f"./fig/9_Top10_by_{category}.png")


if __name__ == "__main__":
    # Some settings
    matplotlib.use('TkAgg')

    # Read the feather file into a DataFrame
    df = pd.read_feather('data/working/1_Structure.output.feather')

    # Today we will focus on missing value to try to remove the less informatives entries
    df.info()
    eda_df = pd.DataFrame()
    eda_df['NULL_before'] = df.isnull().sum()

    # We are missing a lot in the total_sales variables. Let give a look.
    sub_df = df[df['total_sales'].isnull()]
    sub_df.head()

    # WAOW! We see that most of them don't have any values and if we focus on the console look that !
    # I will keep a backup of the Series line
    Series_df = df[df['console'] == 'Series']
    Series_df.to_feather('./data/working/3_Series_df.output.feather')

    # Then I remove all the line that have a total_sales null (as they are less informatives for us)
    df = df[df['total_sales'].notna()]

    # Finally, we take the hypothesis that if last_update is null, it's because the game never had an update
    # (like the old good time)
    df['last_update'] = df['last_update'].fillna(df['release_date'])
    df.to_feather('./data/working/3_Cleaned_df.output.feather')

    # And I redo the same barplot as precedent to compare
    eda_df['NULL_after'] = df.isnull().sum()
    print(eda_df.T)

    fig8, ax8 = plt.subplots(figsize=(14, 4))
    sns.heatmap(eda_df.T, annot=True, square=True, fmt='', cmap="vlag")
    plt.subplots_adjust(right=0.99)
    plt.title("Number of NULL entries by variable before and after cleanup")

    # Save the figure to a file / display the plot
    plt.savefig('./fig/8_NULL_by_variable_before_vs_after_cleaning.png')

    # Let's study some top 5
    for top in ['title', 'console', 'genre', 'developer', 'publisher', 'release_year']:
        top_n_barplots(
            data=df,
            n=10,
            category=top,
            save=True
        )

    top10_games = df[['title', 'console', 'total_sales']].nlargest(10, columns='total_sales')
    top10_games.index = top10_games.title + ' - ' + top10_games.console
    fig11, ax11 = plt.subplots(figsize=(5.5, 5))
    sns.barplot(
        x=top10_games.index,
        y=top10_games.total_sales
    )
    plt.xticks(rotation=90)
    plt.title(f"Top 10 Most Sold Games")
    ax11.set_xlabel("Games")
    ax11.set_ylabel('Total Sales')
    plt.subplots_adjust(bottom=0.55)

    plt.savefig(f"./fig/10_Top10_by_game.png")
