class Vehicle:
    def drive(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def drive(self):
        print("The car is driving smoothly on the road")

v = Vehicle()
v.drive()
c = Car()
c.drive()
