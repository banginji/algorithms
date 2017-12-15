def perm(arr):
    result = []

    def permute(current, rest):
        if not rest:
            result.append(current)
            return

        for i in rest:
            permute(current + (i, ), [j for j in rest if j != i])

    permute((), arr)
    return result


if __name__ == '__main__':
    print(perm([1, 2, 3]), end="\n")