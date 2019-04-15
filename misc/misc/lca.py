class BTNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_bt():
    node_minus_one = BTNode(-1)
    node_zero = BTNode(0)
    node_one = BTNode(1)
    node_two = BTNode(2)
    node_three = BTNode(3)
    node_four = BTNode(4)
    node_five = BTNode(5)
    node_six = BTNode(6)
    node_seven = BTNode(7)
    node_eight = BTNode(8)
    node_nine = BTNode(9)

    node_six.left = node_two
    node_six.right = node_eight
    node_two.left = node_zero
    node_two.right = node_four
    node_zero.left = node_minus_one
    node_zero.right = node_one
    node_four.left = node_three
    node_four.right = node_five
    node_eight.left = node_seven
    node_eight.right = node_nine

    # node_two.left = node_one

    return (node_six, node_one, node_seven)


def lca(root, p, q):
    itx_node = root
    while itx_node.left != None or itx_node.right != None:
        if p.val <= itx_node.val <= q.val:
            return itx_node
        if itx_node.val <= p.val:
            itx_node = itx_node.right
        if q.val <= itx_node.val:
            itx_node = itx_node.left


if __name__ == '__main__':
    print('LCA Impl')
    root, p, q = create_bt()
    print(lca(root, p, q).val)
