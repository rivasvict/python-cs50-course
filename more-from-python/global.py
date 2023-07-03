balance = 0

def main():
    print("Balance:", balance)
    add(100)
    remove(50)
    print("New balance is:", balance)

def add(amount):
    """
    Constants can only be read by default
    in order to be able to write and update
    one would have to specify the word global
    prior to the use of the variable
    """
    global balance
    balance += amount

def remove(amount):
    global balance
    balance -= amount

if __name__ == "__main__":
    main()
