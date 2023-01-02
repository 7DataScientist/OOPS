# Multi Level Inheritance

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

class ICICI(HDFC):
     
     def ic(self):
        print("Only details of ICICI Bank")

b1 = bank()
b1.transcation()

b2 = HDFC()
b2.HDFC_ICICI()

b3 = ICICI()
b3.ic()


