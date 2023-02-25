class WDS():
    
    __students = "Data Science"  # Private
    stu = "FSDS1"                   # Public
    
    def __init__(self,pet_name,age):
        self.pet_name = pet_name
        self.age = age
        
    def tutees(self,name="Aj"):
        self.name = name
        print(f"First name is {name}")
        print(f"Pet_name is {self.pet_name}")
        
    def info(self):
        print(self.name)
        print("class of the students", self.stu)
        print("class of the students", WDS.stu)
        print("class of the students", self.__students)
        print("class of the students", WDS.__students)
        
        
s1 = WDS("Jen",25)
# print(s1.age)

s2 = WDS("Fen",27)

# print(s1.__dict__)

# s1.tutees("Ten")
# s1.info()

# print(s1.__dict__)

# print(s1.stu)
# print(s1._WDS__students)
# print(s1.__dict__)

# print("-----------------------")

# print(s2.stu)
# print(s2._WDS__students)
# print(s2.__dict__)

# s2.age = 28

# print("-----------------------")

# # print(s2.stu)
# # print(s2._WDS__students)
# print(s2.__dict__)

s2.stu = "FSDS_S2"

# print("-----------------------")

# print(s2.stu)
# print(s2._WDS__students)
# print(s2.__dict__)

print("-----------------------")
print(s1.stu)
print(s2.stu)

s2.__students = "Data"

print("-----------------------")
print(s1.stu)
print(s2.stu)