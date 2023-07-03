from calculator import square
from pytest import raises

# To use pytest, you need to install it first with pip and run this
# file from the command line like `pytest test_calculator.py`.
# If you want to run the test in a folder, you need to create the folder

# And then add an empty file called __init__.py which tells python to treat
# The folder as a package, then you can call pytest [folder_name]. A package
# is a module or multiple modules organized in a folder

# The next function is not needed for testing when doing it with pytest
#def main():
	#test_square()

# It is encouraged to separate the tests into different functions for the different cases
def test_positive():
	# Pytest will take care of all of the failing and printing logic
	assert square(2) == 4
	assert square(3) == 9

def test_negative():
	assert square(-2) == 4
	assert square(-3) == 9

def test_zero():
	assert square(0) == 0

def test_str():
	with raises(TypeError):# Checks that a TypeError was risen
		square("cat")

# The next conditional is not needed for testing when doing it with pytest
# if __name__ == "__main__":
#	main()
