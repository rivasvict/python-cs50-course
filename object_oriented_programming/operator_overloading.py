class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    def __add__(self, other):# Operator overload. This makes the + operator work in a different way when two objects of type Voult are put together Vault1 + Vaul2. `self` (left side) + `other` (right side). In here at the end you want to return the result as desired, in this case, we want to have the result of the two Vault in a new different Vault object.     Other could be any other object that has the `__add__` method implementation
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
print(potter)
weasley = Vault(25, 50, 100)
print(weasley)
print(weasley + potter)
