from PyQt5.QtWidgets import QApplication
from grader.appmodel import Grader
from grader.appview import AppView


def setup_app_and_view():
    main = QApplication([])
    main.setQuitOnLastWindowClosed(True)
    return main, AppView(Grader())


def test_system_passed_the_class():
    app, view = setup_app_and_view()
    view.win.txtGrade.setText('85.0')
    view.onBtnClickDidIPass()
    assert(view.win.lblResult.text() == 'You passed the class!')


def test_system_failed_the_class():
    app, view = setup_app_and_view()
    view.win.txtGrade.setText('55.0')
    view.onBtnClickDidIPass()
    assert(view.win.lblResult.text() == 'You failed the class!')


def test_system_invalid_type_error():
    app, view = setup_app_and_view()
    view.win.txtGrade.setText('Z')
    view.onBtnClickDidIPass()
    assert(view.win.lblResult.text() == 'Unrecognized score: Z')


def test_system_negative_number_error():
    app, view = setup_app_and_view()
    view.win.txtGrade.setText('-1.0')
    view.onBtnClickDidIPass()
    assert(view.win.lblResult.text() == 'Score not in 0-100 range.')
