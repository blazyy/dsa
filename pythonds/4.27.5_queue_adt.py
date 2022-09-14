class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def get_front(self):
        return self.items[0]

    def get_rear(self):
        return self.items[-1]