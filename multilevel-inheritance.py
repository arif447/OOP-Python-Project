class Student:
    def __init__(self, st_name, st_roll):
        self.student_name = st_name
        self.student_roll = st_roll

    def display_student_informations(self):
        print('Name :', self.student_name, "\nRoll :", self.student_roll)


class Marks(Student):
    def __init__(self, st_name, st_roll, number1, number2):
        super().__init__(st_name, st_roll)
        self.number1 = number1
        self.number2 = number2


class result(Marks):

    def calculate(self):
        self.total = self.number1 + self.number2

    def display_result(self):
        print('Name :', self.student_name, "\nRoll :", self.student_roll)
        print('The result is :', self.total)

student1 = result('arif', 4, 6, 7)
student1.calculate()
student1.display_result()