def main():
    print("Enter a colour")
    color = input()
    
    if color == "Red":
        print("It indicates that you should stop behinf=d zebra crossing until signal is red") 
        
    elif color.lower() == "green " or color.lower() == "blue":
        print("You should move no need to stop ")
        
    elif color.lower() == "yellow":
        print("Wither you can go forwerd of stop depending on road condions ")  
        
    else:
        print("Enter valid traffic color or \ncheck spelling colour you entered")    
        

if __name__ == '__main__':
    main()
