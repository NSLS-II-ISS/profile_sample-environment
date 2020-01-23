
from PyQt5.QtWidgets import QApplication
import sys
from isstools import xsample

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




app = QApplication(sys.argv)

mfcs_cart= [mfc_cart_CH4,
            mfc_cart_CO,
            mfc_cart_H2,
            ]

xsample_gui = xsample.XsampleGui(mfcs=mfcs_cart, RE=RE)

def xsample():
    xsample_gui.show()

xsample()
