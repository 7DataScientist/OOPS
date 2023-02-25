# class person1():
    
#     def __init__(self, name,surname, yob):
#         self.name = name
#         self.surname = surname
#         self.yob = yob
        
#     def info(self):
        
#         print(f"Name is {self.name}")
#         print(f"Sur-Name is {self.surname}")

# a1 = person1("Ajay","Kumar",1996)
# a2 = person1("Vijay","Bhaskar",1999)

# print(a1.surname)
# print(a2.surname)

# a1.info()

# ----------------------------------------

# Public Object
# _Protected Object  
# __Private Object   
class person1():
    
    def __init__(self, name,surname, yob):        
        self._name = name                        # _Protected Object  
        self.__surname = surname                 # __Private  - cannot access outside the class
        self.yob = yob                           # Public Object
        
    def info(self):
        
        print(f"Name is {self.name}")
        print(f"Sur-Name is {self.surname}")

p1 = person1("Ben_gen3","John",1995)



print(p1.yob)
# print(p1.__surname)
print(p1._name)

