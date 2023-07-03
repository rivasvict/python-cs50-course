import random
class Hat_singleton:
    """
    As this is a singleton, there is no need for instance variables
    as we will not be instancing variable. Thus `self` is not necessary
    the idea in a singleton would be to use cls to access this variable
    as we see below in the `random_house_sort`  
    """
    houses = ["house0","house1","house2","house3",]
    """
    @classmethod makes sure this is a static function
    """
    @classmethod
    def random_house_sort(cls, name):# Note that the keyword self is not used here as the firt parameter to refer to the class because we are referring here to the class, we use cls. This is true for @classmethod s
        # When using a static method
        print(name, "is in", random.choice(cls.houses));

class Hat:
    def __init__(self):
        self.houses = ["house0","house1","house2","house3",]
    def random_house_sort(self, name):
        print(name, "is in", random.choice(self.houses));

hat = Hat()
hat.sort("Harry")
