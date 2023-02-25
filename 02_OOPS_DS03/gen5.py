# Multi Level Inheritance

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
        

class t_nexon(tata):
    
    def s_rating(self):
        print("5 star safety rating")


class t_exon_type(t_nexon):
    
    def variant(self,vari):
        print(f"type of variant is : {vari}")


# c1 = t_nexon("Solid","V7","rad")
# c1.s_rating()

c2 = t_exon_type("Semi-Solid","V9","rad")
print(c2.body1)
c2.variant("Electric")