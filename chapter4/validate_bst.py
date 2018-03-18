class BinaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def create_binary_tree():
    root_node = BinaryTreeNode(5)
    node_one = BinaryTreeNode(3)
    node_two = BinaryTreeNode(7)
    node_three = BinaryTreeNode(2)
    node_four = BinaryTreeNode(4)
    node_five = BinaryTreeNode(6)
    node_six = BinaryTreeNode(5)
    node_seven = BinaryTreeNode(1)
    node_eight = BinaryTreeNode(1.5)

    root_node.left_child = node_one
    root_node.right_child = node_two
    node_one.left_child = node_three
    node_one.right_child = node_four
    node_two.left_child = node_five
    node_two.right_child = node_six
    node_three.left_child = node_seven
    node_seven.right_child = node_eight

    return root_node


def validate_bst(list_of_nodes):
    sorted_list = sorted(list_of_nodes)
    for x, y in zip(list_of_nodes, sorted_list):
        if x != y:
            return False
    return True


def in_order_traversal(node, list_of_nodes):
    if node is None:
        return
    in_order_traversal(node.left_child, list_of_nodes)
    list_of_nodes.append(node.data)
    in_order_traversal(node.right_child, list_of_nodes)


if __name__ == '__main__':
    root_node = create_binary_tree()
    list_of_nodes = []
    in_order_traversal(root_node, list_of_nodes)
    print(list_of_nodes)
    print(validate_bst(list_of_nodes))