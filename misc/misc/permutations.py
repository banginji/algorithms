def perms(n, base=[()], i=1):
    result = []
    for base_elem in base:
        new_elems = [base_elem + (elem,) for elem in range(1, n) if elem not in base_elem]
        result.extend(new_elems)
        if i is not n:
            result.extend(perms(n, new_elems, i + 1))
    return result


def perms_alpha(str, base=[()], idx=0):
    result = []
    for base_elem in base:
        new_elems = [base_elem + (elem,) for elem in range(1, n) if elem not in base_elem]
        result.extend(new_elems)
        if i is not n:
            result.extend(perms(n, new_elems, i + 1))
    return result


if __name__ == '__main__':
    print('Permutations Impl')
    result = perms(5)
    for elem in result:
        print(elem, end='\n')

# 1, 2
# (), (1), (2), (1, 2), (2, 1)
# 1, 2, 3
# (), 
# (1), 
# (2), 
# (3), 
# (1, 2), 
# (1, 3), 
# (2, 1), 
# (2, 3), 
# (3, 1), 
# (3, 2),
# (1, 2, 3), 
# (1, 3, 2), 
# (2, 1, 3), 
# (2, 3, 1), 
# (3, 1, 2), 
# (3, 2, 1)
