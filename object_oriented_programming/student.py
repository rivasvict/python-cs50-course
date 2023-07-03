# Python classes documentation
def main():
    object_oriented_programming_complex_student_implementation();


class Student:
    def __init__(self, name, house, patronus):# This is the constructor and self is the access to the object of the object
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):# __str__ is a standard fucntion that will be called by default when a print is called upon the object instance of the class
        return f"{self.name} from {self.house}"

    """
    Getters are created by using the name of the property instance
    we want to create the getter for as a method and a decorator
    called @property.

    As you see below we have the `house` property. This means that
    every time we call self.house to get the property outside of this
    method (even from outside of the class as student.house), we are
    calling this getter method.
    """
    # Getter
    @property
    def house(self):
        return self._house;

    """
    For setters, the story is practically the same as getters, the
    only difference in syntax is that the setter uses a different
    decorator which should be called @house.[name_of_property]
    """
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["house1", "house2"]:# This is a way to check if an element is part of a list
            raise ValueError("Invalid house")
        """
        IMPORTANT:
        In setters and getters, we should NOT use the same variable instance
        name as the property name. The reason is because if we do, the setter,
        getter and name of the property class will collide and python will not
        know which one we are referring to. that is why we by convention use an
        underscore as a prefix on the name to indicate that this is the underlying
        variable name used to return and set the property instance name in which
        case is house.

        Also, the name of the property uses an underscore in this case by convention
        to tell other programmers not to touch this variable as it is a private variable.
        Python does not enforce any type of encapsulation as other languages
        """
        self._house = house
    
    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, name):
        if not name:# This is a way to check if the name is not empty
            raise ValueError("Missing name")
        self._name = name



    """
    # match only works in python3.10
    def charm(self):
        match self.patronus:
            case "Stag":
                return "horse"
            case "Otter":
                return "mouse"
            case _:
                return "/"
    """
    def charm(self):
        if self.patronus == "Stag":
            return "horse"
        elif self.patronus == "Otter":
            return "mouse"
        else:
            return "/"


def object_oriented_programming_complex_student_implementation():
    def get_student():
        name = input("name: ")
        house = input("house: ")
        patronus = input("patronus: ")
        student = Student(name, house, patronus)
        print(student)
        return student

    student = get_student()
    print(f"student._name: {student._name}")
    print(student.charm())
    print(f"{student.name} on house {student.house}")


class Basic_student:# This is a class and can be deemed as a custom data type
    ...# This is the notation for a placeholder implementation. One can also use `pass`
def object_oriented_programming_basic_student_implementation():
    def get_student():
        student = Basic_student()
        student.name = input("name: ")
        student.house = input("house: ")
    student = get_student()
    print(f"{student.name} on house {student.house}")


def procedural_student_implementation():
    student = get_student()

    def get_student():
        name = input('name: ')
        house = input('house: ')
        # Tuples cannot be mutated
        return (name, house) # Tuple: It can be expressed with parentheses and comma or parentheses can be ommited

if __name__ == "__main__":
    main()
