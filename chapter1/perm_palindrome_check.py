def is_perm_palindrome(str):
    ###############
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    is_odd = 0
    for char in str:
        char_val = get_char_value(char)
        if char_val != -1:
            table[char_val] += 1
            if table[char_val] % 2:
                is_odd += 1
            else:
                is_odd -= 1

    return is_odd <= 1


def get_char_value(char):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    char_val = ord(char)

    if a <= char_val <= z:
        return char_val - a
    elif A <= char_val <= Z:
        return  char_val - A
    else:
        return -1


if __name__ == '__main__':
    print(is_perm_palindrome("abccb sa"))