from datastructures import stack
from sys import maxsize


class MinStack(stack.Stack):
    def __init__(self):
        super().__init__()

    def push(self, data):
        super().push((data, self._min(data)))

    def _min(self, data):
        if self.len_stack() is 0:
            return data
        _, prev_min = self.stack_data[0]
        if data < prev_min:
            return data
        else:
            return prev_min


if __name__ == '__main__':
    stack = MinStack()
    stack.push(2)
    stack.push(6)
    stack.push(4)
    stack.push(0)
    stack.push(5)
    stack.push(1)
    stack.print_stack()
    _, min_stack = stack.seek()
    print(min_stack)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.print_stack()
    _, min_stack = stack.seek()
    print(min_stack)