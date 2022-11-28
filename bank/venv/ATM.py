from Account import Account
from Customer import Customer
from Bank import Bank
import sys
import string
import random
class ATM:
    def __init__(self):
        self.__numOfUser = 0
        self.__name = ''
        self.__cus = {}
        self.__admnLog = {"12345": "Admin"}
        self.__amount = 0
        #self.__key = key
    def addUser(self, Name, psw, addrs, pin: str):
        self.__cus.update({pin: Customer(Name, psw, addrs)})
        # self.__cus.append(Customer(Name, psw, addrs))
        self.__numOfUser += 1
    def getUser(self, pin: str):
        return self.__cus[pin]
    def AccoutDetail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {atm.getUser(self.__name).getName().upper()}")
        print(f"Account Addres: {atm.getUser(self.__name).getAddrs()}")
        print("----------------------------------\n")
        #print(f"Available balance: Rp.{atm.CheckBlnc()}\n")
    def Deposit(self):
        p = int(input("Enter amount you want to deposit: "))
        atm.getUser(self.__name).getAccount().deposit(p)
    def Withdraw(self):
        self.__p = int(input("Enter amount you want to withdraw: "))
        atm.getUser(self.__name).getAccount().withdraw(self.__p)
    def CheckBlnc(self):
        return atm.getUser(self.__name).getAccount().getBalance()
    def addUserDetail(self):
        Name = input("Enter your name: ")
        psw = int(input("Make your pin: "))

    def transaction(self):
        print("""
                  TRANSACTION 
              *********************
                  Menu:
                  1. Account Detail
                  2. Check Balance
                  3. Deposit
                  4. Withdraw
                  5. Exit
              *********************
              """)
        option = ''
        while option != "6":
            option = input("Select an option: ")
            if option == "1":
                atm.AccoutDetail()
            elif option == "2":
                print("Your balance is: ", atm.CheckBlnc())
            elif option == "3":
                atm.Deposit()
            elif option == "4":
                atm.Withdraw()
            elif option == "5":
                self.__name = ''
                cn = input("Are you sure want to exit? y/n ")
                if cn == "y":
                    atm.Start()
                elif cn == "n":
                    atm.transaction()
                atm.Start()
            else:
                print("It is not on the option")


    def Register(self):
        Name = input("enter your name: ")
        psw = int(input("Create your pin:"))
        addrs = ''
        ltr = string.ascii_letters + string.digits
        for i in range(8):
            addrs += random.choice(ltr)
        print("Account created succesfully \n")
        atm.addUser(Name, psw, addrs, str(psw))
        atm.getUser(str(psw)).setAccount(0)
        atm.Admin()
    def RemoveUser(self):
        nm = input("Enter the user name: ")

        if self.__cus.get(nm) is not None:
            self.__cus.pop(nm)
            self.__numOfUser -= 1
        else:
            print(f"There is no user with the name {nm}")

    def AdminLogin(self):
        nm = input("Enter admin pass: ")

        if nm in self.__admnLog:
            atm.Admin()
        else:
            print("\nWrong password, please try again\n")
            cn = input("Try Again? y/n ")
            if cn == "y":
                atm.AdminLogin()
            elif cn == "n":
                atm.Start()
            else:
                print("Error")

    def Admin(self):
        print("""
                  ADMIN MENU 
              *********************
                  Menu:
                  1. Add User
                  2. Remove User
                  3. Exit
              *********************
              """)
        opt = ''
        while opt != "4":
            opt = input("Select an option: ")
            if opt == "1":
                atm.Register()
            if opt == "2":
                atm.RemoveUser()
            if opt == "3":
                atm.Start()

    def Login(self):
        name = input("enter your name: ")
        pin = int(input("enter your pin: "))
        if self.__cus.get(str(pin)) is not None:
            atm.getUser(str(pin))
            self.__name += str(pin)
            atm.transaction()
        else:
            print(f"\nLogin failed, please check again your password or usename\n")
            cn = input("Try again? y/n ")
            if cn == "y":
                atm.Login()
            elif cn == "n":
                atm.Start()
            else:
                print("Error")
    def Start(self):
        print("         *******WELCOME TO BANK OF INDONESIA*******")
        # print("___________________________________________________________\n")

        while True:
            print("""
                          MENU 
                  *********************
                      Menu:
                      1. Customer
                      2. Admin
                      3. Exit
                  *********************
                  """)
            opt = input("Enter an option: ")
            if opt == "1":
                atm.Login()
            elif opt == "2":
                atm.AdminLogin()
            elif opt == "3":
                print("Thank you")
                sys.exit()

atm = ATM()






