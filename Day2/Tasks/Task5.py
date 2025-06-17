def divisible_by_5_7_3(num):
    
    if num % 5==0 or num % 7==0 or num% 3 == 0:
        return " Number is devisible either by 5,7 or 3"
    
    return " not divisible "
    
def main():
    print("Enter a number : ")
    k = divisible_by_5_7_3(int(input()))
    print(k)
    
if __name__ == '__main__':
    main()
