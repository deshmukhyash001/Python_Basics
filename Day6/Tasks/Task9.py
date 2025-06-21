def main():
    arr1=[
        [1,2,3,4,5,6,7,6],
        [4,2,4,3,5,2,4,4],
        [23,43,23,542,23]
    ]             
    
    for i in range(len(arr1)):
        arr1[i] == reversed(arr1[i]) 
        
    print(list(reversed(arr1)))

if __name__ == '__main__':
    main()
