def url_encoded(url):
    return ''.join(x if x != ' ' else '%20' for x in url)


def temp(url):
    for index, item in enumerate(url):
        if url[index] == ' ':
            url[index] = '%20'
    return url


if __name__ == '__main__':
    print(url_encoded("iuefh iwoeh"))