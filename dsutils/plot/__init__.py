####
# matplotlib backend
####
import os
import matplotlib

no_display = (("DISPLAY" not in os.environ) or (os.environ["DISPLAY"] == ""))
current_backend = matplotlib.get_backend()
using_notebook = (current_backend in [
            'module://ipykernel.pylab.backend_inline',
            'NbAgg',
            ])
ssh_server = "SSH_TTY" in os.environ

if no_display:
    if ssh_server:
        if using_notebook:
            pass
        else:
            matplotlib.use('Agg')
            print(f"matplotlib backend : {current_backend} -> agg")

####
# import
####
from . import bar
from . import boxplot
from . import histgram
from . import pairplot
from . import pie
from . import scatter