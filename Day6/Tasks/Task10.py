def main():
    arr1=[
        [1,2,3,4,5,6,7,6],
        [4,2,4,3,5,2,4,4],
        [2,3,43,23,542,23]
    ]
    
    for i in arr1[0]:
        if i in arr1[1] and i in arr1[2]:
            print(i)

if __name__ == '__main__':
    main()
