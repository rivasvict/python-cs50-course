def main():
	things = [
		{'test': None,'number': 1},
		{'test': 'test', 'number': 2}
	]

	for things in things:
		print(things['test'], things['number'])
def howards_2():
	students = {
		'Hermione': 'Gryfindor',
		'Harry': 'Gryfindor',
		'Ron': 'Gryfindor',
		'Draco': 'Slytherin',
	}

	for student in students:
		print(student, students[student], sep=', ')
	
def howarts():
	students = ['Hermione', 'Harry', 'Ron']
	for student in students:
		print(student)
	for i in range(len(students)): # Len function to get the length of the list
		print(students[i])

def cat():
	number = get_number()
	meow(number)

def get_number():
	while True:
		number = int(input('How many times to repeat? '))
		if number > 0:
			return number # Snaps out of the loop. If you were to use brewk, you'd have to return the number after the loop finishes

def meow(number):
	for _ in range(number):
		print('meow')

main()

def practice_loops():
	i = 3
	while i != 0:
		print('test')
		i -= 1

	for i in [0, 1, 2]:
		print('test2')

	for i in range(3):
		print('test3')

	for _ in range(3): # Underscore to indicate we are not using the variable
		print('test3')

	print('test' * 3, end='')

	while True:
		n = int(input('what is n: '))
		if n > 0:

			break;
