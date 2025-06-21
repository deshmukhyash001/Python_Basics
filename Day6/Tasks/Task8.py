def main():

    arr1 = [
        [1,2,3,4,5],
        [5,4,3,2,1]
    ]        
    add = 0
    for i in arr1:
        for k in i:
           add += k
           
    print(add) 

if __name__ == '__main__':
    main()
