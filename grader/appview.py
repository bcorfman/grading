from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class AppView(QMainWindow):
    def __init__(self, model):
        QMainWindow.__init__(self, None)
        self.model = model
        self.win = loadUi('grading.ui', self)
        self.win.btnDidIPass.clicked.connect(self.onBtnClickDidIPass)
        self.win.show()

    def onBtnClickDidIPass(self):
        label = self.win.lblResult
        text = self.win.txtGrade.text()
        if self.model.validate_data(text):
            score = float(text)
            grade = self.model.get_letter_grade(score)
            if grade:
                result = self.model.passed_class(grade)
                if result is not None:
                    label.setText(result)
                else:
                    label.setText(f"Could not evaluate {grade} in passed_class.")
            else:
                label.setText("Score not in 0-100 range.")
        else:
            label.setText(f"Unrecognized score: {text}")
