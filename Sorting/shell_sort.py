def shell_sort(num, n):
    gap = n//2
    while gap > 0:
        for i in range(int(gap),n):
            temp = num[i]
            j = i 
            while j >=gap and num[j-gap] > temp:
                num[j] = num[j - gap]
                j -= gap
                num[j] = temp
        gap = gap //2 

num = [33, 45, 62, 12, 98]
n = len(num)
print("Array before Sorting: ")
print(num)
shell_sort(num, n);
print("Array after Sorting: ")
print(num)