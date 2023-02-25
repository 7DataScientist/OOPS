# Multi Label Inheritance

class car():
    
    def __init__(self,body,engine,tyre):
        self.body1 = body
        self.engine1 = engine
        self.tyre1 = tyre
        
    def egn(self):
        print(f"Type of engine is {self.engine1}")
    

class safety_rating():
    
    def s_rating(self,rating):
        print(f"{rating} star safety rating")
        
class dep_check():
    
    def s_rating(self,rating):
        print(f"{rating} star safety rating required for govt clearence")
        
    def poll_lev(self,lev):
        print(f"pollution level is {lev}")
    
    
        
        
class tata(car,safety_rating,dep_check):
    
    def brand(self):
        print("TATA")
        
class MS(car,dep_check,safety_rating):
    
    def brand(self):
        print("MS")

c1 = tata("Semi-Solid","V9","Cir")
c1.brand()
c1.s_rating(5)
c1.poll_lev(0.5)


c2 = MS("Semi-Solid","V5","Cir")
c2.brand()
c2.s_rating(4)
c2.poll_lev(0.9)