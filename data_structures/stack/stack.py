class Stack:
    def __init__(self):
        self.stack = []
        self.stack_size = 0

    def push(self, element):
        self.stack.append(element)
        self.stack_size += 1

    def pop(self):
        self.temp = False
        if not self.empty():
            self.temp = self.stack.pop(self.stack_size - 1)
            self.stack_size -= 1
        return self.temp

    def top(self):
        if self.stack_size > 0:
            return self.stack[-1]
        return None

    def empty(self):
        if self.stack_size == 0:
            return True
        return False

    def length(self):
        return self.stack_size
