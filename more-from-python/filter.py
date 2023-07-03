students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"}
]
def main():
    #list_filter_with_list_comprenhention()
    filter_students()

def is_gryffindor(student):
    return studetn["house"] == "Gryffindor"

# This is the same as the next function list_filter_with_list_comprenhention
def filter_students():
    filtered_students = filter(is_gryffindor, students)

    # The lambda function serves to be able to sort dictionaries
    for student in (sorted(filtered_students, key=lambda student_: student_["name"])):
        print(student["name"])


# This is a way to filter as well using list comprenhention
def list_filter_with_list_comprenhention():

    filtered_students = [
            student["name"] for student in students if student["house"] == "Gryffindor"
    ]

    for student in filtered_students:
        print(student)

if __name__ == "__main__":
    main()

"""
Note: You can use the library `black` as a command `black` for code formatting fixes,
for example in this file it would be: `black filter.py`. If we want a directory, it
would be `black [name_of_my_directory]`
"""
