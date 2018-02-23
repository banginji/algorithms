from datastructures import LinkedList


def is_palindrome(list):
    # get tail and head
    # compare
    # if equal remove from list

    tail = list.seek_tail()

    while tail is not None or list.head is not None:
        if tail is None or list.head is None:
            return True
        else:
            if tail.data is list.head.data:
                list.remove_node(tail)
                list.remove_node(list.head)
            else:
                return False
        tail = list.seek_tail()
    return True


if __name__ == '__main__':
    is_palindrome_string = "aabca"
    is_palindrome_list = LinkedList.SingleLinkedList()
    is_palindrome_list.add_array_of_elements(is_palindrome_string)
    is_palindrome_list.print_list()
    print(is_palindrome(is_palindrome_list))
