from datastructures import stack


class PlateOfStacks:
    def __init__(self):
        self.stacks = [[]]
        self.present_stack_idx = 0
        self.stack_size = 5

    def push(self, data):
        if self._len_stack(self.stacks[self.present_stack_idx]) is self.stack_size:
            self.__add_stack()
            self.present_stack_idx += 1
        self.stacks[self.present_stack_idx] = [data]+self.stacks[self.present_stack_idx]

    def pop(self):
        pass

    def __add_stack(self):
        _stack = []
        self.stacks.append(_stack)

    def _len_stack(self, _stack):
        _len = 0
        while _stack[_len: _len+1]:
            _len += 1
        return _len

    def print_stack(self):
        for stack_idx in range(self._len_stack(self.stacks)):
            for idx in range(self._len_stack(self.stacks[stack_idx])):
                print(f"{self.stacks[stack_idx][idx]}", end=",")


if __name__ == '__main__':
    stack = PlateOfStacks()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    stack.push(60)
    stack.push(70)
    stack.push(80)
    stack.push(90)
    stack.push(100)
    stack.push(110)
    stack.print_stack()