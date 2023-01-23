import gc
import os

import matplotlib.pyplot as plt
import seaborn as sns

list_metric = [
    "braycurtis",
    "canberra",
    "chebyshev",
    "cityblock",
    "correlation",
    "cosine",
    "dice",
    "euclidean",
    "hamming",
    "jaccard",
    # "jensenshannon",
    # "kulczynski1",
    # "mahalanobis",
    "matching",
    "minkowski",
    "rogerstanimoto",
    "russellrao",
    "seuclidean",
    "sokalmichener",
    "sokalsneath",
    "sqeuclidean",
    "yule",
]

list_method = [
    "single",
    "complete",
    "average",
    "weighted",
    "centroid",
    "median",
    "ward",
]


def plot_clustermap(df, method, metric, ax=None):
    if ax is None:
        ax = plt.gca()

    g = sns.clustermap(
        df,
        cmap="coolwarm",
        method=method,
        metric=metric,
        figsize=(5, 5),
    )
    plt.clf()
    plt.close()
    gc.collect()

    col = g.dendrogram_col.reordered_ind
    row = g.dendrogram_row.reordered_ind
    sns.heatmap(
        df.iloc[row, col], cmap="coolwarm", ax=ax, square=True, cbar=False
    )


def plot_clustermap_all(df):
    fig, ax = plt.subplots(
        len(list_method), len(list_metric), figsize=(50, 20)
    )

    for i, method in enumerate(list_method):
        for j, metric in enumerate(list_metric):
            if (
                method in ["centroid", "median", "ward"]
                and metric != "euclidean"
            ):
                continue

            plot_clustermap(df, method, metric, ax[i, j])
            ax[i, j].set_title(f"method = {method}\nmetric = {metric}")
    fig.tight_layout()

    return fig


def save_clustermap_all(df, path):
    if os.path.exists(path):
        pass
    else:
        fig = plot_clustermap_all(df)
        fig.savefig(path)
