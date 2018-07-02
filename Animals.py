class Animal(object):
    def __init__(self, name):
        super(animal, self).__init__()
        self.name = name
        self.health = 130
    def walk(self):
        print "walk"
        self.health -= 1
        return self
    def run(self):
        print "run"
        self.health -=5
        return self
    def display_health(self):
        print self.name
        print "health is:", self.health
        


animal1 = animal("Kitty")
animal1.walk().walk().walk().run().run().display_health()

class Dog(object):
    def __init__(self, name):
        super(Dog,self).__init__()
        self.health = 150
    def pet(self):
        print "pet"
        self.health += 5
        return self
dog1 = Dog("Fufu")
dog1.walk().walk().walk().run().run().pet().display_health()



# class Dragon(animal):
#     def __init__(self, name):
#         self.name = name
#         self.health = 170

#     def fly(self, -=10):
#         print self.fly
#         self.health -= 10
#         return self

#     def display_health(self):
#         print "This is a dragon", self.display_health

# dragon = Dragon("Smaug")
# dragon.fly().display_health()
