def main():
	my_bytes = bytearray(b'Hello');
	my_bytes[1] = 111;
	print(my_bytes);

	print('--------------------------------------------------');
	my_diccionary = {
		'key1': 'value1',
		'key2': 'value2',
	};

	print('key3' in my_diccionary);

	name = input('What is your name? ');

	name = name.title();
	print(name);

	# Floating point number. Formatting to rounding with formatted strings

	x = 100
	y = 10

	s = x * y
	a = y / x

	print(f'{s:,}'); # Formats the number to separate by comma
	print(f'{a:.2f}') # Syntax to cause rounding to two digits on float point numbers

	# Functions


	hello(name);

def hello(to='world'):
	print('Hello, ', to);

main();
