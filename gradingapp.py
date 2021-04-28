import sys
from PySide2.QtWidgets import QApplication
from appmodel import Grader
from appview import AppView


if __name__ == "__main__":
    main = QApplication()
    main.setQuitOnLastWindowClosed(False)
    model = Grader()
    view = AppView(model)
    sys.exit(main.exec_())
