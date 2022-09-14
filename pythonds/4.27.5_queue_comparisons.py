import random
import timeit


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items != []:
            return self.items.pop()


class QueueReverse:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items != []:
            return self.items.pop()


'''
Using timeit, comparing random queue and dequeue operations (the random order operation is the same for both queues)
Incomplete!!
'''


def test_queue(random_numbers):
    queue = Queue()
    for num in random_numbers:
        if num == 0:
            queue.enqueue(num)
        else:
            queue.dequeue()


def test_queue_reverse(random_numbers):
    queue_rev = QueueReverse()
    for num in random_numbers:
        if num == 0:
            queue_rev.enqueue(num)
        else:
            queue_rev.dequeue()


NUM_SIMULATIONS = 10
NUM_QUEUE_OPERATIONS = 2000000
for _ in range(NUM_SIMULATIONS):

    random_numbers = [random.randint(0, 1) for i in range(NUM_QUEUE_OPERATIONS)]

    start_time_queue = timeit.default_timer()
    test_queue(random_numbers)
    end_time_queue = timeit.default_timer()

    start_time_queue_reverse = timeit.default_timer()
    test_queue_reverse(random_numbers)
    end_time_queue_reverse = timeit.default_timer()

    print(f'Queue: {round(end_time_queue - start_time_queue, 2)}s, Queue Reverse: {round(end_time_queue_reverse - start_time_queue_reverse, 2)}')