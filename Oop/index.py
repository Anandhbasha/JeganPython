# car1_milage = 20
# car1_cc = 1200
# car1_wheels =4
# car1_airbags = 5
# car1_cam = 2

# def acc():
#     print("Car1 Moves")
# def breaks():
#     print("car1 Stopss")


# car2_milage = 20
# car2_cc = 1200
# car2_wheels =4
# car2_airbags = 5
# car2_cam = 2

# def acc():
#     print("Car2 Moves")
# def breaks():
#     print("car2 Stopss")



class Cars:
    car_milage = 0
    car_cc = 0
    car_wheels =4
    car_airbags = 5
    car_cam = 2
    car_Name = "Honda"

    def acc(self,name):
        self.name = name
        print(f"{name} Moves")
    def breaks(self):
        print("car Stopss")
    

c1 = Cars()
c2 = Cars()

print(c1.car_milage)
c1.car_milage=25
print(c1.car_milage)
print(c2.car_milage)
c2.car_milage=20
print(c2.car_milage)
c1.acc("BMW")
c2.acc("Benz")


class Bank:
    #when opens a account
    def _init_(self, name, money=0):
        self.name = name     #to store the given name inside the object
        self.money = money   #to store the given money
#output:priya 5000
#       ravi 3000
    def add(self, x):
        self.money += x
        print(f"{self.name}: +₹{x} → ₹{self.money}")
#output:priya 5000 + 2000 =7000
#       ravi 3000 + 5000 =8000

    def withdraw(self, x):
        if x > self.money:
            print(f"{self.name}: Insufficient balance! ₹{self.money} only")
        else:
            self.money -= x
            print(f"{self.name}: -₹{x} → ₹{self.money}")
#output:priya 7000-500=6500
#       ravi  8000-800=7200

    def emi(self, loan, rate=10, months=12):
        r = rate / 12 / 100
        return round(loan * r * (1 + r)*months / ((1 + r)*months - 1), 2)

# SavingsAccount inherits from Bank
class SavingsAccount(Bank):
    def withdraw(self, x):
        print("Savings Account Transaction:")
        super().withdraw(x)

# Creating account
a1 = SavingsAccount("Priya", 5000)
b1 = SavingsAccount("Ravi", 3000)

print(a1.name, a1.money)  
print(b1.name, b1.money)    

# Deposit 
a1.add(2000)
b1.add(5000)

# Withdraw 
a1.withdraw(500)
b1.withdraw(800)
b1.withdraw(9000)

# EMI 
print(f"Priya's EMI: ₹{a1.emi(50000)}")
print(f"Ravi's EMI: ₹{b1.emi(60000)}")
