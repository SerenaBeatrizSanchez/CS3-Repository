#DEPENDENCY
class Sauce:
    def __init__(self,name,taste):
        self.name = name; self.taste = taste
        print(self.name,"is ready")
    def __del__(self):
        print(self.name, "is ubos na")

class Tusoktusok:
    def __init__(self,name,sauce = None):
        self.name = name
        self.sauce = sauce
        print(self.name,"is cooked")
        if self.sauce != None:
            print("It is dipped in",self.sauce.name)
    def eat(self):
        print("I am eating",self.name)
        if self.sauce != None:
            print("It tastes",self.sauce.taste)
    def dip(self,sauce):
        self.sauce = sauce
        print(self.name,"was dipped in",self.sauce.name)
    def __del__(self):
        print(self.name,"was thrown in the trash can")

hotsauce = Sauce("Hot sauce", "spicy")
fishball = Tusoktusok("fishball", hotsauce)
fishball.eat()
kikiam = Tusoktusok("kikiam")
kikiam.eat(); kikiam.dip(hotsauce); kikiam.eat()
