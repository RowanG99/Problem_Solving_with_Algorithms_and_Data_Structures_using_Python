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