def main():
    print("Enter a character")
    ch = input()
    ch = ch.isalpha()

    print("Yes i's alphabet") if ch else print("No it's not character")

if __name__ == '__main__':
    main()
