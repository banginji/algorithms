class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


def sum_list(l1, l2):
    res_list_head = ListNode(l1.val + l2.val)
    it = res_list_head
    l1 = l1.next
    l2 = l2.next
    while l1.next is not None:
        it.next = ListNode(l1.val + l2.val)
        it = it.next
        l1 = l1.next
        l2 = l2.next
    it.next = ListNode(l1.val + l2.val)
    return res_list_head


def create_list(number):
    head = ListNode(int(number[0]))
    it = head
    for num in number[1:]:
        node = ListNode(int(num))
        it.next = node
        it = it.next
    return head


if __name__ == '__main__':
    print('Lists sum')
    num1 = create_list(str(123))
    num2 = create_list(str(456))
    sum_head = sum_list(num1, num2)
    result = []
    while sum_head.next is not None:
        result.append(sum_head.val)
        sum_head = sum_head.next
    result.append(sum_head.val)
    print(result)
    # while sum_head.next is not None:
    #     print(sum_head.val, end=', ')
    #     sum_head = sum_head.next
    # print(sum_head.val)
