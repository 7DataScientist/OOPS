# Public Object
# _Protected Object
# __Private Object

class person2():

    def __init__(self , name ,surname , yob):
        self._name1 = name # _Protected 
        self.__surname1 = surname  # __Private  - cannot access outside the class
        self.yob1 = yob # Public



p1 = person2("Ben_gen3","John",1995)


print(p1.yob1)
# print(p1.__surname1)
print(p1._name1)