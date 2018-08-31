import os

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from . import PLOTCONFIG
from . import _path_utils

def plot():
    raise NotImplementedError

def s_plot():
    raise NotImplementedError

def categorical_hist_plot(df, colname: str, title: str=None, savename: str=None, ylim: tuple=None) -> None:
    """
    arguments

        df : pandas dataframe

        colname : str
            A column name of df which will be plotted.

        title : str


    Ex.
        In [1]: import pandas as pd
           ...: from dsutils import plot
           ...:
           ...: # bar plot
           ...: df = pd.DataFrame({"a": ["A", "B", "C", "A", "A"]})
           ...:

        In [2]: df
        Out[2]:
           a
        0  A
        1  B
        2  C
        3  A
        4  A

        In [3]: colname = "a"
           ...: plot.bar.categorical_hist_plot(df=df, colname=colname)

        In [4]: savename = "./output/bar_example.png"
           ...: plot.bar.categorical_hist_plot(df=df, colname=colname, savename=savename)
    """

    if savename is not None:
        _path_utils._make_savedir_from_savename(savename)

    plot_col = df[colname].dropna().values # 

    classnames, indices = np.unique(plot_col, return_inverse=True)
    hist, _ = np.histogram(indices, density=False, bins=len(classnames))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    if ylim is not None:
        ax.set_ylim(ylim)

    ax = sns.barplot(x=classnames, y=hist, ax=ax)

    if title is not None:
        ax.set_title(title)

    if savename is None:
        fig.show()
    else:
        fig.savefig(savename)
        plt.close(fig)

def bar_plot_categorical_columns(df, colnames: list, savepath: str=None, title_suffix: str=None, ylim_dict: dict=None) -> None:
    """
        arguments
            df : pandas dataframe
                Ex.
                    In [3]: df
                    Out[3]:
                       a  b  c
                    0  1  M  0
                    1  1  F  0
                    2  2  M  0
                    3  2  F  0
                    4  2  F  0
                    5  3  F  1

            colnames : list
                colnames should be a subset of df columns name.
                Ex.
                    In [6]: df.columns
                    Out[6]: Index(['a', 'b', 'c'], dtype='object')

                    In [7]: colnames = ["a", "b"]

            savepath : str
                Ex. savepath = "./output"

            title_suffix : str
                The figure title will be {colname}_{title_suffix}.
                Ex. title_suffix = "2018data"

            ylim_dict : dict of tuple
                A key is an element of colnames.
                A value is a tuple of ylim.
                Ex.
                    ylim_dict = {}
                    ylim_dict["a"] = (0, 100)

    Ex.
        In [1]: import pandas as pd
           ...: from dsutils import plot

        In [2]: df = pd.DataFrame({"a": [1,1,2,2,2,3], "b": ["M","F","M","F","F","F"], "c": [0,0,0,0,0,1]})
           ...: colnames = ["a", "b"]
           ...: plot.bar.bar_plot_categorical_columns(df, colnames=colnames)
    """
    if savepath is None:
        savepath = PLOTCONFIG.savepath

    os.makedirs(savepath, exist_ok=True)

    for colname in colnames:
        if not colname in df.columns:
            continue

        savename = os.path.join(savepath, colname)

        if title_suffix is None:
            title = colname
        else:
            title = colname + "_" + title_suffix

        if ylim_dict is not None:
            if colname in list(ylim_dict.keys()):
                ylim = ylim_dict[colname]
        else:
            ylim = None

        categorical_hist_plot(df=df, colname=colname, title=title, savename=savename, ylim=ylim)


def plot_columns_stacked_bar(df, stack_columns: list, summarize_by: str="median",\
                                x_column: str=None, add_all_bar: bool=False,\
                                x_label: str=None, y_label: str=None,\
                                title: str=None, savename: str=None, ylim: str=None):
    """
    It will stack representative values for columns (given by stack_columns).
        Ex.
            import pandas as pd
            from dsutils import plot

            df = pd.DataFrame({"class": [1,1,1,0,0,0], "values1": [2,3,4,20,21,22], "values2": [10,13,14,5,6,7]})
            stack_columns = ["values1", "values2"]
            x_column = "class"
            plot.bar.plot_columns_stacked_bar(df, stack_columns)
            plot.bar.plot_columns_stacked_bar(df, stack_columns, x_column=x_column)

    You can change order of stacking by changing order of stack_columns like below.
        # stack_columns = ["values1", "values2"]
        stack_columns = ["values2", "values1"]

    """
    df_stacked_bar = _make_stacked_bar_plot_df(df=df, stack_columns=stack_columns,\
                                                 x_column=x_column, add_all_bar=add_all_bar,\
                                                 summarize_by=summarize_by)

    plot_stacked_bar(df_stacked_bar, x_label, y_label, title, savename, ylim)

def plot_stacked_bar(df_stacked_bar, x_label: str=None, y_label: str=None, title: str=None, savename: str=None, ylim: tuple=None):
    """
    arguments
        df_stacked_bar : pandas dataframe
            stacked by columns.
            index is x axis.
                Ex.
                    In [28]: df_stacked_bar
                    Out[28]:
                         values1  values2
                    0       21.0      6.0
                    1        3.0     13.0
                    all     12.0      8.5

                    In this case, It shows 3 bar (0, 1, all) stacked by columns (values1, values2).

        savename : str
            savename = "./output/figure.png"
            If savename is given, it saves figure without showing up.

        ylim : tuple of float or int
            Ex. ylim = (0, 100)
    """
    df_stacked_bar_cumsum = np.cumsum(df_stacked_bar, axis=1).values
    n_row, n_col = df_stacked_bar_cumsum.shape
    plot_x = np.arange(n_row)
    bottom_matrix = np.c_[np.tile(0, n_row)[:, np.newaxis], df_stacked_bar_cumsum][:, 0:n_col]

    max_val = df_stacked_bar_cumsum.max()
    y_max = max_val + max_val / 10.

    fig = plt.figure()
    ax = fig.add_subplot(111)

    if ylim is None:
        ylim = (0, y_max)

    ax.set_ylim(ylim)

    for i, col_name in enumerate(df_stacked_bar.columns):
        ax.bar(plot_x, df_stacked_bar[col_name].values, width=0.5, align='center', label=col_name, bottom=bottom_matrix[:, i])

    ax.legend()

    if x_label is not None:
        ax.set_xlabel(x_label)
    if y_label is not None:
        ax.set_ylabel(y_label)

    ax.set_xticks(plot_x)
    ax.set_xticklabels(df_stacked_bar.index.astype(str))

    if title is not None:
        ax.set_title(title)

    if savename is None:
        fig.show()
    else:
        fig.savefig(savename)
        plt.close(fig)


def _make_stacked_bar_plot_df(df, stack_columns: list, x_column: str=None, add_all_bar: bool=False, summarize_by: str="median"):
    """
    This function caluculate a representative value of stack_columns, then arrange it to dataframe for plotting stacked bar.

        arguments
            df : pandas dataframe
            stack_columns : list of str
            add_all_bar : bool
            summarize_by : ["median"|"mean"]

    Ex.
        import pandas as pd
        df = pd.DataFrame({"class": [1,1,1,0,0,0], "values1": [2,3,4,20,21,22], "values2": [10,13,14,5,6,7]})
        stack_columns = ["values1", "values2"]
        x_column = "class"
        df_stacked_bar = _make_stacked_bar_plot_df(df, stack_columns, x_column, add_all_bar=True)

        In [28]: df_stacked_bar
        Out[28]:
             values1  values2
        0       21.0      6.0
        1        3.0     13.0
        all     12.0      8.5
        pandas.core.frame.DataFrame

        In [34]: df_stacked_bar = _make_stacked_bar_plot_df(df, stack_columns, add_all_bar=False)
        In [35]: df_stacked_bar
        Out[35]:
        values1    12.0
        values2     8.5
        Name: all, dtype: float64
        pandas.core.series.Series

        In [20]: df_stacked_bar = _make_stacked_bar_plot_df(df, stack_columns, x_column, add_all_bar=True, summarize_by="mean")

        In [21]:

        In [21]: df_stacked_bar
        Out[21]:
            values1  values2
        0        21        6
        1         3  12.3333
        all      12  9.16667
    """
    assert summarize_by in ("mean", "median"), "summarize_by input error"

    if x_column is not None:
        if not x_column in df.columns:
            raise ValueError(f"There is no {x_column} columns in df.")

    if summarize_by == "median":
        df_stacked_bar_all = df.loc[:, stack_columns].median()
    elif summarize_by == "mean":
        df_stacked_bar_all = df.loc[:, stack_columns].mean()

    df_stacked_bar_all = df_stacked_bar_all.rename("all")

    if x_column is None:
        if isinstance(df_stacked_bar_all, pd.Series):
            df_stacked_bar_all = pd.DataFrame(df_stacked_bar_all).T

        return df_stacked_bar_all
    else:
        subset_columns = [x_column] + stack_columns
        df_subset = df.loc[:, subset_columns]
        df_subset = df_subset.set_index(x_column)

        x_column_unique = np.sort(df_subset.index.unique())

        df_stacked_bar = pd.DataFrame([], columns=df_subset.columns, index=x_column_unique)
        for x_val in x_column_unique:
            if summarize_by == "median":
                df_stacked_bar.loc[x_val, :] = df_subset.loc[x_val, :].median()
            elif summarize_by == "mean":
                df_stacked_bar.loc[x_val, :] = df_subset.loc[x_val, :].mean()
        if add_all_bar:
            df_stacked_bar = df_stacked_bar.append(df_stacked_bar_all)

        if isinstance(df_stacked_bar, pd.Series):
            df_stacked_bar = pd.DataFrame(df_stacked_bar).T

        return df_stacked_bar

if __name__ == "__main__":
    pass