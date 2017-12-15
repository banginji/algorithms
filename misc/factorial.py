def fact(n):

    def _fact(_n, acc):
        if _n == 0:
            return acc
        else:
            return _fact(_n-1, acc*_n)

    return _fact(n, 1)


if __name__ == '__main__':
    print(fact(10))
