def main():
    execute()
"""
Excercise, create a student class that:
    * Is a singleton (other objects cannot be created from it)
    * Will have a get classmethod that asks for the student data from an input
    * Has validation of the name and house class properties
    * Uses getters and setters for its properties
    * Uses the __str__ built in standard method to print the student when called `print` upon it
    * Finally, make sure to call the class and print the new singleton student
"""

class Student_singleton():
    def __init__(self, name, house):
        self.name = name
        self.house = house
    def __str__(self):
        return f"The student name is {self.name} and it lives in {self.house}"
    @property
    def _valid_houses(self):
        return ("house0", "house1", "house3");

    @classmethod
    """
    One of the main differences between cls and self is that self has access to
    anything defined in the self onject (which depends on the class instance). On
    the other hand cls has access to the class-related variables (the ones defined)
    outside of the constructor
    """
    """
    Also there exists the decorator @staticmethod which is a method that does not
    have access to the class' instance and does not depend in it.
    """
    def get(cls):
        name = input("What is your name? ")
        house = input("What is your house? ")
        # cls is the reference as a class and calling it, we set up the singleton
        return cls(name, house)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Student must have a name")
        self._name = name

    @property
    def house(self):
        return self._house
    @house.setter
    def house(self, house):
        if house not in self._valid_houses:
            # This is a generator expression `str(valid_house) for valid_house in self._valid_houses`. It can be used to join a string https://docs.python.org/3/reference/expressions.html?highlight=generator%20expresion#grammar-token-python-grammar-generator_expression
            valid_entries = ", ".join(str(valid_house) for valid_house in self._valid_houses)
            raise ValueError("Invalid house: ", "House must be one of the following: ", valid_entries)
        self._house = house


def execute():
    student = Student_singleton.get()
    print(student)

main()
