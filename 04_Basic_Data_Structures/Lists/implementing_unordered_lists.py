class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next

class Unordered_list:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count 
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

unordered_list = Unordered_list()

unordered_list.add(31)
unordered_list.add(77)
unordered_list.add(17)
unordered_list.add(93)
unordered_list.add(26)
unordered_list.add(54)

print(unordered_list.search(91))