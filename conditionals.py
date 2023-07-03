def main():
	if 3 == 3:
		print('equal');

	test(-3);

def test(num):
	if -5 < num < 1:# Equivalent to -5 < num and num < 1. As both of num evaluations are one beside the other one, it can be simplified to -5 < num < 1
		print('chaining operators inside a conditional');

def is_even(n):
	return True if n % 2 == 0 else False # Pythonic way to create a ternary operator

def my_macth(name):
	match name: # This is the switch case for python
		case 'Harry' | 'Ron': # The equivalent to OR in match case
			print('Gryffindor');
		case 'Draco':
			print('Slytherin');

main();
