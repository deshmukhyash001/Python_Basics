def main():
    lst = [12,34,243,64,32,24,67]
    lst2 = lst
    a = max(lst2)        
    lst2.remove(a)
    print(max(lst2))

if __name__ == '__main__':
    main()
