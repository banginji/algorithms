from heapq import heappush, heappop


def dijkstra(graph, start_vertex):
	distances = {}
	pq = []
	for vertex in graph:
		if vertex != start_vertex:
			distances[vertex] = [float('infinity'), vertex]
		else:
			distances[vertex] = [0, vertex]
		heappush(pq, distances[vertex])

	while len(pq) > 0:
		_, vertex = heappop(pq)
		for neighbour, neighbour_distance in graph[vertex].items():
			if neighbour_distance < distances[neighbour][0]:
				distances[neighbour][0] = neighbour_distance

	return distances


def create_graph():
	return {
	    'U': {'V': 2, 'W': 5, 'X': 1},
	    'V': {'U': 2, 'X': 2, 'W': 3},
	    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
	    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
	    'Y': {'X': 1, 'W': 1, 'Z': 1},
	    'Z': {'W': 5, 'Y': 1},
	}


if __name__ == '__main__':
	print('Dijkstra Heapq Impl')
	print(dijkstra(create_graph(), 'X'))
