import matplotlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import duckdb

if __name__ == "__main__":
    # Some settings
    matplotlib.use('TkAgg')

    # Load data
    df = pd.read_feather('./data/working/3_Cleaned_df.output.feather')
    series_df = pd.read_feather('./data/working/3_Series_df.output.feather')

    join_query = """
    SELECT
        df.title,
        df.release_year,
        df.total_sales,
        series_df.title AS Series
    FROM series_df
    INNER JOIN df
    ON df.title LIKE series_df.title || '%'
    """
    series_sales = duckdb.query(join_query).df()

    # We have a lot of different Series: 349
    len(set(series_sales.Series))

    # Check the Top 20 most saled series over time
    top10_query = """
    SELECT Series
    FROM series_sales
    GROUP BY Series
    ORDER BY SUM(total_sales) DESC
    LIMIT 10
    """
    top10_series = duckdb.query(top10_query)

    filtering_query = """
    SELECT *
    FROM top10_series
    INNER JOIN series_sales
    USING (Series)
    """
    top10_series_sales = duckdb.query(filtering_query)

    grouping_query = """
    SELECT Series, release_year, SUM(total_sales) AS sales_by_years
    FROM top10_series_sales
    GROUP BY Series, release_year
    ORDER BY Series, release_year
    """
    top10_series_sales_by_years = duckdb.query(grouping_query).df()

    # Plot evolution of total sales by year for each series
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=top10_series_sales_by_years, x='release_year', y='sales_by_years', hue='Series', marker='o')

    # Customize the plot
    plt.title('Evolution of Total Sales by Year for Each Series')
    plt.xlabel('Release Year')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.legend(title='Series', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # Show the plot
    plt.savefig("./fig/16_Top10_TotalSales_by_year_by_series")

    # Not very informative, we will check the cumulatives sales over time !
    top10_series_sales_by_years['cumulative_sales'] = (
        top10_series_sales_by_years
        .groupby('Series')['sales_by_years']
        .cumsum()
    )
    # Plot evolution of cumulative sales by year for each series
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=top10_series_sales_by_years, x='release_year', y='cumulative_sales', hue='Series', marker='o')

    # Customize the plot
    plt.title('Evolution of Cumulatives Sales by Year for Each Series')
    plt.xlabel('Release Year')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.legend(title='Series', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # Show the plot
    plt.savefig("./fig/16_Top10_CumulativeSales_by_year_by_series")

    # We can see now that Call of Duty is clearly the most selled series over years !
