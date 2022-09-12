from queue import Queue


def hot_potato(names, num):
    queue = Queue(names)
    while queue.getSize() != 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()


print(hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))
