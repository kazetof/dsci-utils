from dsutils.utils import status_logger as sl

STATUSDICT = {}
STATUSDICT[0] = "contain nan"
STATUSDICT[1] = "not conversion"
STATUSDICT[2] = "It seems outlier"

status_list = sl.StatusList(STATUSDICT)
status_list.append(0)

status_logger = sl.StatusListLogger(STATUSDICT)
new_row = status_logger.get_new_row()
new_row.append(1)
status_logger.append(new_row)

new_row = status_logger.get_new_row()
new_row.append(0)
new_row.append(2)
status_logger.append(new_row)

status_df = status_logger.get_status_df()