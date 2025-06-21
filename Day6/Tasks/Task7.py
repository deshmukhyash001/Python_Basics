def main():
    arr1=[
        [1,2,3,4,5,6,7,6],
        [4,2,4,3,5,2,4,4],
        [23,43,23,542,23]
    ]        
    maxx = 0
    for k in arr1:
        if max(k) > maxx:
            maxx = max(k)
    
    print(maxx)

if __name__ == '__main__':
    main()
