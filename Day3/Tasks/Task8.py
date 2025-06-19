def calculator(no1,operator,no2):
    if operator == "+":
        return no1+no2

    elif operator == "/":
        return no1/no2
    
    elif operator == "*":
        return no1*no2

    elif operator == "-":
        return no1 - no2

    
def main():
    print("Enter a no1 ")
    no1 = int(input())
    print("Enter operator ")
    operator = input()
    print("Enter no2 :")
    no2 = int(input())
    
    print(calculator(no1,operator,no2))

if __name__ == '__main__':
    main()
