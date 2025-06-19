def main():
    print("Your age : ")
    age = int(input())
    print("You are Eledgible to vote") if age >=18 else print("You are not eledgible to vote")

if __name__ == '__main__':
    main()
