"""
Docstrings like this one can help to document the code

They may follow a popular convention to generate the
documentation for that function (with other tools).
This convention requires that the docstring is below
the def of the function and follows certain format,
for our purposes it is restructured text. It is 
very popular convention.

see the example below in the `meow` function
"""

def meow(times: int) -> str:
    """
    Meow `times` times.

    :param times: Number of times to meow
    :type times: int
    :raise TypeError: If `times` is not an int
    :return: A string of `times` meows, one per line
    :rtype: string
    """
    return "meow\n" * times

number: int = int(input("Number: "))
print(meow(number), end="")

