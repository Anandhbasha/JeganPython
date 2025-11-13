class vechicle():
    def acc(self):
        print("Car Moves")
class car(vechicle):
    def brake(self):
        print("Car Stops")
class bike(car):
    def kick(self):
        print("Bike Starts")

c = bike()
c.brake()
c.acc()
c.kick()