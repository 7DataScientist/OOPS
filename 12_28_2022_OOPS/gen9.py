class WDS():

    __students = "Data Science"
    stu = "FS"

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

s1 = WDS("Jen",25)
s1.tutees("KUMAR")

s1.inst()

s2 = WDS("Ben",35)
s2.tutees("Ton")
s2.inst()


# print(s1.stu)
# print(s1.__students)