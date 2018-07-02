class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        self.sold = False
        self.display_info()
    def sell(self):
        if self.sold == True:
            print "Item is sold", self.item_name
        else:
            print "Item is for sale", self.item_name
        return self
    def addTax(self, tax):
        self.tax = tax
        self.cost = self.price + (self.price * tax)
        self.cost = self.cost + (self.cost * self.tax)
        return self
    def Return(self, reason):
        self.reason = reason
        if reason == "defective":
            self.price = 0
            self.cost = 0
        elif reason == "In box":
            self.cost = self.cost
        elif reason == "Open box":
            self.cost == self.cost - (self.price * "20%")
        return self
    def __str__(self):
        return "Item price: {} Item Name: {} Weight: {} Brand: {} Cost: {}"
        self.price
        self.item_name
        self.weight
        self.brand
        self.cost
        print product1.sell().addTax("12%").Return("defective")
        print product2.sell().addTax("12%").Return("In box")
        print product3.sell().addTax("12%").Return("Open box")
        print product4.sell().addTax("12%")
        product1 = Product(14, "dog food", 30, "Max Frontier", 14)
        product2 = Product(4, "cat food", 12, "Whiskers", 4)
        product3 = Product(11, "hamster food", 3, "Happy Hamster", 11)
        product4 = Product(7, "dog ball", 12, "Kong", 7)
        

