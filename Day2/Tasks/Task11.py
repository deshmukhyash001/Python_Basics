def main():
    
    print("Enter 3 subject marks : ")
    a,b,c = int(input()),int(input()),int(input())    
    
    # Assuming student will enter each mark out of 100 
    
    print(((a+b+c)/(100*3))*100) 

if __name__ == '__main__':
    main()
