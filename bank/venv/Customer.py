from Account import Account


class Customer:
    def __init__(self, Name, psw, addrs):
        self.__Name = Name
        self.__pass = psw
        self.__addrs = addrs

    def setName(self, Name):
        self.__lastName = Name

    def setPw(self, psw):
        self.__pass = psw

    def setAddrs(self, addrs):
        self.__addrs = addrs

    def getPw(self):
        return self.__pass

    def getAddrs(self):
        return self.__addrs

    def getName(self):
        return self.__Name

    def setAccount(self, account):
        self.__acc = Account(account)

    def getAccount(self):
        return self.__acc
