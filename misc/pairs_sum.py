import timeit


def pairs_with_list_comprehension(arr, sum):
    return [{x, y} for idx_x, x in enumerate(arr) for y in arr[idx_x+1:] if x + y == sum]


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
    print(pairs_with_list_comprehension([5, 2, 4, 7, 3, 18, -9, 1, 53, 11, 8, 6], 9))
    # t = timeit.Timer("pairs_with_list_comprehension([5, 2, 4, 7, 3, 18, -9, 1, 53, 11, 8, 6], 9)", "from __main__ import pairs_with_list_comprehension")
    # time = t.timeit()
    # print(f"pairs_with_list_comprehension -----> {time}")

    print(pairs([5, 2, 4, 7, 3, 18, -9, 1, 53, 11, 8, 6], 9))
    # t = timeit.Timer("pairs([5, 2, 4, 7, 3, 18, -9, 1, 53, 11, 8, 6], 9)", "from __main__ import pairs")
    # time = t.timeit()
    # print(f"pairs -----> {time}")

    # Using lambdas
    x_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y_arr = [4, 6, 8]
    result_list = list(filter(lambda x: x not in y_arr, x_arr))
    print(result_list)

