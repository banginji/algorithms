def convert(s, num_rows):
    """
    :type s: str
    :type num_rows: int
    :rtype: str
    """
    dir = 1
    itx_row = 0
    len_str = len(s)
    result = [""] * num_rows
    for idx in range(len_str):
        result[itx_row] += s[idx]
        itx_row += dir
        if itx_row is 0 or itx_row % (num_rows-1) is 0:
            dir *= -1
    return ''.join([elem for elem in result])


if __name__ == '__main__':
    print('String to Pattern Impl')
    print(convert("PAYPALISHIRING", 50))
