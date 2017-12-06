def compress(str):
    idx = 0
    count = 1
    compressed_string = ''
    while idx < len(str):
        if idx == len(str)-1:
            compressed_string += str[idx] + repr(count)
            break
        if str[idx] == str[idx+1]:
            idx += 1
            count += 1
        else:
            compressed_string += str[idx] + repr(count)
            count = 1
            idx += 1
    return compressed_string


if __name__ == '__main__':
    print(compress("aaaaaabkdbbbbekjbbjeje"))