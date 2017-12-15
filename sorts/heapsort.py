#!/usr/bin/env python3


def build_max_heap(arr):
    for i in range(len(arr) // 2, -1, -1):
        max_heapify(arr, i)


def max_heapify(arr, i):
    # print(arr, end=", heapify\n")
    l = left(i)
    r = right(i)
    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)


def heap_sort(arr):
    build_max_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        # print(arr, end=", before\n")
        arr[0], arr[i] = arr[i], arr[0]
        # arr = arr[:i]
        # print(arr, end=", after\n")
        temp = arr[:i]
        max_heapify(temp, 0)
        arr = temp+arr[i:]
    return arr


def left(i):
    return 2*i+1


def right(i):
    return 2*i+2


if __name__=='__main__':
    # arr=[6,5,3,1,8,7,2,4]
    arr = [23, 45, 1, 76, 235, 24, 686, 87, 234, 11, 235, 44, 29]
    # buildmaxheap(arr)
    print(arr, ", before sorting")
    sorted_array = heap_sort(arr)
    print(sorted_array, ", heap sorted array")
