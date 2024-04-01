import random

class Queue():
    def __init__(self):
        self.items = []
    def is_empty(self) -> any:
        return self.items == []
    def enqueue(self, item: any):
        self.items.insert(0,item)
    def dequeue(self) -> any:
        return self.items.pop()
    def size(self) -> int:
        return len(self.items)
    def queue_items(self):
        return self.items

# queue = Queue()
# queue.enqueue(25)
# print(queue.queue_items())
# queue.enqueue(9)
# print(queue.queue_items())
# queue.dequeue()
# print(queue.queue_items())

# Example 1: Hot Potato ----------------------------------
def hot_potato(players_list, num_passes) -> str:
    hot_potato_queue = Queue()
    for player in players_list:
        hot_potato_queue.enqueue(player)
    while hot_potato_queue.size() > 1:
        for i in range(num_passes):
            hot_potato_queue.enqueue(hot_potato_queue.dequeue())
        hot_potato_queue.dequeue()
    return hot_potato_queue.dequeue()

hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7)
# ---------------------------------------------------------

# Example 2: Printing Tasks -------------------------------
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    def busy(self) -> bool:
        if self.currentTask != None:
            return True
        else:
            return False
    def startNext(self, new_task):
        self.currentTask = new_task
        self.timeRemaining = new_task.get_pages() * 60/self.pagerate
class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
    def get_stamp(self):
        return self.timestamp
    def get_pages(self):
        return self.pages
    def wait_time(self, current_time):
        return current_time - self.timestamp
def simulation(num_secs, pages_per_min):
    printer = Printer(pages_per_min)
    printer_queue = Queue()
    waiting_times = []
    for current_secs in range(num_secs):
        if new_print_task():
            task = Task(current_secs)
            printer_queue.enqueue(task)
        if (not printer.busy()) and (not printer_queue.is_empty()):
            next_task = printer_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_secs))
            printer.startNext(next_task)
        printer.tick()
    average_wait = sum(waiting_times)/len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, printer_queue.size()))

def new_print_task():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)
# ---------------------------------------------------------
