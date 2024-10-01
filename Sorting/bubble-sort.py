from typing import List


def bubbleSort(A: List[int]):
    for i in range(len(A)):
        swap = 0
        for k in range(i,len(A) -i -1 ):
            if A[k] > A[k + 1]:
                tmp = A[k]
                A[k] = A[k + 1]
                A[k + 1] = tmp
                swap = 1
        if not swap:
            break

def swap(A: List[int], x: int, y: int):
    print(A[x], A[y])
    tmp = A[x]
    A[y] = A[x]
    A[x] = tmp
num = [1,2, 3, 4,6]
print(num)
bubbleSort(num)
print(num)