# Dictionaries comprenhention is a way to build an object out of an iterable expression such as an array
# This is the very same idea of doing it with list comprenhentions but for dictionaries
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)
