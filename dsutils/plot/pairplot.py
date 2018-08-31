import os

import seaborn as sns
from matplotlib import pyplot as plt

# from . import PLOTCONFIG

def plot(df, colnames, classes: str=None, savename: str=None, replace_nan2zero: bool=False) -> None:
    """
    arguments
        df : pandas dataframe

        colnames : list
            colnames should be a subset of df columns name.
            Ex.
                In [6]: df.columns
                Out[6]: Index(['a', 'b', 'c'], dtype='object')

                In [7]: colnames = ["a", "b"]

        classes : str
            A column name in df to use separate color.

        savepath : str
            Ex. savepath = "./output/pairplot.png"

        show : bool
            If show is True, plot will show up without saving.

        replace_nan2zero : bool
            If this option is True, replace nan to 0.
            It is simplified way for dealing with a data containing too much nan.
            This option is in the idea that It is better than cannot get output.
    """

    if isinstance(savename, str):
        savepath = os.path.dirname(savename)
        os.makedirs(savepath, exist_ok=True)

    if isinstance(classes, str):
        colnames = colnames + [classes]
        colnames = [column for column in colnames if column in df.columns] # continuous_colnamesには入っているが，dfにはないものは削除する．

    df_subset = df[colnames]

    if replace_nan2zero:
        df_subset = df_subset.fillna(0)

    sns.pairplot(df_subset, hue=classes, palette=sns.color_palette("coolwarm", len(df[classes].unique())), diag_kind="hist", markers="+")

    if savename is None:
        plt.show()
    else:
        plt.savefig(savename)
        plt.close()

if __name__ == "__main__":
    pass