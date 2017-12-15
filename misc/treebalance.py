#!/usr/bin/env python3

from collections import deque


class BinaryTreeNode:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_tree():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    # root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.left.right.left = BinaryTreeNode(8)
    root.left.right.left.right = BinaryTreeNode(9)
    return root


def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print('{0:}, '.format(node.value), end="")
    in_order_traversal(node.right)


def is_tree_balanced(node):
    return abs(height(node.left)-height(node.right))<=1


def height(node):
    lh = -1
    rh = -1
    if node.left is not None:
        lh = height(node.left)
        lh += 1
    else:
        lh += 1
    if node.right is not None:
        rh = height(node.right)
        rh += 1
    else:
        rh += 1
    
    return max(lh, rh)


def bfs(node):
    if node is not None:
        return
    q = deque([])
    q.append(node)
    while len(q) > 0:
        temp_node = q.popleft()
        print(temp_node.value, end=", ")
        if temp_node.left is not None:
            q.append(temp_node.left)
        if temp_node.right is not None:
            q.append(temp_node.right)


if __name__ == '__main__':
    in_order_traversal(create_tree())
    print("\n", end="")
    print(is_tree_balanced(create_tree()))
    bfs(create_tree())
