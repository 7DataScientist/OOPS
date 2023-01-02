# Multi Label Inheritance

class bank():
    
    def transcation(self):
        print("Transaction value")

    def acc_open(self):
        print("Your account number is confidential")

    def deposite(self):
        print("Deposite value is confidential")

class HDFC(bank):
     
    def HDFC_ICICI(self):
        print("All transaction b/w HDFC and ICICI")

    def tot(self):
        print("Total from HDFC")

class ICICI(bank):
     
    def ic(self):
        print("Only details of ICICI Bank")

    def tot(self):
        print("Total from ICICI")

class CB(ICICI,HDFC):
    pass

# b1 = bank()
# b1.transcation()

# b2 = HDFC()
# b2.HDFC_ICICI()

# b3 = ICICI()
# b3.ic()

b4 = CB()

b4.tot()