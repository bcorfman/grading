from grader.appmodel import Grader


def test_validate_score():
    g = Grader()
    assert (g.validate_data('-0.01') == -0.01)
    assert (g.validate_data('0.00') == 0.00)
    assert (g.validate_data('0.01') == 0.01)
    assert (g.validate_data('100.00') == 100.00)
    assert (g.validate_data('100.01') == 100.01)
    assert (g.validate_data('A') is False)


def test_get_letter_grade():
    g = Grader()
    assert('A' == g.get_letter_grade(101.0))
    assert('A' == g.get_letter_grade(95.0))
    assert('B' == g.get_letter_grade(85.0))
    assert('C' == g.get_letter_grade(75.0))
    assert('D' == g.get_letter_grade(65.0))
    assert('F' == g.get_letter_grade(55.0))


def test_passed_class():
    g = Grader()
    assert (g.passed_class('A') == "You passed the class!")
    assert (g.passed_class('B') == "You passed the class!")
    assert (g.passed_class('C') == "You passed the class!")
    assert (g.passed_class('D') == "You failed the class!")
    assert (g.passed_class('F') == "You failed the class!")


def test_integration():
    g = Grader()
    assert (g.passed_class(g.get_letter_grade(-1.0)) is None)
    assert (g.passed_class(g.get_letter_grade('100.0')) is None)
    assert(g.passed_class(g.get_letter_grade(0.0)) == 'You failed the class!')
    assert(g.passed_class(g.get_letter_grade(50.0)) == 'You failed the class!')
    assert(g.passed_class(g.get_letter_grade(70.0)) == 'You passed the class!')
    assert(g.passed_class(g.get_letter_grade(101)) == 'You passed the class!')


def test_system():
    ga = Grading