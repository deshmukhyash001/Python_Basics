def main():
    print("Enter your Marks : ")
    marks = int(input())
    
    print("Enter attendance : ")
    attendance = int(input())
    
    if marks > 50:
        print("You are no eledgible for scollership")
        
    elif marks > 70 and attendance > 65:
        print("You are eledgiblefor scollarship")

if __name__ == '__main__':
    main()
