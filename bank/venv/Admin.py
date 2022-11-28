class Admin:
    def __init__(self, name, pwd: int):
        self.__name = name
        self.__pwd = pwd
    def getName(self):
        return self.__name
    def getPwd(self):
        return self.__pwd