class Food:
    def __init__(self,name="Unnamed food",price=0):
        self.name=name
        self.price=price

    def print_data(self):
        print(f"the food name is {self.name} and the food price is {self.price}")
    @staticmethod
    def print_hello():
        print("Hello we are in the parent class")
    def return_data(self):
        return f"name: {self.name} price: {self.price}"

class Apple(Food):
    def __init__(self,name,price,amount=0):
        Food.__init__(self,name,price) #to inhirite the parameters
        # super().__init__(name,price)   #to inhirite the parameters
        self.amount=amount
    def tostring(self):
        return f"amount {self.amount}"

class Egg(Food):
    def __init__(self,name,price,amount):
        super().__init__(name,price)
        self.amount=amount
    def return_data(self):
        return f"the price of egg is: {self.price} and the amount is :{self.amount}"

class Checken(Egg): #we must move in the same order
    def __init__(self,name,price,amount):
        super().__init__(name,price,amount) #super from the class Egg
        #super().__init__(name) #super from the class Food

    def return_data(self):
        return f"""the checken name is {self.name} and the checken price is
{self.price} and the checken amount is:{self.amount}"""

print(Checken.mro())
obj = Food("rice",30)
obj2 = Apple("mild",50,70)
obj3 = Checken("Wight checken",35,20)
print(obj3.return_data())
# obj.print_data()
# obj2.print_data()
# print(obj2.toString())
print("is the Egg a sub class from the Food one :", issubclass(Egg,Food))

