import os

import matplotlib.pyplot as plt
import seaborn as sns

pallet = "deep"
color_num = 24
COLORPALLET = sns.color_palette(pallet, color_num)

def plot(labels, sizes, df=None, title: str=None, savename: str=None, sort_by_size: bool=False) -> None:
    """
        arguments
            labels : array like or str
            sizes : array like or str
            title : str
                Ex. title = "pie chart"
            savename : str
                Ex. savename = "./pie.png"

            sort_by_size : bool
        Ex.
            labels = ["A", "B"]
            sizes = [20, 231]
            pie_plot(labels, sizes)

            import pandas as pd
            df = pd.DataFrame({"labels": labels, "sizes": sizes})
            pie_plot(labels="labels", sizes="sizes", df=df)
    """
    global COLORPALLET, color_num

    if df is None and (isinstance(labels, str) or isinstance(sizes, str)):
        raise ValueError("Only in case df is given, labels and sizes can be str.")

    if df is not None:
        df = df[::-1]
        if sort_by_size:
            df = df.sort_values(by=sizes, ascending=False)

    if isinstance(labels, str):
        labels_plot = df[labels]
    else:
        labels_plot = labels

    if isinstance(sizes, str):
        sizes_plot = df[sizes]
    else:
        sizes_plot = sizes

    label_num = len(labels_plot)

    if label_num > color_num:
        raise ValueError(f"The number of labels should be under {color_num}.")

    colors = COLORPALLET[:label_num]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.pie(sizes_plot, labels=labels_plot, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.legend(loc="best")
    ax.axis('equal')
    if title is not None:
        ax.set_title(title)
    plt.tight_layout()

    if savename is None:
        plt.show()
    else:
        fig.savefig(savename)
        plt.close(fig)

if __name__ == "__main__":
    pass



