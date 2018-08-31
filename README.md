# Summary
dsci-utils is a collection of helper functions whcih makes it easier to do data science.

# Dependencies
Python 3.6+.

# USAGE
## Plot
### histgram

```
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

## Hyper Parameter Holder

```
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

```
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