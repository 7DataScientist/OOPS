# Polymorphism

class gen():

    def tes(self,a,b):
        c = a + b
        print(c)


a = gen()
b = gen()

# a.tes(5,6)
# b.tes("abc","def")

# Abstraction

from abc import ABC, abstractmethod 

class shape(ABC):

    def __init__ (self, shapeType):

        """
        Objective: To initialize object of class Shape Input Parameters:
        self (implicit parameter) - object of type Shape
        shapeType - string
        Return Value: None
        """

        self.shapeType = shapeType

    @abstractmethod 
    def area(self) :
        pass

    # @abstractmethod
    # def perimeter (self):
    #     pass


class Rectangle(shape):

    def __init__(self, length, breath):

        """
        Objective: To initialize object of class Rectangle Input Parameters: self
        (implicit parameter) – object of type Rectangle length, breadth – numeric value 
        Return Value: None 
        """

        shape.__init__(self, "Rectangle")

        self.length = length
        self.breath = breath

    
    def area(self):

        """
        Objective: To compute area of the Rectangle Input Parameter: 
        self (implicit parameter) object of type Rectangle
        Return Value: numeric value 
        """

        return self.length * self.breath


# rectangle = Rectangle (30, 15)
# print(rectangle.area ())

###########################################

from abc import ABC, abstractmethod
 
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):
        pass

    @abstractmethod
    def noofpoints(self):
        pass
 
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

    def noofpoints(self):
        print("I have 3 connecting points")
        

class Pentagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
 
class Hexagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")
 
class Quadrilateral(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")

    def noofpoints(self):
        print("I have 4 connecting points")
 
# Driver code
# R = Triangle()
# R.noofsides()
# R.noofpoints()
 
# K = Quadrilateral()
# K.noofsides()
# K.noofpoints()
 
# R = Pentagon()
# R.noofsides()
 
# K = Hexagon()
# K.noofsides()

############################

# Encapsulation

class WDS():

    public1 = "Public _ FS"
    _protected1 = "Protected _ 23"
    __private1 = "Private _ Data Science"
    
    def __init__(self,pet_name,age):
        self.pet_name = pet_name
        self.age = age

    def to_call_pub(self):
        print("class of the public :",WDS.public1)
        print("class of the protected :",WDS._protected1)
        print("class of the private :",WDS.__private1)

    

    def gen(self):
        print("Attributes ",self.pet_name)
        print("Attributes ",self.age)
        print("class of the public :",WDS.public1)
        print("class of the public :",self.public1)

    def gen1(self):
        print("Attributes ",self.pet_name)
        print("Attributes ",self.age)
        print("class of the protected :",WDS._protected1)
        print("class of the protected _ Self :",self._protected1)

    
    def gen2(self):
        print("Attributes ",self.pet_name)
        print("Attributes ",self.age)
        print("class of the private :",WDS._protected1)
        print("class of the private _ Self :",self._protected1)



s1 = WDS("Tom",25)
s2 = WDS("Can",35)


# print(s1.stu)
# print(s1._term)
# print(s1.__students)

# s1.to_call_pub()
# s1.public1 = "Public _ FS Changed"
# s1.to_call_pvt()

# print("#####################")


# s1.to_call_pvt()
# WDS.public1 = "Public _ FS Changed"
# s1.to_call_pvt()


# s1.gen()
# s2.gen()

# s1.public1 = "Public _ FS Changed"

# print("#####################")

# s1.gen()
# s2.gen()

###############

s1.gen1()
s2.gen1()

WDS.__private1 = "Private _ Data Science Changed"

print("#####################")

s1.gen1()
s2.gen1()