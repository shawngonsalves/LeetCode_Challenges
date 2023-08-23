class Item:
    all = []
    def __init__(self, name, price, quantity):
        
        print("I am created! ", name)
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
        
    def calculate(self, x, y):
        return x * y
    
item1 = Item("Phone",20, 5)


item2 = Item("Laptop", 200,4)

for instance in Item.all:
    print(instance.name)


