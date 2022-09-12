import random
from queue import Queue

PRINTER_PPM = 10
NUM_STUDENTS = 10
LOWER_BOUND_PRINT_TASK = 1
UPPER_BOUND_PRINT_TASK = 20
NUM_TASKS_PER_STUDENT = 2

class Printer:
    def __init__(self):
        self.print_queue = Queue()

    def get_num_waiting_tasks(self):
        return self.print_queue.get_size()

    def get_current_task(self):
        return self.print_queue.get_front()

    def add_task(self, task):
        self.print_queue.enqueue(task)

    def remove_task(self):
        self.print_queue.dequeue()

class Task:
    def __init__(self, start_time, num_pages):
        self.start_time = start_time
        self.remaining_time = (num_pages / PRINTER_PPM) * 60

    def get_remaining_time(self):
        return self.remaining_time

    def get_num_pages(self):
        return self.num_pages

    def do_task(self):
        self.remaining_time -= 1


def simulate(duration_hours):
    printer = Printer()
    waiting_times = []
    duration_seconds = duration_hours * 3600
    for second in range(duration_seconds):
        is_task_available = random.randint(1, 3600 // (NUM_TASKS_PER_STUDENT * NUM_STUDENTS))
        if printer.get_num_waiting_tasks() > 0:
            current_task = printer.get_current_task()
            if current_task.get_remaining_time() == 0:
                printer.remove_task()
            else:
                current_task.do_task()
        if is_task_available == 180:
            new_task = Task(start_time=second, num_pages=random.randint(LOWER_BOUND_PRINT_TASK, UPPER_BOUND_PRINT_TASK))
            if printer.get_num_waiting_tasks() > 0:
                waiting_times.append(printer.get_current_task().get_remaining_time())
            printer.add_task(new_task)
    print(f'Average waiting time: {round(sum(waiting_times) / len(waiting_times), 2)}. Remaining tasks: {printer.get_num_waiting_tasks()}')


for i in range(10):
    simulate(1)