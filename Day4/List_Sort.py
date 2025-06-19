def main():
    list = [12,23,453,64,64,45,32,13,7] 
    print("All list itm",list[::-1],"\n")    
    
    print("Even in list")
    for itm in list:
        if itm & 1 == 0:
            print(itm,end=",")
    print("\n\nOdd in list")
    for itm in list:
        if itm & 1 == 1:
            print(itm,end=",")
    print()

if __name__ == '__main__':
    main()
