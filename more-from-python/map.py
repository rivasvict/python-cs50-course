def main():
    print(*yell("This is CS50"))

def yell(*words):
    return map(str.upper, words)

if __name__ == "__main__":
    main()
