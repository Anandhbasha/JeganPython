from abc import ABC,abstractmethod
class paymentGateway(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    def gpay(self,amount):
        pass
    def phonepe(self,amount):
        pass