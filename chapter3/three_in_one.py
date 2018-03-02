class StackThreeInOne:
    def __init__(self, number_of_stacks, stack_size):
        self.stack_data = [0 for _ in range(stack_size)] * number_of_stacks
        self.stack_metadata = []
        for idx in range(number_of_stacks):
            stack_top_idx = idx * stack_size
            stack_first_element_idx = stack_top_idx - 1
            stack_end_idx = stack_first_element_idx + stack_size
            self.stack_metadata.append((stack_top_idx, stack_first_element_idx, stack_end_idx))
        self.stack_size = stack_size

    def push(self, data, stack_idx):
        stack_top_idx, stack_first_element_idx, stack_end_idx = self.stack_metadata[stack_idx]
        if stack_first_element_idx == stack_end_idx:
            print(f"{data} cannot be pushed. Stack is full")
            return

        if stack_first_element_idx < stack_top_idx:
            self.stack_data[stack_top_idx] = data
            stack_first_element_idx += 1
        else:
            idx = stack_first_element_idx
            while idx >= stack_top_idx:
                self.stack_data[idx+1] = self.stack_data[idx]
                idx -= 1
            self.stack_data[stack_top_idx] = data
            stack_first_element_idx += 1

        self.stack_metadata[stack_idx] = (stack_top_idx, stack_first_element_idx, stack_end_idx)

    def pop(self, stack_idx):
        stack_top_idx, stack_first_element_idx, stack_end_idx = self.stack_metadata[stack_idx]
        if stack_first_element_idx < stack_top_idx:
            print(f"Stack is empty")
            return

        idx = stack_top_idx
        while idx < stack_first_element_idx:
            self.stack_data[idx] = self.stack_data[idx+1]
            idx += 1
        self.stack_data[stack_first_element_idx] = 0
        stack_first_element_idx -= 1

        self.stack_metadata[stack_idx] = (stack_top_idx, stack_first_element_idx, stack_end_idx)

    def print_stack(self):
        for idx in range(self.len_stack()):
            print(f"{self.stack_data[idx]}", end=", ")
        print(end="\n")

    def len_stack(self):
        _len = 0
        while self.stack_data[_len: _len+1]:
            _len += 1
        return _len


if __name__ == '__main__':
    stack = StackThreeInOne(3, 5)
    stack.print_stack()
    stack.push(10, 1)
    stack.push(20, 1)
    stack.push(30, 2)
    stack.push(40, 0)
    stack.push(50, 2)
    stack.push(60, 2)
    stack.push(70, 1)
    stack.print_stack()
    stack.pop(1)
    stack.pop(1)
    stack.pop(1)
    stack.print_stack()