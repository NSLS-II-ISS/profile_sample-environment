
from PyQt5.QtWidgets import QApplication
import sys
from iss_xsample import xsample

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


#import matplotlib
#matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
plt.ion()


app = QApplication(sys.argv)



xsample_gui = xsample.XsampleGui(mfcs=mfcs_cart,
                                 rga_channels=rga_channels,
                                 rga_masses=rga_masses,
                                 ghs=ghs,
                                 RE=RE,
                                 archiver = arch_iss)
#
def xsample_show():
    xsample_gui.show()

xsample_show()
