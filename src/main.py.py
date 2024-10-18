import random
import time
import copy
#selectionsort
def selectionSort(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i + 1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
        list[min_idx], list[i] = list[i], list[min_idx]
#bubblesort
def BubbleSort(list):
    n = len(list)
    for i in range(n):
        for j in range(n - i - 1):
             if list[j] > list[j + 1]:
                 list[j], list[j + 1] = list[j + 1], list[j]
#insertionsort
def InsertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j], list[j + 1] = list[j + 1], list[j]
            j-=1
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
# mergesort
def mergesort(list):
    n = len(list)
    if (n > 1):
        mid = n // 2
        L = list[:mid]
        R = list[mid:]

        mergesort(L)
        mergesort(R)

        list.clear()
        while len(L) > 0 and len(R) > 0:
            if (L[0] < R[0]):
                list.append(L[0])
                L.pop(0)
            else:
                list.append(R[0])
                R.pop(0)
        for i in L:
            list.append(i)
        for i in R:
            list.append(i)

#quicksort
def partition(list, low, high):
    i = low - 1
    pivot = list[high]

    for j in range(low, high):
        if list[j] < pivot:
            i = i+1
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[high] = list[high], list[i + 1]
    return (i + 1)
def quicksort(list, low, high):
    if low < high:
        pi = partition(list, low, high)
        quicksort(list, low, pi - 1)
        quicksort(list, pi + 1, high)

#heapsort
def heapify(list, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and list[i] < list[l]:
        largest = l
    if r < n and list[largest] < list[r]:
        largest = r
    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, n, largest)
def heapsort(list):
    n = len(list)
    for i in range(n//2 - 1, -1, -1):
        heapify(list, n, i)
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)

list1 = list(i for i in range(10000))
random.shuffle(list1)

list_selectionsort = copy.deepcopy(list1)
start_time = time.time()
selectionSort(list_selectionsort)
end_time = time.time()
print("selectionsort_execution time:", (end_time - start_time), "s")

list_bubblesort = copy.deepcopy(list1)
start_time = time.time()
BubbleSort(list_bubblesort)
end_time = time.time()
print("bubblesort_execution time:", (end_time - start_time), "s")

list_insertionsort = copy.deepcopy(list1)
start_time = time.time()
InsertionSort(list_insertionsort)
end_time = time.time()
print("insertionsort_execution time:", (end_time - start_time), "s")

list_mergesort = copy.deepcopy(list1)
start_time = time.time()
mergesort(list_mergesort)
end_time = time.time()
print("mergesort_execution time:", (end_time - start_time), "s")

list_quicksort = copy.deepcopy(list1)
start_time = time.time()
quicksort(list_quicksort, 0, len(list_quicksort)- 1)
end_time = time.time()
print("quicksort_execution time:", (end_time - start_time), "s")

list_heapsort = copy.deepcopy(list1)
start_time = time.time()
heapsort(list_heapsort)
end_time = time.time()
print("heapsort_execution time:", (end_time - start_time), "s")

start_time = time.time()
list1.sort()
end_time = time.time()
print("python_sort_execution time:", (end_time - start_time), "s")

      


