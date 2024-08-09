import pandas as pd
import duckdb
import plotnine as pn

if __name__ == "__main__":
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

    # Check the Top 10 most saled series over time
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

    # # Plot evolution of total sales by year for each series
    (pn.ggplot(top10_series_sales_by_years, pn.aes(x='release_year', y='sales_by_years', color='Series'))
     + pn.geom_line()
     + pn.geom_point()
     + pn.labs(title='Evolution of Total Sales by Year for Each Series',
               x='Release Year',
               y='Total Sales')
     + pn.theme_minimal()
     + pn.theme(figure_size=(14, 8),
                legend_position='right',
                legend_title=pn.element_text(size=10),
                legend_box_margin=0.1,
                panel_grid_major=pn.element_line(color='gray', linetype='dashed'),
                panel_grid_minor=pn.element_line(color='lightgray', linetype='dotted'),
                panel_background=pn.element_rect(color='white'))
     + pn.guides(color=pn.guide_legend(title='Series'))
     ).save("./fig/16_Top10_TotalSales_by_year_by_series.png")

    # Not very informative, we will check the cumulatives sales over time !
    top10_series_sales_by_years['cumulative_sales'] = (
        top10_series_sales_by_years
        .groupby('Series')['sales_by_years']
        .cumsum()
    )
    (pn.ggplot(top10_series_sales_by_years, pn.aes(x='release_year', y='cumulative_sales', color='Series'))
     + pn.geom_line()
     + pn.geom_point()
     + pn.labs(title='Evolution of Cumulatives Sales for Each Series',
               x='Release Year',
               y='Total Sales')
     + pn.theme_minimal()
     + pn.theme(figure_size=(14, 8),
                legend_position='right',
                legend_title=pn.element_text(size=10),
                legend_box_margin=0.1,
                panel_grid_major=pn.element_line(color='gray', linetype='dashed'),
                panel_grid_minor=pn.element_line(color='lightgray', linetype='dotted'),
                panel_background=pn.element_rect(color='white'))
     + pn.guides(color=pn.guide_legend(title='Series'))
     ).save("./fig/16_Top10_CumulativeSales_by_year_by_series.png")

    # We can see now that Call of Duty is clearly the most selled series over years !
    # This approach could be very informative for another kind of metrics likes Console:

    top10_query = """
    SELECT console
    FROM df
    GROUP BY console
    ORDER BY SUM(total_sales) DESC
    LIMIT 10
    """
    top10_console = duckdb.query(top10_query)

    filtering_query = """
    SELECT *
    FROM top10_console
    INNER JOIN df
    USING (console)
    """
    top10_console_sales = duckdb.query(filtering_query)

    grouping_query = """
    SELECT console, release_year, SUM(total_sales) AS sales_by_years
    FROM top10_console_sales
    GROUP BY console, release_year
    ORDER BY console, release_year
    """
    top10_console_sales_by_years = duckdb.query(grouping_query).df()

    # # Plot evolution of total sales by year for each series
    (pn.ggplot(top10_console_sales_by_years, pn.aes(x='release_year', y='sales_by_years', color='console'))
     + pn.geom_line()
     + pn.geom_point()
     + pn.labs(title='Evolution of Total Sales by Year for Each Console',
               x='Release Year',
               y='Total Sales')
     + pn.theme_minimal()
     + pn.theme(figure_size=(14, 8),
                legend_position='right',
                legend_title=pn.element_text(size=10),
                legend_box_margin=0.1,
                panel_grid_major=pn.element_line(color='gray', linetype='dashed'),
                panel_grid_minor=pn.element_line(color='lightgray', linetype='dotted'),
                panel_background=pn.element_rect(color='white'))
     + pn.guides(color=pn.guide_legend(title='Console'))
     ).save("./fig/17_Top10_TotalSales_by_year_by_console.png")

    # Not very informative, we will check the cumulatives sales over time !
    top10_console_sales_by_years['cumulative_sales'] = (
        top10_console_sales_by_years
        .groupby('console')['sales_by_years']
        .cumsum()
    )
    (pn.ggplot(top10_console_sales_by_years, pn.aes(x='release_year', y='cumulative_sales', color='console'))
     + pn.geom_line()
     + pn.geom_point()
     + pn.labs(title='Evolution of Cumulatives Sales for Each Series',
               x='Release Year',
               y='Total Sales')
     + pn.theme_minimal()
     + pn.theme(figure_size=(14, 8),
                legend_position='right',
                legend_title=pn.element_text(size=10),
                legend_box_margin=0.1,
                panel_grid_major=pn.element_line(color='gray', linetype='dashed'),
                panel_grid_minor=pn.element_line(color='lightgray', linetype='dotted'),
                panel_background=pn.element_rect(color='white'))
     + pn.guides(color=pn.guide_legend(title='Console'))
     ).save("./fig/17_Top10_CumulativeSales_by_year_by_console.png")
