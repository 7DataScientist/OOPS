class WDS():

  
    stu = "FS"
    _term = 23
    __students = "Data Science"
    


    def __init__(self,pet_name,age):
        self.pet_name = pet_name
        self.age = age

    def tutees(self,name="Ajay"):
        self.name = name
        # print("class of the students",)

    def inst(self):
        print("name of the student is : ",self.name)
        print("class of the students",WDS.stu)
        print("class of the students",WDS.__students)
        print(f"Pet_Name is {self.pet_name}")
        print(f"age is {self.age}")

    def to_call_pvt(self):
        print("class of the students :",WDS.__students)


s1 = WDS("Jen",25)
s1.tutees("KUMAR")

# s1.inst()

# s2 = WDS("Ben",35)
# s2.tutees("Ton")
# s2.inst()


# print(s1.stu)
# print(s1._term)
# print(s1.__students)

s1.to_call_pvt()

###############

class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
 
 
# Driver code
obj1 = Base()
print(obj1.a)