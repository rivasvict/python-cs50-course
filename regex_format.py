def main():
    name = input("What's your name? ").strip()
    if matches := re.search(r"^(.+), *(.+)$", name):# := us tge walrus operator and what it does is allows the user to assign a value to a variable and ask the if statement in the same line
        name = matches.group(2) + " " + matches.group(1)
    print(f"hello, {name}")

def traditional_conditionals_with_regex():
    name = input("What's your name? ").strip()
    matches = re.search(r"^(.+), *(.+)$", name)# The parentheses in this case is used as capturing group, which means that they will be returned on the search method
    if matches:
        name = matches.group(2) + " " + matches.group(1)
    print(f"hello, {name}")
main()
