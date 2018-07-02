class Car(object): 
	def __init__(self, price, speed, fuel, mileage): 
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax
		self.tax()
		self.display_all()

	def tax(self): 
		if self.price >= 10000: 
			self.tax = "15%"
		else: 
			self.tax = "12%"

	def display_all(self): 
		print "Price is:", self.price
		print "Speed is:", self.speed
		print "Fuel is:", self.fuel
		print "Mileage is:", self.mileage
		print "Tax is:", self.tax

car1 = Car(5000, "35mph", "full", "15mpg")
car2 = Car(2000, "45mpg", "not full", "105mpg")
car3 = Car(7000, "55mpg", "kind of full", "95mpg")
car4 = Car(8500, "25mpg", "full", "25mpg")
car5 = Car(20000, "30mpg", "full", "55mpg")
car6 = Car(9000, "50mpg", "empty", "60mpg")