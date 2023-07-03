def main():
    #yell("This is CS50")
    list_filter_with_list_comprenhention()

def yell(*words):
    # List comprenhention help us generating lists on the go with an iteration expression such as `for word in words`
    print(*[word.upper() for word in words])
    # Similar to do this next line
    print(*map(str.upper, words))

# This is a way to filter as well using list comprenhention
def list_filter_with_list_comprenhention():
    students = [
            {"name": "Hermione", "house": "Gryffindor"},
            {"name": "Harry", "house": "Gryffindor"},
            {"name": "Ron", "house": "Gryffindor"},
            {"name": "Draco", "house": "Slytherin"}
    ]


    filtered_students = [
            student["name"] for student in students if student["house"] == "Gryffindor"
    ]

    for student in filtered_students:
        print(student)

if __name__ == "__main__":
    main()

