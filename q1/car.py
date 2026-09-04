class Car:
  def __init__(self, brand, model, battery=35):
    self.brand = brand
    self.model = model 
    self.__battery = battery
  def go(self, distance):
    self.__battery -= distance/20
    print("You traveled",distance)
    print("You have",self.__battery,"wH left")
  def charge(self, wH):
    self.__battery += wH
    print("You recharged with",wH,"wH")

car = Car("Geely", "EX5")
while car.battery > 0:
  act = input("What do we do? (g or c) ")
  if act == "g":
    distance = int(input("How far? "))
    car.go(distance)
  elif act == "c":
    wH = int(input("How much to charge? "))
    car.charge(wH)
  else:
    print("Invalid action")
print("Game over, you ran out of batteries")
