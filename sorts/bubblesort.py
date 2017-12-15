#!/usr/bin/env python3


def bubble_sort(arr):
    count = len(arr)
    while count > 0:
        for i in range(0, count-1, 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        count -= 1


if __name__=='__main__':
    arr=[34, 52, 134, 656, 334, 14, 46, 32]
    bubble_sort(arr)
    print(arr, end=", bubble sorted\n")
