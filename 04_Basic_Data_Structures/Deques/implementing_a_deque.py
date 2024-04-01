class Deque():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_front(self, item):
        self.items.append(item)
    def add_rear(self, item):
        self.items.insert(0,item)
    def size(self):
        return len(self.items)
    def remove_front(self):
        return self.items.pop()
    def remove_rear(self):
        return self.items.pop(0)
    
# Example 1: Palindrome Checker -----------------------------------
def palindrome_checker(string):
    deque = Deque()
    for char in string:
        deque.add_rear(char)
    equal = True
    while deque.size() > 1 and equal:
        first  = deque.remove_front()
        last = deque.remove_rear()
        if first != last:
            equal = False
    return equal

print(palindrome_checker("fnwofwefw"))
print(palindrome_checker("racecar"))
# -----------------------------------------------------------------