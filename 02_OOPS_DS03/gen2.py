import logging
logging.basicConfig(filename="gen2.log",level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


# class students1():
    
#     def __init__(self, name1, age1, school1):
        
#         self.name = name1
#         self.age = age1
#         self.school = school1
        
#     def p_details(self):
        
#         print("Name of the Student is", self.name)
#         print("Age of the Student is", self.age)
#         print("School of the Student is", self.school)
        
        
class students1():
    
    def __init__(self, name1, age1):
        
        self.name = name1
        self.age = age1
        
    def p_details(self):
        
        print("Name of the Student is", self.name)
        print("Age of the Student is", self.age)
        print("School of the Student is Camb")
    

class students2():
     
    name = "Mahendra"
    age = 24
        
    def p_details(self):
        
        print(self.name)
        print(self.age) 
    
# print(dir())

# stu1 = students2()
# stu1.p_details()

# stu2 = students2()
# stu2.p_details()

# stud1 = students1("Ajay",22,"Camb")
# stud1.p_details()

# stud2 = students1("Mahendra",24,"Camb")
# stud2.p_details()

# stud3 = students1("ABC",25,"Camb")
# stud3.p_details()


# stud1 = students1("Ajay",22)
# stud1.p_details()

# stud2 = students1("Mahendra",24)
# stud2.p_details()

# stud3 = students1("ABC",25)
# stud3.p_details()


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
        logging.info(f"Name is {self.name} and age is {self.age} and ID is {self.ID_1} and Photo {self.Photo} and Number is {self.Number}")


cust1 = bank("Ajay",22,"Yes","Yes",10200)
# cust1.add_info('Yes')

# cust2 = bank("Jay",22,"Yes","No",10200)
# cust2.pt1()

print(cust1.Number)


if __name__ == "__main__":
    print(cust1.name)
    print(cust1.Photo)
    