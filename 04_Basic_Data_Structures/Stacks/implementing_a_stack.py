from typing import List

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self) -> any:
        return self.items == []
    def push(self, item: any):
        self.items.append(item)
    def pop(self) -> any:
        return self.items.pop()
    def peek(self) -> any:
        return self.items[len(self.items)-1]
    def size(self) -> int:
        return len(self.items)
    
# Example 1: Parenthesis checker ----------------------------------
def matches(open: str, close: str) -> bool:
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)
    
def paren_checker(paren: str) -> bool:
    paren_checker = Stack()
    balanced = True
    index = 0
    while index < len(paren) and balanced:
        symbol = paren[index]
        if symbol in "([{":
            paren_checker.push(symbol)
        else:
            if paren_checker.is_empty():
                balanced = False
            else:
                top = paren_checker.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and paren_checker.is_empty():
        return True
    else:
        return False

print(paren_checker('{({([][])}())}'))
print(paren_checker('[{()]'))
# -----------------------------------------------------------------

# Example 2: Converting Decimal Numbers to Binary Numbers ---------
def divide_by_two(number):
    divide_by_two_stack = Stack()
    while number > 0:
        remainder = number % 2
        divide_by_two_stack.push(remainder)
        number = number // 2
    binary_string = ""
    while not divide_by_two_stack.is_empty():
        binary_string = binary_string + str(divide_by_two_stack.pop())
    return binary_string

print(divide_by_two(42))
# -----------------------------------------------------------------

# Example 3: Base converter ---------------------------------------
def base_converter(number: int, base: int) -> str:
    digits = "0123456789ABCDEF"
    base_converter_stack = Stack()
    while number > 0:
        remainder = number % base
        base_converter_stack.push(remainder)
        number = number // base
    binary_string = ""
    while not base_converter_stack.is_empty():
        binary_string = binary_string + digits[base_converter_stack.pop()]
    return binary_string

print(base_converter(25,2))
print(base_converter(25,16))
# -----------------------------------------------------------------
# Example 4: Infix to postfix converter ---------------------------
def infix_to_postfix(infix_value: str) -> List[str]:
    precedence = {}
    precedence['*'] = 3
    precedence['/'] = 3
    precedence['+'] = 2
    precedence['-'] = 2
    precedence['('] = 1
    operator_stack = Stack()
    postfix_list = []
    token_list = infix_value.split()
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            topToken = operator_stack.pop()
            while topToken != '(':
                postfix_list.append(topToken)
                topToken = operator_stack.pop()
        else:
            while (not operator_stack.is_empty()) and (precedence[operator_stack.peek()] >= precedence[token]):
                postfix_list.append(operator_stack.pop())
            operator_stack.push(token)
    while not operator_stack.is_empty():
        postfix_list.append(operator_stack.pop())
    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
# -----------------------------------------------------------------