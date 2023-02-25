class car():
    
    def __init__(self,body,engine,tyre):
        self.body1 = body
        self.engine1 = engine
        self.tyre1 = tyre
        
    def egn(self):
        print(f"Type of engine is {self.engine1}")
    

class tata(car):
    
    def brand(self):
        print("TATA")
        

class MS(car):
    
    def brand(self):
        print("MS")
    
    


# c1  = car("solid","V7","rad")
# c1.egn()
    
c2 = tata("Semi-Solid","V9","Cir")

c2.egn()
c2.brand()


c3 = MS("Liquid","V9","Simo - Cir")

c3.egn()
c3.brand()
