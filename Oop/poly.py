#method overloading
class calculator:
    def add(self,a=0,b=0,c=0):
        return a+b+c
    
cal = calculator()
print(cal.add(20,30,40))
print(cal.add(20,30))
print(cal.add(20))
print(cal.add())


# method overriding
class Restarunt:
    def order(self):
        print("Order placed from genral res")
class vegRes(Restarunt):
    def order(self):
        print("Order placed from Veg res")
class NvRes(Restarunt):
    def order(self):
        print("Order placed from NvRes res")


nv = NvRes()
nv.order()
v = vegRes()
v.order()