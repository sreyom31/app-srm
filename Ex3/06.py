# A student from SRMIST has his/her money deposited Rs.15000, Rs.30000 and Rs. 40,000 in banks-CUB, HDFC and Indian Bank respectively. We have to print the money deposited by him/her in a particular bank.
# Create a class named 'Banks_SRMIST' with a function 'getBalance' which returns 0. Make its three subclasses named 'CUB', 'HDFC' and 'Indian_Bank' with a function with the same name 'getBalance' which returns the amount deposited in that particular bank. Call the function 'getBalance' by the object of each of the three banks.

class Banks_SRMIST:
    def getBalance():
        return 0
class CUB(Banks_SRMIST):
   
    def getBalance(balance):
         return balance
class HDFC(Banks_SRMIST):
   
    def getBalance(balance):
        return balance
class Indian_Bank(Banks_SRMIST):
   
    def getBalance(balance):
        return balance
Banks_SRMIST()
print(CUB.getBalance(15000))
print(HDFC.getBalance(30000))
print(Indian_Bank.getBalance(40000))