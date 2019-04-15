from collections import deque


class Graph():
    def __init__(self, nodes):
        self.nodes = nodes


class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.visited = False


def init_graph():
    zero_zero = Node(1)
    zero_one = Node(2)
    zero_two = Node(3)
    one_zero = Node(4)
    one_one = Node(0)
    one_two = Node(6)
    two_zero = Node(0)
    two_one = Node(0)
    two_two = Node(9)
    three_zero = Node(0)
    three_one = Node(11)
    three_two = Node(12)

    zero_zero.children.extend([zero_one, one_one, one_zero])
    zero_one.children.extend([zero_zero, one_zero, one_one, one_two, zero_two])
    zero_two.children.extend([zero_one, one_one, one_two])
    one_zero.children.extend([zero_zero, zero_one, one_one, two_one, two_zero])
    one_one.children.extend([zero_zero, zero_one, zero_two, one_zero, one_two, two_zero, two_one, two_two])
    one_two.children.extend([zero_two, zero_one, one_one, two_one, two_two])
    two_zero.children.extend([one_zero, one_one, two_one, three_one, three_zero])
    two_one.children.extend([one_zero, one_one, one_two, two_zero, two_two, three_zero, three_one, three_two])
    two_two.children.extend([one_two, one_one, two_one, three_one, three_two])
    three_zero.children.extend([two_zero, two_one, three_one])
    three_one.children.extend([three_zero, two_zero, two_one, two_two, three_two])
    three_two.children.extend([two_two, two_one, three_one])

    return zero_zero


def min_dist(start_node):
    visited, queue = set(), deque([])
    queue.extend([start_node, None])

    _len = 0

    while len(queue) > 0:
        node = queue.popleft()
        if node is not None:
            print(f"{node.data}")
        if node is None:
            _len += 1
            if _len > 4:
                break
            queue.append(None)
            print(f"Length: {_len}")
            continue
        node.visited = True
        if node.data is 12:
            break
        for child in node.children:
            if child.data not in visited and child.data is not 0:
                visited.add(child.data)
                queue.append(child)

    return _len if _len <= 4 else -1


# 01 02 03
# 04 00 00
# 00 08 09
# 00 11 12


if __name__ == '__main__':
    print('Min dist impl')
    start_node = init_graph()
    print(f"{min_dist(start_node)}")
