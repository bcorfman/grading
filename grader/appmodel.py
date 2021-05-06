from typing import Union


class Grader:
    def validate_data(self, text) -> Union[float, None]:
        """ Validates the incoming text by making sure it can be converted to a Real
            (i.e., floating-point) type. If not, return None. """
        score = None
        try:
            score = float(text)
        except ValueError:
            pass
        return score

    def passed_class(self, grade) -> Union[str, None]:
        """ Given a letter grade, returns a message telling the student whether they
            passed their class, or None indicating an invalid grade. """
        result = None
        if grade in ['A', 'B', 'C']:
            result = 'You passed the class!'
        elif grade in ['D', 'F']:
            result = 'You failed the class!'
        return result

    def get_letter_grade(self, score) -> Union[str, None]:
        """ Given a score, return a letter grade,
            or None indicating an invalid score. """
        grade = None
        try:
            if score >= 90.0:
                grade = 'A'
            elif 80.0 <= score < 90.0:
                grade = 'B'
            elif 70.0 <= score < 80.0:
                grade = 'C'
            elif 60.0 <= score < 70.0:
                grade = 'D'
            elif 0.0 <= score < 60.0:
                grade = 'F'
        except TypeError:
            pass
        return grade
