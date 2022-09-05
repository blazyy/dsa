class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.getSize():
            return self.items[-1]
        raise Exception('Cannot peek, no items in stack!')

    def __str__(self):
        return ', '.join([str(item) for item in self.items])

    def getSize(self):
        return len(self.items)