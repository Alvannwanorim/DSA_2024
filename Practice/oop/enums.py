from enum import Enum
class subjects(Enum):
    ENGLISH = 1
    MATHS = 2
    PHYSICS = 3
    LAW = 4

obj = subjects.MATHS
print(obj.name)
print(obj.value)