from itertools import combinations


if __name__ == '__main__':
    print('Combinations Impl')
    temp = [elem for elem in combinations([-1, 0, 1, 2, -1, -4], 3) if sum(elem) == 0]
    result = set()
    for elem in temp:
        result.add(tuple(sorted(elem)))
    print(result)
