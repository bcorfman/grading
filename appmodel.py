class Grader:
    def validate_data(self, text):
        try:
            score = float(text)
        except ValueError:
            return False
        return score

    def passed_class(self, grade):
        try:
            if grade in ['A', 'B', 'C']:
                return "You passed the class!"
            elif grade in ['D', 'F']:
                return "You failed the class!"
            else:
                raise TypeError(f'Unrecognized grade: {grade}')
        except TypeError:
            return None

    def get_letter_grade(self, score):
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
