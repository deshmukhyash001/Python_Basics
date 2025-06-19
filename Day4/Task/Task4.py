import random

def main():
    list = []
    for number in range(10):
        k = random.randint(20,30)        
        list.append(k)
    print(list)
    
if __name__ == '__main__':
    main()
