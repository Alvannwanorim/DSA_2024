def heapify(heap, n, i):
    maximum = i 
    l = 2 * i + 1
    r = 2 * i + 1
    if l < n and heap[i] < heap[l]:
        maximum = l 
    if r < n and heap[maximum] < heap[r]:
        maximum = r 
    if maximum != i:
        heap[i], heap[maximum] = heap[maximum], heap[i]
        heapify(heap, n, maximum)

def heap_sort(heap):
    n = len(heap)
    for i in range(n, -1, -1):
        heapify(heap, n, i)
    
    for i in range(n - 1, 0, -1):
        heap[i], heap[0] = heap[0], heap[i]
        heapify(heap, i, 0)

heap = [4, 3, 1, 0, 2]
heap_sort(heap)
n = len(heap)
print("Heap array: ")
print(heap)
print ("The Sorted array is: ")
print(heap)