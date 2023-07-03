students = ["Hermione", "Harry", "Ron"]

# This `enumerate` will be an iterable that can return both the index and the element
for i, student in enumerate(students):
    print(i + 1, student)

# The previous for loop is similar to doing the following one
for i in range(len(students)):
    print(i + 1, students[i])
