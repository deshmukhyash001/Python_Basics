def main():
    
    list = [78,90,67,90,45,89,56,12,34]
    
    for itm in list:
        if itm & 1 == 0:
            print(list.index(itm))

if __name__ == '__main__':
    main()
