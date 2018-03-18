from collections import deque


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def create_minimal_tree(arr, node):
    if len(arr) <= 1:
        return
    left_arr = arr[:len(arr) // 2]
    node.left_child = BinarySearchTreeNode(left_arr[len(left_arr) // 2])
    create_minimal_tree(left_arr, node.left_child)

    if len(arr) > 2:
        right_arr = arr[len(arr) // 2 + 1:]
        node.right_child = BinarySearchTreeNode(right_arr[len(right_arr) // 2])
        create_minimal_tree(right_arr, node.right_child)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    root_node = BinarySearchTreeNode(arr[len(arr) // 2])
    create_minimal_tree(arr, root_node)
    print("")