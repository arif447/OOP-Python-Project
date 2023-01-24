class Student:
    def __init__(self, st_name, st_roll):
        self.student_name = st_name
        self.student_roll = st_roll

    def display_student_informations(self):
        print('Name :', self.student_name, "\nRoll :", self.student_roll)


class Mark:

    def setnumber(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def display_number(self):
        print('Number 1 :', self.number1)
        print('Number 2 :', self.number2)


class result(Student, Mark):
    def calculate(self):
        self.sum = self.number1 + self.number2

    def display_result(self):
        print('Name :', self.student_name, "\nRoll :", self.student_roll)
        print('The result is :', self.sum)
student1 = result('arif', 22)
student1.setnumber(33, 66)
student1.display_student_informations()
student1.display_number()
student1.calculate()
student1.display_result()


