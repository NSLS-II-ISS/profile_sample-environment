
from PyQt5.QtWidgets import QApplication
import sys
from isstools import xsample

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




app = QApplication(sys.argv)



xsample_gui = xsample.XsampleGui(mfcs=mfcs_cart,
                                 rga_channels=rga_channels,
                                 rga_masses=rga_masses,
                                 temps = temps,
                                 temps_sp = temps_sp,
                                 heater_enable1=heater_enable1,
                                 RE=RE,
                                 archiver = arch_iss)

def xsample():
    xsample_gui.show()

xsample()
