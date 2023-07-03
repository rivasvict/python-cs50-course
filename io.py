import csv
import sys
from PIL import Image # Library to manipulate images
def main():
def manipulate_images():
    images = []
    for arg in sys.argv[1:]:# sys.argv[1:] slices the sts.argv (arguments passed on cli array) from 1 to the end
        image = Image.open(arg)
        images.append(image)
    images[0].save(# save to disk
            "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0# creates the gif. loop=0 loops through infinite time. append_images argument appends as many files as needed
    )

def write_to_csv():
    name = input("What is your name? ")
    home = input("Where's your home? ")
    with open("school.csv", "a") as file:
        #writer = csv.writer(file)# Manual way to write the data (the next line). It needs to be in order and same number of arguments in the array
        #writer.writerow([name, home])# Needs to be in order
        writer = csv.DictWriter(file, fieldnames=["name", "home"])# With this approach we have to provide DictWriter with the order and header columns (this is done with the named argument called `fieldnames`)
        writer.writerow({"home": home, "name": name})# It does not need order as the order is already indicated in the `fieldnames` named argument of `DictWriter` and this handles not dictionaries to write the row

def use_csv_library():
    students = []
    with open('school.csv') as file:
        #reader = csv.reader(file)# To read the csv in a raw way
        reader = csv.DictReader(file)# To read directly as a dictionary. This returns dicctionaries by row whose keys are determined by the first row (header row of the csv file)
	#for row in reader:# one way to do it or
        #for name, home in reader:# Deconstruct the array of reader. this is for the example in which the csv.reader was being used
        for row in reader:# This cannot be deconstructed as DictReader returns dictionaries instead of list
            students.append({"name": row["name"], "home": row["home"]})
    for student in sorted(students, key=lambda student: student['name'], reverse=True): # key is now a lambda function (anonymous function) that does exactly the same as get_name. Syntax `lambda [,args]: [return value]`
        print(f"{student['name']} is in {student['home']}")
		



def sorted_student():
    students = []
    with open('school.csv') as file:
        for line in file:
            name, house = line.rstrip().split(",")
            student = { "name": name, "house": house }
            students.append(student)
    def get_name(student):
        return student["name"]
    # for student in sorted(students, key=get_name, reverse=True): # key named argument receives a function that will receive the key to sort by. The reverse named argument can do reverse sorting
    for student in sorted(students, key=lambda student: student['name'], reverse=True): # key is now a lambda function (anonymous function) that does exactly the same as get_name. Syntax `lambda [,args]: [return value]`
            print(f"{student['name']} is in {student['house']}")
            

def sloppy_ordered_student():
    students = []
    with open('school.csv') as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append(f"{name} is in {house}")
        for student in sorted(student):
            print(student)

def unordered_students():
    with open("school.csv") as file:
        for line in file:
            # rstrip removes the white space at the end of the line
            name, house = line.rstrip().split(",")# This is the way to deconstruct arrays in python. It makes the string to become a list
            print(f"Name: {name}, Lives in: {house}");

def write_csv():
    i = 0
    with open("school.csv", "a") as file:
        while i < 3:
            name = input("What is your name? ")
            house = input("What is your house? ")
            file.write(f"{name},{house}\n");
            i = i + 1


def sort_names():
    names = []
    with open("names.txt") as file:# It is readable by default, that is why we do not have to add the `r` flag to this `open()` call
        #for line in sorted(file): # Alternative more compact syntax for sorting
        for line in file:
            names.append(line)

    for name in sorted(names, reverse=True):
        print(f"Hello, {name}")

def read_file():
    with open("names.txt", "r") as file:# The `r` flag is to read the flag
        #lines = file.readlines()
        for line in file:# I commented the line above in order for this one to work. This is because when using `readlines` once the whole file is read, the position of the indicator is in the last line, therefore no other iterations are possible, one would have to close and reopen the file or use `file.seek(0) to return the indicator to its initial position and be able to read it again.
            print("Also reading from file", line)

    #for line in lines:
        #print("Hello,", line, line.rstrip())# `rstrip([chars])` method will get trailing characters removed from the string. Its optional parameter will remove the matching characters, if not passed, it removes the witespaces
    
def write_file():
    name = input("What's your name? ")
    # With the keyword "with" we can let the program handle
    # the resource management. It automates away the details
    # of setup and teardown operations as well as the proper
    # management of resources and cleaning even in the presence
    # of errors. Syntax: `with expression [as variable]`
    # with open("names.txt", "w") as file:# `w` Write flag will recreate the file every single time
    with open("names.txt", "a") as file:# `a` Lets us append by using the `.write()` function
        file.write(f"{name}\n"); # To write the document
        file.close() # THIS IS NOT NECESSARY AS `with` handles all of the file resoutces already

def print_names_in_order():
    names = []

    for _ in range(3):
        names.append(input("What's your name? "))
    for name in sorted(names):
        print(f"hello, {name}")

main();
