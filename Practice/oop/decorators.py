def decorator_function(Wrapped):
    class Wrapper:
        def __init__(self, x) -> None:
            self.wrap = Wrapped(x)
        
        def print_name(self):
            return self.wrap.name 
    return Wrapper

@decorator_function
class Wrapped:
    def __init__(self,x) -> None:
        self.name = x 

obj = Wrapped("Alvan")
print(obj.print_name())