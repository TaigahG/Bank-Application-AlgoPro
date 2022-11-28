from Customer import Customer
class Bank:
    def __init__(self,bName):
        self.__bName = bName
        self.__customer = []
        self.__numOfCustomer = 0
    def addCustomer(self,fName,lName):
        self.__customer.append(Customer(fName,lName))
        self.__numOfCustomer += 1
    def getCustomer(self,index):
        return self.__customer[index]
    def getNumCustomer(self):
        return self.__numOfCustomer