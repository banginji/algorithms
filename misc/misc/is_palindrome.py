from collections import deque


class LNode():
	def __init__(self, val):
		self.val = val
		self.next = None


def is_palindrome(head):
	fast, slow = head, head
	while fast:
		fast = fast.next.next
		slow = slow.next

	prev = None
	while slow:
		next = slow.next
		slow.next = prev
		prev = slow
		slow = next

	itx_node = head
	while prev:
		if prev.val != itx_node.val:
			return False
		prev = prev.next
		itx_node = itx_node.next

	return True


def is_palindrome_2(head):
	fast, slow = head, head
	stack = deque([])

	while fast:
		fast = fast.next.next
		stack.append(slow.val)
		slow = slow.next

	while slow:
		if slow.val != stack.pop():
			return False
		slow = slow.next

	return True


def create_word(str):
	chars = list(str)
	head = LNode(chars[0])
	itx_node = head
	for char in chars[1:]:
		itx_node.next = LNode(char)
		itx_node = itx_node.next
	itx_node.next = None
	return head


def print_list(node):
	itx_node = node
	while itx_node.next != None:
		print(itx_node.val, end=' -> ')
		itx_node = itx_node.next
	print(itx_node.val)


if __name__ == '__main__':
	print('Palindrome Linked List Impl')
	head = create_word('abcddcba')
	print_list(head)
	print(is_palindrome(head))
	print(is_palindrome_2(head))
