class car():

    def __init__(self,body,engine,tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre

    def milage(self):
        print("Mileage of the car")


c1 = car("Solid","V7","rad")

print(c1.body)
print(c1)
print(c1.__dict__)

# Child Class

class tata(car):

    def brand(self):
        print("TATA")

c2 = tata("Semi-Solid","V12","Axil")
print(c2.engine)

class Hyundai(car):
    pass

c3 = Hyundai("sld","V2","Round")
