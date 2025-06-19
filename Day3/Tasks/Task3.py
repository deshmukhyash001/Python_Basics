def main():
    print("Enter year")
    year = int(input())
    
    year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0   
    print("Yes it's a leap year") if year else print("Not a leap year")

if __name__ == '__main__':
    main()
