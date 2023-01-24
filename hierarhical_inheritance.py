
class vehicle:
    def __init__(self, driver_name, wheels, capacity):
        self.driver_name = driver_name
        self.wheels = wheels
        self.capacity = capacity


class Bus(vehicle):
    def display(self):
        print('Bus Driver name :', self.driver_name)
        print('Number of Wheels :', self.wheels)
        print('Capacity :', self.capacity)
        print(" ")


class Truck(vehicle):
    def display(self):
        print('Truck Driver name :', self.driver_name)
        print('Number of Wheels :', self.wheels)
        print('Capacity :', self.capacity)
        print(" ")


bus1 = Bus('Adnan', 10, 500)
bus1.display()

truck1 = Truck('Mostafizz', 30, 60000)
truck1.display()
