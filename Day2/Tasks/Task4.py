
def largenst_among_3(no1,no2,no3):
    
    if no1 > no2 and no1 > no3:
        return f"number {no1} is greatest"
    
    elif no2 > no1 and no2 > no3:
        return f"number {no2} is greatest"
    
    elif no3 > no1 and no3 > no2:
        return f"number {no3} is greatest"
    
def main():
    
    print("Enter three numbers : ")
    no1,no2,no3 = int(input()),int(input()),int(input())
    
    k = largenst_among_3(no1,no2,no3)      
    
    print(k) 

if __name__ == '__main__':
    main()
