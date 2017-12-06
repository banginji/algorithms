def is_string_rotated(str1, str2):

    if len(str1) != len(str2):
        return False

    idx = 0
    found = False
    new_string = str1+str1
    for i in range(len(new_string)):
        if found:
            if str2[idx] == new_string[i]:
                idx += 1
                if idx == len(str2):
                    return True
                else:
                    continue
            else:
                return False
        elif str2[idx] == new_string[i]:
            found = True
            idx += 1
            continue


if __name__ == '__main__':
    print(is_string_rotated("racame", "acamera"))