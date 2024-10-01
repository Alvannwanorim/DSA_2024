from typing import List


def insertionSort(num:List[int]):
    for i in range(1, len(num)):
        temp = num[i]
        j = i
        while j > 0 and num[j-1] > temp:
            print(num)
            num[j] = num[j-1]
            print(num)
            j -= 1
        num[j] = temp

num = [9, 8, 6, 1, 4, 5,3,7, 2]
insertionSort(num)
print(num)
    