def main():
    arr1 = [
        [1,2,3,4,5],
        [5,4,3,2,1]
    ]
    arr2 = [
        [6,7,8,9,0],
        [0,9,8,7,6]
    ]
    
    new_arr = [[],[]]
    
    for i in range(len(arr1)):
        for k in range(len(arr1[i])):
            new_arr[i].append(arr1[i][k]+arr2[i][k])
            
    print(new_arr)
            

if __name__ == '__main__':
    main()
