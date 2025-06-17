PI = 3.14
def area_of_circle(radi):
    return PI*(radi**2)

def main():
    print("Enter a radius: ")
    k = area_of_circle(int(input()))
    print(k)

if __name__ == '__main__':
    main()
