import os

from matplotlib import pyplot as plt
import seaborn as sns

from . import PLOTCONFIG

def plot(df, colname: str, title: str=None, savename: str=None, classes: str=None, xlabel: str=None,\
                     ylabel: str=None, ylim: tuple=None, kde: bool=False, norm_hist: bool=False,\
                     rug: bool=False, bins: int or list=None) -> None:
    """
    arguments
        df : pandas dataframe

        colname : str
            A colname in df whose histgram will be plotted.

        classes : str
            A column name in df to use separate color.
        bins : int or listlike
            Ex. bins = 30
                bins = np.linspace(0, 100, 10)
    """

    fig = plt.figure()
    ax = fig.add_subplot(111)

    if ylim is not None:
        ax.set_ylim(ylim)

    if classes is None:
        plot_col = df[colname].dropna().values
        ax = sns.distplot(plot_col, kde=kde, ax=ax, norm_hist=norm_hist, rug=rug, bins=bins)
    else:
        for clslabel in df[classes].unique():
            if not np.isnan(clslabel): # nan == nanは仕様でFalseになるのでisnanを用いている．
                plot_col = df[df[classes] == clslabel][colname]
            else:
                plot_col = df[df[classes].isnull()][colname]
            
            if not isinstance(clslabel, str):
                clslabel = str(clslabel)
            ax = sns.distplot(plot_col, kde=kde, label=clslabel, ax=ax, norm_hist=norm_hist, rug=rug, bins=bins)
            ax.legend()

    if title is not None:
        ax.set_title(title)

    if xlabel is not None:
        ax.set_xlabel(xlabel)

    if ylabel is not None:
        ax.set_ylabel(ylabel)

    if savename is None:
        fig.show()
    else:
        fig.savefig(savename)

    plt.close(fig)

def s_plot(df, colnames: list, savepath: str, title_suffix: str=None, ylabel: str=None, ylim_dict: dict=None, kde: bool=False,\
                                        norm_hist: bool=False, rug: bool=False) -> None:
    """
    arguments
        df : pandas dataframe

        colnames : list
            
        savepath : str
            Ex. savepath = "./output"

        title_suffix : str
            Ex. title_suffix = "2018data"
                It will be {colname}_{title_suffix}.

        ylabel : str
            Ex. ylabel = "Frequency"

        ylim_dict : dict
            Ex.
                ylim_dict = {}
                ylim_dict["col1"] = (0. 100)
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

        if isinstance(ylim_dict, dict):
            if colname in list(ylim_dict.keys()):
                ylim = ylim_dict[colname]
        else:
            ylim = None

        plot(df=df, colname=colname, ylabel=ylabel, title=title, savename=savename, ylim=ylim, kde=kde, norm_hist=norm_hist, rug=rug)

if __name__ == "__main__":
    pass