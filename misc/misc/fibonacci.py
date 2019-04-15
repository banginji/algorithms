from collections import deque


def fib(n):
	queue = deque([0, 1, 1])

	for _ in range(n):
		queue.popleft()
		total = 0
		for elem in queue:
			total += elem
		queue.append(total)

	return queue.pop()


if __name__ == '__main__':
	print('Fibonacci impl')
	print(fib(30))
