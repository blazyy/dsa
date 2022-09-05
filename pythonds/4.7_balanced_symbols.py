from stack import Stack

def check_parentheses(string):
    stack = Stack()
    openers = '([{'
    closers = ')]}'
    for char in string:
        if char in openers:
            stack.push(char)
        else:
            if not stack.isEmpty():
                if openers.index(stack.peek()) == closers.index(char):
                    stack.pop()
                else:
                    return False
            else:
                return False
    if not stack.isEmpty():
        return False
    return True


print(check_parentheses('{({([][])}())}'))
print(check_parentheses('[{()]'))