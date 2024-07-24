import matplotlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from itertools import combinations
from scipy.stats import pearsonr


def correlation_pvals(data: pd.DataFrame):
    cols, n = data.columns, len(data.columns)

    corr_matrix = pd.DataFrame(np.zeros((n, n)), columns=cols, index=cols)
    pvals_matrix = pd.DataFrame(np.zeros((n, n)), columns=cols, index=cols)

    np.fill_diagonal(corr_matrix.values, 1.0)
    np.fill_diagonal(pvals_matrix.values, 0.0)

    for (col1, col2) in combinations(cols, 2):
        stat_corr, stat_pvals = pearsonr(data.dropna()[col1].values, data.dropna()[col2].values)
        corr_matrix.loc[col1, col2] = corr_matrix.loc[col2, col1] = stat_corr
        pvals_matrix.loc[col1, col2] = pvals_matrix.loc[col2, col1] = stat_pvals

    return corr_matrix, pvals_matrix


def clustermap_signif(corr_matrix: pd.DataFrame, pvals_matrix: pd.DataFrame, signif: float = 0.05,
                      dendrogram_ratio: float() = (0.1, 0.2), min_corr: float = None):
    try:
        assert corr_matrix.shape == pvals_matrix.shape, "Corr and Pvals need to have the same shape!"
    except AssertionError as e:
        print(f"Error: {e}")
        return

    mask = pvals_matrix > signif
    corr_signif = corr_matrix.mask(mask)

    if min_corr is not None:
        corr_mask = abs(corr_matrix) <= min_corr
        corr_signif = corr_signif.mask(corr_mask)

    annot = corr_signif.map(lambda x: f'{x:.2f}' if pd.notnull(x) else '')
    grid = sns.clustermap(
        figsize=(8, 8),
        data=corr_matrix,
        cmap="Spectral_r",
        annot=annot,
        fmt='',
        dendrogram_ratio=dendrogram_ratio,
        linewidths=0.5,
        cbar_pos=None,
        yticklabels=True,
        xticklabels=True
    )

    grid.ax_row_dendrogram.set_visible(False)
    grid.ax_col_dendrogram.set_visible(False)
    grid.ax_heatmap.set_position([0.025, 0.2, 0.8, 0.79])

    plt.setp(grid.ax_heatmap.get_xticklabels(), rotation=90)
    plt.setp(grid.ax_heatmap.get_yticklabels(), rotation=0)
    return grid


def clustermap_var_by_var(data: pd.DataFrame, var1: str, var2: str, top: int = None, min_corr: float = None):
    print(f"Starting study between {var1} and {var2}:")
    sub_df = data[[var1, var2]]
    if top is not None:
        top_var1 = data.groupby(var1)['total_sales'].sum().nlargest(top).index
        top_var2 = data.groupby(var2)['total_sales'].sum().nlargest(top).index
        sub_df = sub_df[sub_df[var1].isin(top_var1) & sub_df[var2].isin(top_var2)]
    sub_df = pd.get_dummies(sub_df.dropna(), dtype=float)
    print(f"    1. New shape is {sub_df.shape} after OneHot encoding")
    corr_matrix, pvals_matrix = correlation_pvals(sub_df)
    print(f"    2. Correlation done!")
    filtered_corr = corr_matrix[corr_matrix.index.str.startswith(var1)]
    filtered_corr = filtered_corr.loc[:, filtered_corr.columns.str.startswith(var2)]
    filtered_pvals = pvals_matrix.loc[filtered_corr.index, filtered_corr.columns]
    print(f"    3. Filtering done!")
    grid = clustermap_signif(filtered_corr, filtered_pvals, dendrogram_ratio=(0.0, 0.2), min_corr=min_corr)
    print(f"    4. Map generated")
    return grid


def crosstab_var_by_var(data: pd.DataFrame, var1: str, var2: str, top: int = None, z_score: int = None):
    sub_df = data[[var1, var2]]
    if top is not None:
        top_var1 = data.groupby(var1)['total_sales'].sum().nlargest(top).index
        top_var2 = data.groupby(var2)['total_sales'].sum().nlargest(top).index
        sub_df = sub_df[sub_df[var1].isin(top_var1) & sub_df[var2].isin(top_var2)]
    sub_ct = pd.crosstab(sub_df[var1], sub_df[var2])
    cluster_grid = sns.clustermap(sub_ct, cmap="Spectral_r", method="complete", dendrogram_ratio=(0, 0), linewidth=.1,
                                  cbar_pos=None, yticklabels=True, xticklabels=True, z_score=z_score)
    return cluster_grid


if __name__ == "__main__":
    # Some settings
    matplotlib.use('TkAgg')

    # Load data
    df = pd.read_feather('./data/working/3_Cleaned_df.output.feather')

    # Correlation analysis is only possible with numerical data, lets give a look :
    num_df = df.select_dtypes('float64')
    corr, pvals = correlation_pvals(num_df)
    clustermap_signif(corr, pvals, signif=1)
    plt.savefig("./fig/11_Numerical_corrmap.png")
    clustermap_signif(corr, pvals, signif=0.05)
    plt.savefig("./fig/11_Numerical_corrmap_signif.png")

    # To be able to run a correlation analysis, we need to transform our categories into numerical values.
    # We will try two approaches: label encoding and one-hot encoding.

    # 1. Label encoding:
    le_df = df.copy()
    for col in le_df.columns:
        if le_df[col].dtype != "float64":
            le_df[col], _ = pd.factorize(le_df[col])

    # Generate and save a cluster map of the correlation matrix of label-encoded data
    corr_le, pvals_le = correlation_pvals(le_df)
    clustermap_signif(corr_le, pvals_le)
    plt.savefig("./fig/12_LabelEncoded_corrmap_signif.png")

    # 2. One-hot encoding:
    # One-hot encoding splits a categorical variable of N categories into N binary (0 or 1) variables.
    # We will select some columns before to avoid creating an overly large plot. It will be more accurate
    # to study correlations between categories such as genre and console or publisher and developer.
    clustermap_var_by_var(data=df, var1='console', var2='genre')
    plt.savefig("./fig/13_Console_Genre_clustmap.png")
    clustermap_var_by_var(data=df, var1='developer', var2='publisher', top=50, min_corr=0.1)
    plt.savefig("./fig/13_Developer_Publisher_clustmap_top50.png")
    clustermap_var_by_var(data=df, var1='developer', var2='genre', top=50, min_corr=0.1)
    plt.savefig("./fig/13_Developer_Genre_clustmap_top50.png")
    clustermap_var_by_var(data=df, var1='publisher', var2='genre', top=50, min_corr=0.1)
    plt.savefig("./fig/13_Publisher_Genre_clustmap_top50.png")

    # 3. Crosstab
    # Another approach to check the relationship between two categorical variables is to use the crosstab() function.
    # It counts the frequencies of pairs between two variables.
    crosstab_var_by_var(data=df, var1='console', var2='genre')
    plt.savefig("./fig/14_Console_Genre_crossmap.png")
    crosstab_var_by_var(data=df, var1='developer', var2='publisher', top=50)
    plt.savefig("./fig/14_Developer_Publisher_crossmap_top50.png")
    crosstab_var_by_var(data=df, var1='developer', var2='genre', top=50)
    plt.savefig("./fig/14_Developer_Genre_crossmap_top50.png")
    crosstab_var_by_var(data=df, var1='publisher', var2='genre', top=50)
    plt.savefig("./fig/14_Publisher_Genre_crossmap_top50.png")

    # Finally, while crosstab visualization is great, it can be biased by high count values. To compare each genre
    # represented in each console/developer, we can use the Z-score transformation. This centers and scales the data
    # for each row or column to express the results in terms of standard deviation units above or below the mean.
    crosstab_var_by_var(data=df, var1='console', var2='genre', z_score=0)
    plt.savefig("./fig/15_ZSCORE_Console_Genre_crossmap.png")
    crosstab_var_by_var(data=df, var1='developer', var2='publisher', top=50, z_score=0)
    plt.savefig("./fig/15_ZSCORE_Developer_Publisher_crossmap_top50.png")
    crosstab_var_by_var(data=df, var1='developer', var2='genre', top=50, z_score=0)
    plt.savefig("./fig/15_ZSCORE_Developer_Genre_crossmap_top50.png")
    crosstab_var_by_var(data=df, var1='publisher', var2='genre', top=50, z_score=0)
    plt.savefig("./fig/15_ZSCORE_Publisher_Genre_crossmap_top50.png")
