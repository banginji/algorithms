from datastructures import LinkedList


def sum_list_backward(list_a, list_b):
    current_a = list_a.head
    current_b = list_b.head

    # sum_list = []
    sum_list = LinkedList.SingleLinkedList()
    carry = 0

    while current_a or current_b is not None:
        if current_a is None:
            temp_sum = current_b.data + carry
            current_b = current_b.next
        elif current_b is None:
            temp_sum = current_a.data + carry
            current_a = current_a.next
        elif current_a and current_b is not None:
            temp_sum = current_a.data + current_b.data + carry
            current_a = current_a.next
            current_b = current_b.next
        if temp_sum > 9:
            # sum_list.append(temp_sum%10)
            sum_list.add_node(temp_sum%10)
            carry = 1
        else:
            # sum_list.append(temp_sum)
            sum_list.add_node(temp_sum)
            carry = 0

    if carry != 0:
        # sum_list.append(carry)
        sum_list.add_node(carry)
    return sum_list


def sum_list_forward(list_a, list_b):
    tail_a = list_a.seek_tail()
    tail_b = list_b.seek_tail()

    # sum_list = []
    sum_list = LinkedList.SingleLinkedList()
    carry = 0

    while tail_a or tail_b is not None:
        if tail_a is None:
            temp_sum = tail_b.data + carry
        elif tail_b is None:
            temp_sum = tail_a.data + carry
        elif tail_a and tail_b is not None:
            temp_sum = tail_b.data + tail_b.data + carry
        if temp_sum > 9:
            # sum_list.append(temp_sum%10)
            sum_list.add_node_to_head_of_list(temp_sum%10)
            carry = 1
        else:
            # sum_list.append(temp_sum)
            sum_list.add_node_to_head_of_list(temp_sum)
            carry = 0
        list_a.remove_node(tail_a)
        list_b.remove_node(tail_b)
        tail_a = list_a.seek_tail()
        tail_b = list_b.seek_tail()

    if carry != 0:
        # sum_list.append(carry)
        sum_list.add_node_to_head_of_list(carry)
    return sum_list


if __name__ == '__main__':
    list_a = LinkedList.SingleLinkedList()
    list_a.add_array_of_elements([9, 9])

    list_b = LinkedList.SingleLinkedList()
    list_b.add_array_of_elements([9, 9, 9])

    sum_list = sum_list_forward(list_a, list_b)
    sum_list.print_list()
