import os

from matplotlib import pyplot as plt
import seaborn as sns

from . import PLOTCONFIG

def plot(df, x_colname: str, y_colname: str, title: str=None, savename: str=None, ylim: tuple=None) -> None:
    """
        arguments
            df : pandas dataframe

            x_colname : str
                A column name in df which is categorical data.

            y_colname : str
                A column name in df which is continuous data.

            title : str

            ylim : tuple of int
                ylim = (0, 2000)
    """
    df_subset = df[df[y_colname].notnull().values]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax = sns.boxplot(x=x_colname, y=y_colname, data=df_subset, ax=ax)

    if ylim is not None:
        ax.set_ylim(ylim)

    if title is not None:
        ax.set_title(title)

    if savename is None:
        fig.show()
    else:
        fig.savefig(savename)
        plt.close(fig)

def s_plot(df, colnames, x_colname: str, savepath: str=None, title_suffix: str=None, ylim_dict: dict=None) -> None:
    """
        arguments
            df : pandas dataframe

            colnames : list
                column names in df which are continuous data.

            x_colname : str
                 A column name in df which is categorical data.

            savepath : str
            Ex. savepath = "./output"

            title_suffix : str
                Ex. title_suffix = "2018data"
                    It will be {colname}_{title_suffix}.

            ylim_dict : dict
                Ex.
                    ylim_dict = {}
                    ylim_dict["col1"] = (0. 100)
    """
    if savepath is None:
        savepath = PLOTCONFIG.savepath

    if isinstance(savepath, str):
        os.makedirs(savepath, exist_ok=True)

    for y_colname in colnames:
        if not y_colname in df.columns:
            continue

        if isinstance(ylim_dict, dict):
            if y_colname in list(ylim_dict.keys()):
                ylim = ylim_dict[y_colname]
        else:
            ylim = None

        if title_suffix is None:
            title = y_colname
        else:
            title = y_colname + "_" + title_suffix
        
        base_name = "x_" + x_colname + "_y_" + y_colname
        savename = os.path.join(savepath, base_name)
        plot(df=df, x_colname=x_colname, y_colname=y_colname, title=title, savename=savename, ylim=ylim)

if __name__ == "__main__":
    pass