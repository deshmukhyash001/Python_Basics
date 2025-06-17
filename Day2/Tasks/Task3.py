def Even_or_Odd(num):
    if num & 1 == 0:
        print("Number is Even")
        
    else :
        print("Number is Odd")
        
def main():
    print("Enter a number : ")
    Even_or_Odd(int(input()))

if __name__ == '__main__':
    main()
