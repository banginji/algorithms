def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr if x < arr[0]]) + [arr[0]] + qsort([x for x in arr if x > arr[0]])


def qsort_alt(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)-1]
        lesser = []
        greater = []
        idx = 0
        while idx < len(arr)-1:
            if arr[idx] < pivot:
                lesser.append(arr[idx])
            else:
                greater.append(arr[idx])
            idx += 1
        return qsort_alt(lesser) + [pivot] + qsort_alt(greater)


if __name__ == '__main__':
    print(qsort_alt([34, 12, 542]))
    print(qsort_alt([32, 53, 23, 12, 45]))
    print(qsort_alt("afsa"))