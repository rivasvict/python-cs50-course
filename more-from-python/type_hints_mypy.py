"""
To enforce typing, one could use the library
called mypy https://mypy.readthedocs.io/en/stable/index.html
It works out of the box with the normal python
syntax using anotations (see the argument of the
function below which is specified to be an int
and the arrow indicating the type that is being
returned from the function)

to use this library you only have to `pip install mypy`
and then run `mypy [my_file].py`, in this very case
it would be `mypy type_hints_mypy.py`

This will help to check type in a static way.
"""
def meow(times: int) -> str:
    return "meow\n" * times

number: int = int(input("Number: "))
print(meow(number), end="")

"""
EXTRA NOTE: On functions that do not return anything,
if you try to print them, they will print out the
string "None"
"""
