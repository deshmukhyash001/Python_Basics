def main():
    print("Enter age : ")
    age = int(input())
    
    if age>0 and age<=13:
        print("Child")
        
    elif age>13 and age<=20:
        print("Teen")
        
    elif age>20 and age<=40:
        print("Adult")
        
    elif age>40:
        print("senior")
        
    else:
        print("Enter valid age")
    
        

if __name__ == '__main__':
    main()
