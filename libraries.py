import statistics
import random
import sys
# Can use from as well
from random import choice
# You can check random's documentation (shuffle, randint)
# Check statistics
# Check command-line-argument (sys, sys.argv)
	# sys.exit will allow you to exit the program at any time
# Check json package with json.dumps to format the output of a json response to be more readable
# You can also use pip
# Check APIs for requests specifically the request package (SYNCHRONOUS)
	# request.get(url)
from custom_module import hello

def main():
	hello('victor')


def slices():
	print([1, 2, 3, 4, 5][:-1]) # [1, 2, 3, 4]
	print([1, 2, 3, 4, 5][1:-1]) # [2, 3, 4]
	print([1, 2, 3, 4, 5][1:]) # [2, 3, 4, 5]

def use_sys():
	if len(sys.argv) < 2:
		sys.exit('Too few arguments')
	for arg in sys.argv[1:]:# The part in the square brackets will get a range from 1 to the end of the array with the : implying the end. This is the way slices are done in pytho. USE -1 TO COUNT FROM THE END [1:-1]
		print('Hello, my name is:', sys.argv[1])
	

def coin_toss():
	coin = random.choice(['heads', 'tails']);
	coin2 = choice(['heads', 'tails']);
	print(coin);

main()
