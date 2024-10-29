from abc import ABC, abstractmethod
class democlass(ABC):
    @abstractmethod
    def method1(self):
        print("Abstract method")
        return 
    def method2(self):
        print("concrete method ")
    
class concreteclass(democlass):
    def method1(self):
        return super().method1()

obj = concreteclass()
obj.method1()
obj.method2()
    