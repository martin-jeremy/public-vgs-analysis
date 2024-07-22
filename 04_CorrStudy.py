import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder


def cluster_var_by_var(data: pd.DataFrame, var1: str, var2: str, top: int() = None):
    sub_df = data[[var1, var2]]
    if top is not None:
        top_var1 = data.groupby(var1)['total_sales'].sum().nlargest(top).index
        top_var2 = data.groupby(var2)['total_sales'].sum().nlargest(top).index
        sub_df = sub_df[df[var1].isin(top_var1) & df[var2].isin(top_var2)]
    sub_df = pd.get_dummies(sub_df.dropna())
    print(f"New shape are {sub_df.shape}")
    # go = input("Are you sur that you want to continue? (Y/n)")
    # if go not in ['Yes', 'y', 'Oui', 'o', 'Y', 'O']:
    #     return None
    sub_df_corr = np.corrcoef(np.array(sub_df.T))
    sub_df_corr = pd.DataFrame(sub_df_corr)
    sub_df_corr.index, sub_df_corr.columns = sub_df.columns, sub_df.columns
    filtered_corr = sub_df_corr[sub_df_corr.index.str.startswith(var1)]
    filtered_corr = filtered_corr.iloc[:, filtered_corr.columns.str.startswith(var2)]
    cluster_grid = sns.clustermap(filtered_corr, cmap="Spectral_r", method="complete", dendrogram_ratio=(0, 0), linewidth=.1, cbar_pos=None)
    cluster_grid.ax_heatmap.get_xticklabels()
    return cluster_grid

if __name__ == "__main__":
    # Some settings
    matplotlib.use('TkAgg')

    # Load data
    df = pd.read_feather('./data/working/3_Cleaned_df.output.feather')

    # To be able to run a correlation analysis we need to transform our categories into numerical.
    # We will try two approaches: laben encoding and one hot encoding

    # 1. Label encoding:
    le = LabelEncoder()
    le_df = df.copy()
    for col in le_df.columns:
        if le_df[col].dtypes != "float64":
            le_df[col] = le.fit_transform(le_df[col])

    cor_mat = le_df.corr()
    sns.clustermap(cor_mat, cmap="Spectral_r", figsize=(6, 6), dendrogram_ratio=(.1, .2), method="complete", linewidth=.1)
    plt.savefig("./fig/12_LabelEncoded_clustmap.png")

    # 2. OneHot Encoding:
    # OneHot encoding consist into split a categorical variable of N categories into N variables encoded into 0 or 1.
    # We will select some column before to be able to keep a good tracking and not overblow the plot. It will be more
    # accurate to study correlation between genre and console or publisher and developer for example:
    cluster_var_by_var(data=df, var1='console', var2='genre')
    plt.savefig("./fig/13_Console_Genre_clustmap.png")
    cluster_var_by_var(data=df, var1='developer', var2='publisher', top=50)
    plt.savefig("./fig/13_Developer_Publisher_clustmap_top50.png")
    cluster_var_by_var(data=df, var1='developer', var2='genre', top=50)
    plt.savefig("./fig/13_Developer_Genre_clustmap_top50.png")
    cluster_var_by_var(data=df, var1='publisher', var2='genre', top=50)
    plt.savefig("./fig/13_Publisher_Genre_clustmap_top50.png")
