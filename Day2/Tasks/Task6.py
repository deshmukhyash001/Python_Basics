def area_of_circle(radi):
    Pi = 3.14
    return Pi*(radi**2)

def main():
    print("Enter a radius: ")
    k = area_of_circle(int(input()))
    print(k)

if __name__ == '__main__':
    main()
