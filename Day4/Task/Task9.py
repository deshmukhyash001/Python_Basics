def main():
    list = [78,90,67,90,45,89,56,12,34]
    k = len(list)
    
    first_half = list[:int(k/2)]
    second_half = list[int(k/2)+1:]
    
    print(first_half)
    print(second_half)
if __name__ == '__main__':
    main()
