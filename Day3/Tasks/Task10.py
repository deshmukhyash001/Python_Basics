def main():
    print("Enter a year")
    year = input()
    
    print("it's centure year ") if int(year)%100==0 else print("Not century year")       

if __name__ == '__main__':
    main()
