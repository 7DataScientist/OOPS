# OOPS

import logging
logging.basicConfig(filename="gen1.log",level=logging.INFO)

class students():
    pass

s1 = students()
s2 = students()

# print(s1)
# print(s2)

# s1.name = "Jorge"
# s1.age = 24


# s2.name = "John"
# s2.age = 25
# s2.schoot = "Cambridge"


# print(s1.name)
# print(s1.schoot)



class students1():
    
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def add_info(self,school):
        self.school = school

    def pt1(self):
        print(f"Name is {self.name} and age is {self.age}")

    def pt2(self):
        print(f"Name is {self.name} and age is {self.age} and school is {self.school}")


s1 = students1("Peter", 25)
s2 = students1("Tony", 35)

# s2.add_info("Cambridge")

# s2.pt2()

# print(s2.__dict__)
# print(s1.__dict__)


class bank():

    bank_name = "SBI"
    
    def __init__(self,name,age,ID_1,Photo,Number):
        self.name = name 
        self.age = age
        self.ID_1 = ID_1
        self.Photo = Photo
        self.Number = Number
    
    def add_info(self,GC):
        self.GC = GC
        print(f"Name is {self.name} and age is {self.age} and ID is {self.ID_1} and Photo {self.Photo} and Number is {self.Number} is Green Card available {self.GC}")
        logging.info(f"Name is {self.name} and age is {self.age} and ID is {self.ID_1} and Photo {self.Photo} and Number is {self.Number} is Green Card available {self.GC}")


    def pt1(self):
        print(f"Name is {self.name} and age is {self.age} and ID is {self.ID_1} and Photo {self.Photo} and Number is {self.Number}")


# p1 = bank("Peter", 25,"DL","YES",445)
# p1.pt1()


# p2 = bank("John", 25,"ADHAAR","YES",963)
# p2.pt1()

p3 = bank("Tony", 35,"DL","NO",556)
p3.add_info("GC_YES")

p3.pt1()

# print(p1.bank_name)
# print(p2.bank_name)

# p1.bank_name = "HDFC"  XXXXX

# print(p1.bank_name)
# print(p3.bank_name)
