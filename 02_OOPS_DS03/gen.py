def sum1(a,b):
    v = a + b
    print(v)
    
sum1(5,6)

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


# a = cal()
# print(type(a))

# Explaination S -----------

# name = "Ajay"
# print(type(name))

# Explaination E -----------

a = cal()


multi = a.mul1(5,4)
print(multi)

subtrat = a.sub1(6,8)
print(subtrat)


