class Singleton:
    __uniqueInstance = None

    @staticmethod
    def createInstance():
        if Singleton.__uniqueInstance == None:
            Singleton()
        return Singleton.__uniqueInstance
    
    def __init__(self) -> None:
        if Singleton.__uniqueInstance != None:
            raise Exception("Objec exists!")
        else:
            Singleton.__uniqueInstance = self
        
obj1 = Singleton.createInstance()
print(obj1)
obj2 =  Singleton.createInstance()
print(obj2)
