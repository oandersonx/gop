#!C:\Users\Anderson\PycharmProjects\head\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'google-speech==1.1.0','console_scripts','google_speech'
__requires__ = 'google-speech==1.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('google-speech==1.1.0', 'console_scripts', 'google_speech')()
    )
