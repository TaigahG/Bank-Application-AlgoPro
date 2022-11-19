import string
import random
class Bank:
    def __init__(self):
        self.blnc = 0
        self.amnt = 0
        self.previousTransaction = 0
        self.option = ''
        self.Fname = ''
        self.Lname = ''
        self.rslt = ''
        self.num = 0
        self.acc = {}
    def deposit(self, amnt):
        self.blnc += self.amnt
        self.previousTransaction = self.amnt
        balance = {'balance':self.blnc}
        self.acc.update(balance)
    def withdraw(self, amnt):
        self.blnc -= self.amnt
        self.previousTransaction = -self.amnt
    def getPreviousTransaction(self):
        if self.previousTransaction > 0:
            print("you deposit: ", self.previousTransaction)
        elif self.previousTransaction < 0:
            print("you withdraw: ", self.previousTransaction)
        else:
            print("there is no transaction")
    def AccountRegis(self):
        self.Fname = input("Enter your first name: ")
        self.Lname = input("Enter yout last name: ")
        ltr = string.ascii_letters + string.digits
        for i in range(8):
            self.rslt += random.choice(ltr)
        self.acc['account'] = [self.Fname, self.Lname]
        self.acc['id'] = [self.rslt]
        self.acc['balance'] = self.blnc

    def ShowMenu(self):
        global nm
        print("------------------------------------------")
        print("Welcome to our bank")
        print("------------------------------------------")
        print("A. Balance")
        print("B. Deposit")
        print("C. Withdraw")
        print("D. Previous Transaction")
        print("E. Account Registration")
        print("F. Account Infromation")
        print("G. Exit")

        while self.option != 'g':
            self.option = input("Select an option: ")
            if self.option == 'a':
                print("Your balance is: ", self.blnc)
            elif self.option == 'b':
                try:
                    self.amnt = int(input("enter the ammount of money you want to deposit:"))
                    self.deposit(self.amnt)
                except ValueError:
                    print("Not valid")
            elif self.option == 'c':
                try:
                    self.amnt = int(input("enter the ammount of money you want to withdraw:"))
                    self.withdraw(self.amnt)
                except ValueError:
                    print("Not valid")
            elif self.option == 'd':
                self.getPreviousTransaction()
            elif self.option == 'e':
                self.AccountRegis()
            elif self.option == 'f':
                print("Here is your account info: ", self.acc)
            elif self.option == 'g':
                break
            else:
                print("option invalid")
        print("Thank you for using our service")

b = Bank()
b.ShowMenu()





