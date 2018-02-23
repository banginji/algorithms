class SingleLinkedListNode:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class DoublyLinkedListNode:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class SingleLinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, data):
        current = self.seek_tail()
        if current is not None:
            current.next = SingleLinkedListNode(data)
        else:
            self.head = SingleLinkedListNode(data)

    def add_array_of_elements(self, arr):
        if len(arr) is 0:
            return
        current = self.seek_tail()
        if current is None:
            self.head = SingleLinkedListNode(arr[0])
            current = self.head
        else:
            current.next = SingleLinkedListNode(arr[0])
            current = current.next
        for elem in arr[1:]:
            current.next = SingleLinkedListNode(elem)
            current = current.next

    def seek_tail(self):
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            return current
        else:
            return None

    def print_list(self):
        current = self.head
        while current is not None:
            print(f"{current.data}", end=" -> ")
            current = current.next
        print("None")

    def remove_node(self, node):
        current = self.head
        if current is None:
            return
        if self.head.next is None:
            if self.head is node:
                self.head = None
            else:
                return
        while current.next is not None:
            if current.next is node:
                current.next = current.next.next
                break
            current = current.next
        if self.head is node:
            new_head = self.head.next
            self.head = new_head

    def remove_node_with_data(self, data):
        current = self.head
        if current is None:
            return
        if self.head.next is None:
            if self.head.data is data:
                self.head = None
            else:
                return
        while current.next is not None:
            if current.next.data is data:
                current.next = current.next.next
                break
            current = current.next
        if self.head.data is data:
            new_head = self.head.next
            self.head = new_head

    def add_node_to_head_of_list(self, data):
        if self.head is None:
            self.head = SingleLinkedListNode(data)
        else:
            new_node = SingleLinkedListNode(data)
            new_node.next = self.head
            self.head = new_node
