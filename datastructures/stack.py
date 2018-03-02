class Stack:
    def __init__(self):
        self.stack_data = []

    def push(self, data):
        self.stack_data = [data]+self.stack_data

    def push_array(self, arr):
        self.stack_data = arr + self.stack_data

    def pop(self):
        return_data = self.stack_data[0]
        self.stack_data = self.stack_data[1:]
        return return_data

    def print_stack(self):
        idx = 0
        while idx < len(self.stack_data):
            print(self.stack_data[idx], end=", ")
            idx += 1
        print("\n")

    def seek(self):
        return self.stack_data[0]

    def len_stack(self):
        _len = 0
        while self.stack_data[_len: _len+1]:
            _len += 1
        return _len


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.print_stack()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.print_stack()