from sorts import quicksort as qs


def perm_check(input1, input2):
    return qs.qsort(input1) == qs.qsort(input2)


if __name__ == '__main__':
    print(perm_check("qwer", "rewqd"), end="")