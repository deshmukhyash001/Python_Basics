def main():
    print("Enter marks : ")
    marks = float(input())
    
    if marks<100 and marks>=90:
        print("Distincion")
        
    elif marks<90 and marks >=70:
        print("First class")
        
    elif marks <70 and marks >=50:
        print("Second class")        

    elif marks <50 and marks >=40:
        print("Pass class")
    
    elif marks<40 and marks >=0:
        print("Fail")
        
    else:
        print("Enter valid Marks")

if __name__ == '__main__':
    main()
