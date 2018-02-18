def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr if x < arr[0]]) + [arr[0]] + qsort([x for x in arr if x > arr[0]])


# with extra buffers
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


# avoiding the use of extra buffers
def qsort_space(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)-1]
    pivot_idx = len(arr)-1
    wall_idx, idx = 0, 0

    while idx < len(arr):
        if arr[idx] < pivot:
            if wall_idx != idx:
                arr[wall_idx], arr[idx] = arr[idx], arr[wall_idx]
            wall_idx += 1
            idx += 1
        else:
            idx += 1
    arr[wall_idx], arr[pivot_idx] = arr[pivot_idx], arr[wall_idx]

    return qsort_space(arr[:wall_idx]) + [arr[wall_idx]] + qsort_space(arr[wall_idx+1:])


# Correct time and space complexity
def qsort_eff(arr, start, end):
    if start == end:
        return

    pivot = arr[end]
    wall_idx, idx = start, start

    for idx in range(start, end):
        if arr[idx] < pivot:
            if idx != wall_idx:
                arr[idx], arr[wall_idx] = arr[wall_idx], arr[idx]
            idx += 1
            wall_idx += 1
        else:
            idx += 1
    arr[wall_idx], arr[end] = arr[end], arr[wall_idx]

    if start < wall_idx:
        qsort_eff(arr, start, wall_idx-1)
    if wall_idx < end:
        qsort_eff(arr, wall_idx+1, end)


if __name__ == '__main__':
    print(qsort_alt([34, 12, 542]))
    print(qsort_alt([32, 53, 23, 12, 45]))
    print(qsort_alt("afsa"))
    arr_to_be_sorted = [1234, 12, 341, 123, 764, 3423, 764, 23, 1, 0, 3123, 32]
    qsort_eff(arr_to_be_sorted, 0, len(arr_to_be_sorted)-1)
    print(arr_to_be_sorted, end="; after sorting")