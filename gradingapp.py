import os
os.environ['QT_API'] = 'pyqt5'
import argparse
import sys
from PyQt5.QtWidgets import QApplication
from grader.appmodel import Grader
from grader.appview import AppView
try:
    from grader.util import BUILD_NUMBER  # this is appended to the util module during GitHub Actions deployment
except ImportError:
    BUILD_NUMBER = ""  # default to an empty string if we can't find a build number

VERSION = '1.0'

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='store_true')
args = parser.parse_args()
if args.version:
    print('Grader ' + VERSION + ' Build ' + BUILD_NUMBER)
else:
    main = QApplication([])
    main.setQuitOnLastWindowClosed(True)
    model = Grader()
    view = AppView(model)
    sys.exit(main.exec_())
