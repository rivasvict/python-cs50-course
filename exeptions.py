def main():


def re_ask_for_input_until_it_is_ok():
	while True:
		try:
			x = int(input('What is x? '))
			# break can be used here as if int fails, it will not continue after the error is encountered
		except ValueError:
			pass # This will skip the error
			print('x is not an integer')
		except ZeroDivisionError as error: # Just AN EXAMPLE FO CATCHING MULTIPLE Types of errors, you can the use error to print it
			print(str(error)); # Use the str function to get a string representation of the error that can be printed
		except: # To catch any error (ALL OF THE ERRORS)
			pass
		except Exception: # Catches all of the erros of the Exception class like: ValueError, TypeError, ZeroDivisionError
			pass
		else:
			break
	print(f'x os {x}')

def simple_try_except:
	try:
		x = int(input('What is x? '))
	except ValueError:
		print('x is not an integer')
	else:
		print(f'x os {x}')

main()
