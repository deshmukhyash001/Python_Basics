def main():
    print("Enter User Name : ")
    a = input()
    
    print("Enter Password : ")
    b = input()
    
    usernames_and_password = {
        "yash": "yash@1234",
        "aditya" : "aditya123",
        "mayur" : "mkdir1234"
    }

    if a in usernames_and_password:
        
        if usernames_and_password[a] == b:
            print("Login successful")
        else :
            print("Login denied")    
    

if __name__ == '__main__':
    main()
