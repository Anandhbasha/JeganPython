class BankBalance:
    __balance = 0 #private variable

    def addMoney(self,amount):
        if amount >0:
            self.__balance +=amount
        else:
            print("enter the correct amount")
    
    def debMoney(self,amount):
        if amount > 0 and amount <=self.__balance :
            self.__balance -=amount
        else:
            print("enter the correct amount")
        
    def showBalance(self):
        return self.__balance
acc1 = BankBalance()
acc1.addMoney(500)
acc1.debMoney(150)
# print(acc1.__balance)
print(acc1.showBalance())
