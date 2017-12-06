def is_unique_chars(str):
    return len(set(str)) == len(str)


if __name__ == '__main__':
    print(is_unique_chars("dsgaed"), end="")