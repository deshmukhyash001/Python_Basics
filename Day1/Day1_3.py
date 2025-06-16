class Math:
    def __init__(self,no1,no2):
        self.n1 = no1
        self.n2 = no2
        
    def add(self):
        return self.n1 + self.n2
    
    def sub(self):
        return self.n1-self.n2

    def div(self):
        return self.n1/self.n2
    
    def prod(self):
        return self.n1*self.n2
    
    def Display(self):
        print("Addition of two numbers is ",self.add())
        print("Subraction of two numbers is ",self.sub())
        print("Product of two numbers is ",self.div())
        print("Division of two numbers is ",self.prod())
        

def main():
    print("Enter a number1 : ")        
    no1 = int(input())

    print("Enter a number2 : ")
    no2 = int(input())
    math = Math(no1,no2)
    math.Display()
    

if __name__ == '__main__':
    main()
