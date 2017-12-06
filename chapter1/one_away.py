def one_char_away(str1, str2):
    one_diff = False
    if len(str1) == len(str2):
        for x, y in zip(str1, str2):
            if x != y:
                if not one_diff:
                    one_diff = True
                    continue
                if one_diff:
                    return False
        return True
    elif abs(len(str1) - len(str2)) >= 2:
        return False
    else:
        longer_string = max([str1, str2], key=len)
        shorter_string = min([str1, str2], key=len)
        i, j = 0, 0
        while i < len(longer_string) and j < len(shorter_string):
            if longer_string[i] != shorter_string[j]:
                if not one_diff:
                    one_diff = True


# Levenshtein Distance algorithm implementation - Expensive
def lev(str1, str2):
    length_of_str1 = len(str1)
    length_of_str2 = len(str2)

    dis_table = [[0 for _ in range(length_of_str2+1)] for _ in range(length_of_str1+1)]

    for i in range(1, length_of_str1+1):
        dis_table[i][0] = i

    for j in range(1, length_of_str2+1):
        dis_table[0][j] = j

    for i in range(1, length_of_str1+1):
        for j in range(1, length_of_str2+1):
            if str1[i-1] == str2[j-1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            dis_table[i][j] = min(dis_table[i-1][j] + 1, dis_table[i][j-1] + 1, dis_table[i-1][j-1] + substitution_cost)

    print("Cost Matrix for {}, {}:".format(str1, str2), end="\n")
    for i in range(length_of_str1+1):
        for j in range(length_of_str2+1):
            print("{}".format(dis_table[i][j]), end=", ")
        print(end="\n")
    print(end="\n")

    return dis_table[length_of_str1][length_of_str2]


# Levenshtein Distance with two matrix rows
def lev_alternate(str1, str2):
    length_of_str1 = len(str1)
    length_of_str2 = len(str2)

    v0 = [0 for _ in range(length_of_str2 + 1)]
    v1 = [0 for _ in range(length_of_str2 + 1)]

    for i in range(length_of_str2+1):
        v0[i] = i

    for i in range(length_of_str1):
        v1[0] = i + 1
        for j in range(length_of_str2):
            deletion_cost = v0[j + 1] + 1
            insertion_cost = v1[j] + 1
            if str1[i] == str2[j]:
                substitution_cost = v0[j]
            else:
                substitution_cost = v0[j] + 1
            v1[j+1] = min(deletion_cost, insertion_cost, substitution_cost)
        for j in range(len(v0)):
            v0[j] = v1[j]
    return v1[length_of_str2]


if __name__ == '__main__':
    print("Distance: {}".format(lev("abb", "bbbb")), end="\n\n")
    print("Distance: {}".format(lev("kitten", "sitting")), end="\n\n")
    print("Distance: {}".format(lev("Saturday", "Sunday")), end="\n\n")
    print(lev_alternate("abb", "bbbb"))
    print(lev_alternate("kitten", "sitting"))
    print(lev_alternate("Saturday", "Sunday"))
