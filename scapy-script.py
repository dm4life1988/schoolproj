#!C:\Users\ksutt\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'scapy==2.4.5','console_scripts','scapy'
__requires__ = 'scapy==2.4.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('scapy==2.4.5', 'console_scripts', 'scapy')()
    )
