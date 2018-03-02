def is_str_in(str1, str2):
    if not str1 or not str2:
        return False

    if len_of_str(str1) > len_of_str(str2):
        shorter_str = str2
        longer_str = str1
    else:
        shorter_str = str1
        longer_str = str2

    idx_shorter = 0
    idx_longer = 0

    while idx_longer < len_of_str(longer_str):
        if shorter_str[idx_shorter] is longer_str[idx_longer]:
            idx_range = idx_longer + len_of_str(shorter_str)
            while idx_longer < idx_range:
                if shorter_str[idx_shorter] is not longer_str[idx_longer]:
                    return False
                idx_longer += 1
                idx_shorter += 1
            return True
        idx_longer += 1
    return False


def len_of_str(str):
    idx = 0
    while str[idx: idx+1]:
        idx += 1
    return idx


if __name__ == '__main__':
    print(is_str_in("pqr", "prabc"))