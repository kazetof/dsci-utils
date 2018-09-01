# Summary
dsci-utils is a collection of helper functions whcih makes it easier to do data science.

# Dependencies
Python 3.6+.

```
numpy == 1.15.1
pandas == 0.23.4
seaborn == 0.9.0
matplotlib == 2.2.3
```

# USAGE
## Plot
### histgram

```python
import numpy as np
import pandas as pd

from dsutils import plot

x1 = np.random.randn(100)
x2 = np.random.randn(100)
df = pd.DataFrame(dict(x1=x1, x2=x2))

savename = "./output/histgram_example.png"
plot.histgram.plot(df, colname="x1", savename=savename)

colnames = ["x1", "x2"]
savepath = "./output"
plot.histgram.s_plot(df, colnames=colnames, savepath=savepath)
```

### scatter

```python
# df.head(2)
#           x         y
# 0 -0.466440  1.727682
# 1  0.304809  1.378079

plot.scatter.plot(df, "x", "y")

savename = "./output/scatter_example.png"
plot.scatter.plot(df, "x", "y", savename=savename)
```

### pairplot (seaborn)

```python
# df.head(2)
#           A         B         C       D
# 0  0.129275  0.775375 -0.819235  class1
# 1 -0.587624 -6.162496 -0.032990  class2

colnames = ["A", "B", "C"]
savename = "./output/pairplot_example.png"
plot.pairplot.plot(df, colnames, classes="D", savename=savename)
```

## Hyper Parameter Holder

```python
hpholder = MyHPHolder() # see examples

hpholder.alpha = 10.

hpholder.set_preprocess_params(normalized=True, delete_nan=False)
hpholder.set_model1_params(alpha=10, tol=0.0001)
hpholder.set_model2_params(depth=5)

hpholder
# {'normalized': True, 'delete_nan': False, 'alpha': 10, 'tol': 0.0001, 'depth': 5}

hpholder.preprocess
# {'delete_nan': False, 'normalized': True}
```

## Logger

```python
from dsutils.utils.logger import Logger

columns = ["step", "obj_val", "val"]
dtype = {key: float for key in columns}
dtype["step"] = int

logger = Logger(columns=columns, dtype=dtype)

new_row = [0, 20.34, 0.445]
logger.append(new_row)

#    step  obj_val    val
# 0     0    20.34  0.445
```

## Status Logger

```python
from dsutils.utils import status_logger as sl

STATUSDICT = {}
STATUSDICT[0] = "contain nan"
STATUSDICT[1] = "not conversion"
STATUSDICT[2] = "It seems outlier"

status_logger = sl.StatusListLogger(STATUSDICT)
new_row = status_logger.get_new_row()
new_row.append(1)
status_logger.append(new_row)

new_row = status_logger.get_new_row()
new_row.append(0)
new_row.append(2)
status_logger.append(new_row)

status_df = status_logger.get_status_df()

#    0  1  2
# 0  0  1  0
# 1  1  0  1
```