import random
from collections import deque


class Graph:
    def __init__(self):
        self.nodes = []


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.children = []


def create_graph():
    node_zero = Node(0)
    node_one = Node(1)
    node_two = Node(2)
    node_three = Node(3)
    node_four = Node(4)
    node_five = Node(5)
    node_six = Node(6)

    node_zero.children.append(node_one)
    node_one.children.append(node_two)
    node_two.children.append(node_zero)
    node_two.children.append(node_three)
    node_three.children.append(node_two)
    node_four.children.append(node_six)
    node_five.children.append(node_four)
    node_six.children.append(node_five)

    graph = Graph()
    graph.nodes.append(node_zero)
    graph.nodes.append(node_one)
    graph.nodes.append(node_two)
    graph.nodes.append(node_three)
    graph.nodes.append(node_four)
    graph.nodes.append(node_five)
    graph.nodes.append(node_six)

    return graph


def is_there_a_path_between_nodes(node_one, node_two):
    traversable_nodes = deque([])
    traversable_nodes.append(node_one)

    while len(traversable_nodes) > 0:
        current_node = traversable_nodes.popleft()
        current_node.visited = True
        print(f"{current_node.name} -> ", end="")
        if current_node is node_two:
            return True
        for child in current_node.children:
            if not child.visited:
                traversable_nodes.append(child)
    return False


if __name__ == '__main__':
    graph = create_graph()
    start_node = random.choice(graph.nodes)
    end_node = random.choice(graph.nodes)
    while end_node is start_node:
        node_two = random.choice(graph.nodes)
    print(f"{start_node.name}, {end_node.name}")
    print(f"{is_there_a_path_between_nodes(start_node, end_node)}")