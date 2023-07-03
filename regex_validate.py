import re# library for regex

# Regular expressions work like finite state machines
# The computer expects that at the end of the run
# Through the states, it will end up in the final state
# If this does not happen, the regex will not match. On
# The contraty, if it does get to the final state, then
# It concludes there is a match

def main():
    email = input("What is your email? ").strip()
    # IGNORECASE is a flag on the regex to indicate that the case type should not be taking into account when matching the expression
    if re.search(r".+@.+\.edu", email, re.IGNORECASE):# r (raw string) indicates that the string should be interpreted as is. Python will not try to interpret it, this way we can avoid escaping \n as a new line in a regular expression
        print("Valid")
    else:
        print("Invalid")


def better_validation():
    email = input("What is your email? ").strip()
    username, domain = email.split("@")
    if username and "." in domain.endswith(".edu"):
        print("Valid")
    else:
        print("Invalid")

def basic_validation():
    email = input("What is your email? ").strip()

    if "@" in email and "." in email:# This is a way to check string characters in a text
        print("Valid")
    else:
        print("Invalid")

main()
