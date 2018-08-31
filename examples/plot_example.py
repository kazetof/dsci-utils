import numpy as np
import pandas as pd

from dsutils import plot

# bar plot
df = pd.DataFrame({"a": ["A", "B", "C", "A", "A"]})
colname = "a"
plot.bar.categorical_hist_plot(df=df, colname=colname)

savename = "./output/bar_example.png"
plot.bar.categorical_hist_plot(df=df, colname=colname, savename=savename)

df = pd.DataFrame({"a": [1,1,2,2,2,3], "b": ["M","F","M","F","F","F"], "c": [0,0,0,0,0,1]})
colnames = ["a", "b"]
plot.bar.bar_plot_categorical_columns(df, colnames=colnames)

df = pd.DataFrame({"class": [1,1,1,0,0,0], "values1": [2,3,4,20,21,22], "values2": [10,13,14,5,6,7]})
stack_columns = ["values1", "values2"]
x_column = "class"
plot.bar.plot_columns_stacked_bar(df, stack_columns)
plot.bar.plot_columns_stacked_bar(df, stack_columns, x_column=x_column)

# scatter
x = np.random.randn(100)
y = np.random.randn(100)
df = pd.DataFrame({"x": x, "y": y})

plot.scatter.plot(df, "x", "y")

savename = "./output/scatter_example.png"
plot.scatter.plot(df, "x", "y", savename=savename)

# pie chart
df = pd.DataFrame({"type": ["A", "B", "C"], "volume": [200, 100, 300]})

plot.pie.plot(labels="type", sizes="volume", df=df)
plot.pie.plot(labels="type", sizes="volume", df=df, sort_by_size=True)

# pairplot
A = np.random.randn(100)
B = 10*A + np.random.randn(100)
C = np.random.randn(100)
D = np.tile(["class1", "class2"], 50)
df = pd.DataFrame(dict(A=A, B=B, C=C, D=D))
colnames = ["A", "B", "C"]
plot.pairplot.plot(df, colnames, classes="D")

savename = "./output/pairplot_example.png"
plot.pairplot.plot(df, colnames, classes="D", savename=savename)

# histgram
x1 = np.random.randn(100)
x2 = np.random.randn(100)

df = pd.DataFrame(dict(x1=x1, x2=x2))
savename = "./output/histgram_example.png"
plot.histgram.plot(df, colname="x1", savename=savename)

colnames = ["x1", "x2"]
savepath = "./output"
plot.histgram.s_plot(df, colnames=colnames, savepath=savepath)

# box plot
A = np.random.randn(100)
B = 10*A + np.random.randn(100)
C = np.random.randn(100)
D = np.tile(["class1", "class2"], 50)
df = pd.DataFrame(dict(A=A, B=B, C=C, D=D))
colnames = ["A", "B", "C"]

plot.boxplot.plot(df, x_colname="D", y_colname="A")

savepath = "./output"
plot.boxplot.s_plot(df, colnames=colnames, x_colname="D", savepath=savepath)

