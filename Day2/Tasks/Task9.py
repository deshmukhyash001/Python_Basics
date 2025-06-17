def main():
    print("Enter a number : ")
    k = int(input())
    
    result = "Positive" if k>0 else "Negative" if k<0 else "Zero"     
    print(result)       

if __name__ == '__main__':
    main()
