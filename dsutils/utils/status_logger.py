from collections import UserList

import numpy as np
import pandas as pd

class StatusList(UserList):
    """
    Ex.
        In [6]: STATUSDICT = {}
           ...: STATUSDICT[0] = "contain nan"
           ...: STATUSDICT[1] = "not conversion"
           ...: STATUSDICT[2] = "It seems outlier"
           ...:
           ...: status_list = sl.StatusList(STATUSDICT)
           ...: status_list.append(0)
        In [7]: status_list
        Out[7]:

        0 : contain nan
    """
    def __init__(self, STATUSDICT: dict):
        self.data = []
        self.STATUSDICT = STATUSDICT

    def append(self, item: int) -> None:
        if not item in self.STATUSDICT:
            raise ValueError(f"{item} is not in status.")
            
        self.data.append(item)

    def __repr__(self):
        status_str = self._parse_status2str(self.data)

        output_text = "\n"
        for i, string in zip(self.data, status_str):
            output_text = output_text + str(i) + " : " + string + "\n"
        return output_text

    def _parse_status2str(self, data) -> list:
        status_str = [self.STATUSDICT[i] for i in data]
        return status_str

class StatusListLogger(object):
    """
        In [1]: from dsutils.utils import status_logger as sl
           ...:
           ...: STATUSDICT = {}
           ...: STATUSDICT[0] = "contain nan"
           ...: STATUSDICT[1] = "not conversion"
           ...: STATUSDICT[2] = "It seems outlier"
           ...:
           ...: status_logger = sl.StatusListLogger(STATUSDICT)
           ...:

        In [2]: status_logger
        Out[2]: []
        In [3]: new_row = status_logger.get_new_row()
           ...: new_row.append(1)
           ...: status_logger.append(new_row)
           ...:

        In [4]: new_row
        Out[4]:

        1 : not conversion

        In [5]: status_logger
        Out[5]:
        [
        1 : not conversion
        ]

        In [6]: new_row = status_logger.get_new_row()
           ...: new_row.append(0)
           ...: new_row.append(2)
           ...: status_logger.append(new_row)
           ...:

        In [7]: status_df = status_logger.get_status_df()
           ...:

        In [8]: status_logger
        Out[8]:
        [
        1 : not conversion
        ,
        0 : contain nan
        2 : It seems outlier
        ]

        In [9]: status_df
        Out[9]:
           0  1  2
        0  0  1  0
        1  1  0  1
    """
    def __init__(self, STATUSDICT: dict):
        self.STATUSDICT = STATUSDICT
        self.data = []

    def __repr__(self):
        return repr(self.data)

    def get_new_row(self) -> StatusList:
        status_list = StatusList(self.STATUSDICT)
        return status_list

    def append(self, item: StatusList) -> None:
        if not isinstance(item, StatusList):
            raise TypeError("StatusList class should be passed.")

        self.data.append(item)

    def get_status_df(self) -> pd.DataFrame:
        """
        Ex.
            In [2]: status_df = status_logger.get_status_df()

            In [3]: status_df
            Out[3]:
               0  1  2
            0  0  1  0
            1  1  0  1
        """
        status_keys = list(self.STATUSDICT.keys())
        N_status = len(status_keys)

        status_vectorized = np.empty((0, N_status))

        for status_list in self.data:
            status_row = status_list.data
            row = np.zeros((1, N_status))
            for i in status_row:
                row[0, i] = 1

            status_vectorized = np.r_[status_vectorized, row]

        status_df = pd.DataFrame(status_vectorized, columns=status_keys, dtype=int)

        return status_df

if __name__ == "__main__":
    pass