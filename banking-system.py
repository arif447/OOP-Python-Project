class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender



    def Display_Information(self):
        print('Personal Information ')
        print(" ")
        print('Name :', self.name)
        print('Age :', self.age)
        print('Gender :', self.gender)


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0



    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated :", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print('Insufficient balace :', self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated :", self.balance)

    def show_balace(self):
        self.Display_Information()
        print("Balace :", self.balance)

user1 = Bank('Arif', 33, 'male')
user1.Display_Information()
user1.deposit(1000)
user1.withdraw(500)
user1.show_balace()


