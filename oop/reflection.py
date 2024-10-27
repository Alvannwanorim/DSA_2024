from typing import Any


class Test:
    def __init__(self) -> None:
        pass
    # def __call__(self, *args: Any, **kwds: Any) -> Any:
    #     print("hello")

obj = Test()
obj()
# print(issubclass(int,object))
# print(issubclass(str,object))
# print(issubclass(complex,object))
# print(issubclass(Test,object))
print(callable(obj))