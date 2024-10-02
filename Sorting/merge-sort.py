from typing import List


def mergeSort(num:List[int], n:int):
    if n > 1:
        m = n // 2 
        l1 = num[:m]
        n1 = len(l1)
        l2 = num[m:]
        n2 = len(l2)

        mergeSort(l1, n1)
        mergeSort(l2, n2)
        i = j = k = 0
        while i < n1 and j < n2:
            if l1[i] <= l2[j]:
                num[k] = l1[i]
                i += 1
            else:
                num[k] = l2[j]
                j += 1
            k += 1
        while i < n1:
            num[k] = l1[i]
            i += 1
            k += 1
        while j < n2:
            num[k] = l2[j]
            j += 1
            k += 1
a = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44, 0]
n = len(a)
print("Array before Sorting")
print(a)
mergeSort(a, n)
print("Array after Sorting")
print(a)

