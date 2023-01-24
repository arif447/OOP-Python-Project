class parent:
    def __init__(self, hair_color, eye_size, height):
        self.hair_color = hair_color
        self.eye_size = eye_size
        self.height = height


class child(parent):
    def display(self):
        print('Hair color :', self.hair_color)
        print('Eye :', self.eye_size)
        print('Body Height :', self.height)
        print("")
child1 = child('Black', 'Big', 6.00)
child1.display()



