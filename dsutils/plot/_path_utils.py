import os

def _make_savedir_from_savename(savename: str) -> None:
    savedir = os.path.dirname(savename)
    os.makedirs(savedir, exist_ok=True)

if __name__ == '__main__':
    pass