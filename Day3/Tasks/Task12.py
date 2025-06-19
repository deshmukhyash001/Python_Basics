def main():
    print("Enter 1st angle of tringle")
    angle1 = int(input())
    
    print("Enter 2nd angle of tringle")
    angle2 = int(input())
    
    print("Enter 3st angle of tringle")
    angle3 = int(input())

    print("Its a triangle") if angle1+angle2+angle3 == 180 else print("It's not triangle")
    
        
if __name__ == '__main__':
    main()
