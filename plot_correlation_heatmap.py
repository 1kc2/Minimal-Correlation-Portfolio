import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import distance_correlation as dc

def plot_correlation_heatmap():
    df = dc.distance_correlation().astype("float")

    cmap = sns.cubehelix_palette(3, as_cmap=True, reverse=True)
    sns.heatmap(df, xticklabels=df.columns, yticklabels=df.columns, cmap=cmap)
    plt.show()


if __name__ == "__main__":
    plot_correlation_heatmap()
