from abc import ABC,abstractmethod
class paymentGateway(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class gpayGateway(paymentGateway):
    def pay(self,amount):
        print("Paid",amount)
class phonepeGateway(paymentGateway):
    def pay(self,amount):
        print("Paid:",amount)

gpay = gpayGateway()
gpay.pay(600)