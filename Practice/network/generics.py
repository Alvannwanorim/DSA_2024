from typing import List, TypeVar, Generic
T = TypeVar('T')
def reverse(items: List[T])-> List[T]:
    return items[::-1]


nums= [1,2,3,4,5]
print(reverse(nums))

nums= ["a","b","c","d"]
print(reverse(nums))
U = TypeVar("U")

class Box(Generic[U]):
    def __init__(self, item: U) -> None:
        self.item = item
    def get_item(self):
        return self.item

box1 = Box(42)
print(box1.get_item())

box1 = Box("helo")
print(box1.get_item())

import calendar
import time
cal = calendar.month()
time.cloc