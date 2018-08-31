import os

from matplotlib import pyplot as plt
import seaborn as sns

from . import PLOTCONFIG

def plot(df, x_colname: str, y_colname: str, title: str=None, savename: str=None, ylim: tuple=None, hue: str=None, labels: list=None, alpha: float=None) -> None:
    """
        arguments
            df : pandas dataframe

            x_colname : str
                A column name of df which will be x axis.
            y_colname : str
                A column name of df which will be y axis.
            ylim : tuple of int
                ylim = (0, 2000)
            hue : str
                A column name of categorical column in df.
                It will use separate color for each hue element.
    """
    df_subset = df[df[y_colname].notnull().values]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    if labels is None:
        ax = sns.scatterplot(x=x_colname, y=y_colname, data=df_subset, ax=ax, hue=hue, alpha=alpha)
    else:
        # The reason why It does not use hue option of sns.scatterplot is to label each class
        # by different name from hue column values.
        # In case hue column has like {0, 10, 20}, I have to change {0, 1, 2} and label will be 0, 1, 2.
        hue_uniques = df_subset[hue].unique()
        hue_uniques.sort()
        if len(labels) != len(hue_uniques):
            raise ValueError("The hue unique elements num and labels num should be same value.")

        for i, hue_unique in enumerate(hue_uniques):
            df_plot = df_subset[df_subset[hue] == hue_unique]
            ax = sns.scatterplot(x=x_colname, y=y_colname, data=df_plot, ax=ax, label=labels[i], alpha=alpha)

    if labels is not None:
        ax.legend()

    if ylim is not None:
        ax.set_ylim(ylim)

    if title is not None:
        ax.set_title(title)

    if savename is None:
        fig.show()
    else:
        fig.savefig(savename)
        plt.close(fig)

if __name__ == "__main__":
    pass