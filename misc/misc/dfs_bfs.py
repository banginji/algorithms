from collections import deque


class Graph():
	def __init__(self):
		self.nodes = []


class Node():
	def __init__(self, data):
		self.data = data
		self.visited = False
		self.neighbours = []


def create_graph():
	node_zero = Node(0)
	node_one = Node(1)
	node_two = Node(2)
	node_three = Node(3)
	node_four = Node(4)
	node_five = Node(5)

	node_zero.neighbours.extend([node_one, node_two])
	node_one.neighbours.extend([node_three, node_two])
	node_two.neighbours.extend([node_four, node_five])

	return node_zero

	#   1-3
	#  /|
	# 0-2-4
	#    \
	#	  5


def dfs(node):
	print(node.data)
	for neighbour in node.neighbours:
		if not neighbour.visited:
			neighbour.visited = True
			dfs(neighbour)


def bfs(start_node):
	queue = deque([start_node])
	while len(queue) > 0:
		node = queue.popleft()
		if node.visited:
			continue
		node.visited = True
		print(node.data)
		for neighbour in node.neighbours:
			if not neighbour.visited:
				queue.append(neighbour)


if __name__ == '__main__':
	start_node = create_graph()
	print("DFS Impl")
	dfs(start_node)
	start_node = create_graph()
	print("BFS Impl")
	bfs(start_node)
