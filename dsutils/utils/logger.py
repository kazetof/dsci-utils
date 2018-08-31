import pandas as pd
import numpy as np

class Logger(object):
    """
    Ex.
        In [1]: from dsutils.utils.logger import Logger
           ...:
           ...: columns = ["step", "obj_val", "val"]
           ...: dtype = {key: float for key in columns}
           ...: dtype["step"] = int
           ...:
           ...: logger = Logger(columns=columns, dtype=dtype)
           ...:
           ...: new_row = [0, 20.34, 0.445]
           ...: logger.append(new_row)

        In [2]:

        In [2]: logger
        Out[2]:
           step  obj_val    val
        0     0    20.34  0.445
    """
    def __init__(self, columns=None, dtype=None):
        self.dtype = dtype
        self._df = self._init_logdf(columns)

    def _init_logdf(self, columns=None):
        if columns is None:
            # default columns
            self.columns = ["step", "obj_val"]

        self.columns = columns
        _df = pd.DataFrame(columns=self.columns)

        if self.dtype is not None:
            _df = _df.astype(self.dtype)

        return _df

    def append(self, new_row):
        """
        arguments
            new_row : list like
                new_row vector whose shape is (n,) and n is len(columns).
        """
        new_row = np.array(new_row).reshape(1, len(self.columns))
        new_row_df = pd.DataFrame(new_row, columns=self.columns)
        self._df = pd.concat([self._df, new_row_df], ignore_index=True)

        if self.dtype is not None:
            self._df = self._df.astype(self.dtype)

    def to_csv(self, savename: str):
        self._df.to_csv(savename, index=False, sep=",")

    def __repr__(self):
        return repr(self._df)

if __name__ == '__main__':
    pass