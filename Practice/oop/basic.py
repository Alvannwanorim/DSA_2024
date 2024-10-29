class Employee:
    def __init__(self, name, age) -> None:
        self.__name = name 
        self.__age = age 
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def set_name(self,name):
        self.__name = name 
        return
    
    def set_age(self,age):
        self.__age = age 
        return
    
    age = property(get_age,set_age, "name")
    name = property(get_name,set_name, "age")

emp = Employee("Alvan", 29)
print("Name ", emp.name, "age: ", emp.age)
emp.name = "Igwe"
emp.age = 31

print("Name ", emp.name, "age: ", emp.age)
