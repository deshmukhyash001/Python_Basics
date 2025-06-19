def main():
    print("Enter a character")
    ch = input()
    vovel = ('a','e','i','o','u')
    
    print("It's a vovel") if ch in vovel else print("It's not a vovel")
            
if __name__ == '__main__':
    main()
