def selectionSort(A):
    for i in range(len(A)):
        least = i
        for j in range(i + 1, len(A)):
            if A[j] < A[least]:
                least = j
                temp = A[i]
                A[i] = A[j]
                A[j] = temp

num = [6,5,4,3,2,1]
selectionSort(num)
print(num)