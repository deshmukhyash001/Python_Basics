def isprime(num):
    
    if num<=1:
        return True

    for check in range(num-1,1,-1):
        if num % check == 0:
            return False
            break
        
    else :
        return True
def main():
    list = [12,23,453,64,64,45,32,13,7] 
    for i in list:
        if isprime(i):
            print(f"Number {i} is Prime")
        
        else:
            print(f"Number {i} is not Prime")
                

if __name__ == '__main__':
    main()
