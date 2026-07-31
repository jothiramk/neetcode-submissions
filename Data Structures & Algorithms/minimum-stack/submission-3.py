class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else :
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])


    def pop(self) -> None:
        # print(f'pop stack  is {self.stack[-1]}')
        # print(f'pop MinStack is {self.minStack[-1]}')
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # print(f'getMin is {self.minStack[-1]}')
        return self.minStack[-1]
