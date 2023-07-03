class Person(name):
    def __init__(self, name):
        self.name = name
class Employee(Person):# Employee extends Person class
    def __init__(self, name, title):
        super().__init__(name)# Constructor call of the Person class
        self.name = name
        slef.title = title

    ...
class Boss(Person):# Boss extends Person class
    def __init__(self, name, number_of_employees):
        super().__init__(name)# Constructor call of the Person class
        self.name = name
        self.number_of_employees = number_of_employees

    ...
