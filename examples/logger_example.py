from dsutils.utils.logger import Logger

columns = ["step", "obj_val", "val"]
dtype = {key: float for key in columns}
dtype["step"] = int

logger = Logger(columns=columns, dtype=dtype)

new_row = [0, 20.34, 0.445]
logger.append(new_row)

