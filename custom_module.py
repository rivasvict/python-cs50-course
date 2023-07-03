# Functions are exported by default as parts of the packages
# so they can be used right away

def main():
	print('package working')

def hello(name):
	print('Hello,', name);

def goodbye(name):
	print('Goodbye,', name);
	
	
# To only run the main function when this file is called
# The reason this works is that when this file is directly
# Run from the console as opposed as run by another file (as a package),
# then the special key __name__ is set to '__main__'.
# That is why this line will only run when the file is run directly from
# the terminal
if __name__ == '__main__':
	main()
