class car:
    def __init__(self, brand, wheels, capacity):
        self.brand = brand  # this the public variable
        self._wheels = wheels  # this the protect variable
        self.__capacity = capacity  # this the private variable

    def display(self):
        print('The public value :', self.brand)
        print('The protect value :', self._wheels)
        print('The private value :', self.__capacity)


class Noha(car):
    def display(self):
        print('The public value :', self.brand)
        print('The protect value :', self._wheels)
        print('The private value :', self._car__capacity)
        # when we access the private value another class then we have to mention
        # the class of private value


noha = Noha('Xnoha', 4, 5000)
noha.display()
# car1 = car('Toyota', 5, 777)
# car1.display()

