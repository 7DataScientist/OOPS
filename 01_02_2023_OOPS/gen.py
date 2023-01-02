
# def sum1(a,b):
#     c=a+b
#     print(c)

# sum1(5,4)

# Class 
class Person():

    def __init__(self,name,degree):
        self.name = name
        self.degree = degree

Ajay = Person("Ajay Kumar", "B.COM")
Kalpana = Person("Kalpana", "MSC")

# print(Ajay.name)

A = "Cat"
A_d = "BCOM"
A_p = "Bangalore"

B = "Sat"
B_d = "MSC"
B_p = "Chennai"

C = "Dat"
C_d = "BSC"
C_p = "Mysore"


class info():

    def __init__(self,name_det,degree,place):
        self.name_1 = name_det
        self.degree = degree
        self.place = place


# A_details = info("Cat","BCOM","Bangalore")
# print(A_details.name_1)


class info1():

    def __init__(my,name_det,degree,place):
        my.name_1 = name_det
        my.degree = degree
        my.place = place


# A_details = info1("Cat1","BCOM","Bangalore")
# print(A_details.name_1)

class info2():

        def __init__(self,name,degree,place,yob):
            self.name = name
            self.degree = degree
            self.place = place
            self.yob1 = yob 

        def age(self,date1):
            current_age = date1 - self.yob1
            print(current_age)


A_details = info2("Cat1","BCOM","Bangalore",1995)

# print(A_details.yob)
# A_details.age(2022)

# A_details.age(2030)


# def age(date1):
#     current_age = date1 - 1995
#     print(current_age)

# age(2022)

class val1():

    def __init__(self,age,place):
        self.age = age
        self.place = place

    def name1(self,name1):
        print("your name :",name1)
        self.name1 = name1

    def email(self):
        em = input("Enter your email :")
        print("your email :",em)
        self.em = em

    def det(self):
        print(f"Your name {self.name1}, email is {self.em}, age is {self.age} and place is {self.place}")

# person1 = val1()
# print(person1)

# person1.name1("7D")
# person1.email()
# person1.det()

# p1 = val1(27,"Bangalore")
# p1.name1("7D")
# p1.email()

# p1.det()


class val2():

    def __init__(self,name,place,pin:int):
        self.name = name
        self.place = place
        self.pin = pin

    def det_1(self):
        print(f"name is {self.name} and place is {self.place} and age is 45 and pin id {self.pin}")

# p2 = val2("7D","Bangalore",45)
# p2.det_1()

# print(type(p2.pin))

class lst():

    def __init__(self,l):
        self.l = l

    def odd1(self):
        j = []
        for i in self.l:
            if i %2 != 0:
                j.append(i)
        return j

    def even1(self):
        j = []
        for i in self.l:
            if i %2 == 0:
                j.append(i)
        return j
        
# l1 = lst([1,2,3,4,5,6,7,8,9])

# print(l1.odd1())
# print(l1.even1())


# 1 - All excersies we have completed w.r.t list,tuple,dict convert then into classes
# 2 - Exception handling
# 3 - use Loggging