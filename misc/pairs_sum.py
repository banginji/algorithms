def pairs_with_list_comprehension(arr, sum):
    return [(x, y) if x + y == sum else (x, y, 0) for idx_x, x in enumerate(arr) for y in arr[idx_x+1:]]


def pairs(arr, sum):
    result_set = []
    i, j = 0, 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] + arr[j] == sum:
                result_set.append({arr[i], arr[j]})
                arr.remove(arr[i])
                arr.remove(arr[j-1])
                i, j = 0, 0
                continue
            else:
                j += 1
        i += 1

    return result_set


if __name__ == '__main__':
    print(pairs([5, 2, 4, 7, 3, 18, -9, 1, 53, 11, 8, 6], 9))
