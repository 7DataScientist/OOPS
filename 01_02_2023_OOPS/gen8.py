# Method Overriding

class fuel():

    def petrol(self):
        print("Petrol for Vehicles")

    def diesel(self):
        print("Deisel for Cars")

class air_fuel(fuel):

    def petrol(self):
        print("White Petrol for Aero-Planes")

f = air_fuel()
f.petrol()

f1 = fuel()
f1.petrol()