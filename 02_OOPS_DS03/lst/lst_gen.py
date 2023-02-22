class list_met():
    
    ctype = "Takes input a list"
    
    def int_ext(self,l):
        lst1 = []
        for i in l: 
            if type(i) == int:
                lst1.append(i)
        return lst1
    
    def str_ext(self,l):
        lst1 = []
        for i in l: 
            if type(i) == str:
                lst1.append(i)
        return lst1
    
class cal():

    def sum1(self,a,b):
        v = a + b
        return v
        
    def sub1(self,a,b):
        v = a - b
        return v
        
    def mul1(self,a,b):
        v = a * b
        return v   
    

