class list_met():
    
    ctype = "Takes input a list"
    
    def int_ext(self,l):
        lst1 = []
        for i in l: 
            if type(i) == int:
                lst1.append(i)
        return lst1
    
    def str_ext(self,l):
        lst1 = []
        for i in l: 
            if type(i) == str:
                lst1.append(i)
        return lst1
    
    def com_ext(self,l):
        lst1 = []
        for i in l: 
            if type(i) == complex:
                lst1.append(i)
        return lst1
    
    
# lst = list_met()

# l2 = [23, 'sdsd', 'ss ', 23.56, True, (5+6j), 4, 67, 89, 3, 6, 8, 7, "dw ", 67,98,59,79,"dwwr"]
# print(lst.int_ext(l2))
