from datastructures import LinkedList
from collections import deque


class BinaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def create_binary_tree():
    root_node = BinaryTreeNode(0)
    node_one = BinaryTreeNode(1)
    node_two = BinaryTreeNode(2)
    node_three = BinaryTreeNode(3)
    node_four = BinaryTreeNode(4)
    node_five = BinaryTreeNode(5)
    node_six = BinaryTreeNode(6)
    node_seven = BinaryTreeNode(7)

    root_node.left_child = node_one
    root_node.right_child = node_two
    node_one.left_child = node_three
    node_one.right_child = node_four
    node_two.left_child = node_five
    node_two.right_child = node_six
    node_three.left_child = node_seven

    return root_node


def list_of_depths(same_level_nodes, result_list):
    if len(same_level_nodes) is 0:
        return

    traversable_nodes = deque([])
    same_level_nodes_linked_list = LinkedList.SingleLinkedList()
    while len(same_level_nodes) is not 0:
        traversable_nodes.append(same_level_nodes.popleft())
    for node in traversable_nodes:
        same_level_nodes_linked_list.add_node(node.data)
    result_list.append(same_level_nodes_linked_list)
    while len(traversable_nodes) is not 0:
        current_node = traversable_nodes.popleft()
        if current_node.left_child is not None:
            same_level_nodes.append(current_node.left_child)
        if current_node.right_child is not None:
            same_level_nodes.append(current_node.right_child)
    list_of_depths(same_level_nodes, result_list)
    return result_list


def print_linked_lists_data(result_list):
    for linked_list in result_list:
        linked_list.print_list()


if __name__ == '__main__':
    root_node = create_binary_tree()
    result_list = []
    list_of_depths(deque([root_node]), result_list)
    print_linked_lists_data(result_list)