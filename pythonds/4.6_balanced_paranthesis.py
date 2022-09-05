from stack import Stack

def check_paranthesis(string):
    stack = Stack()
    for char in string:
        if char not in '()':
            raise Exception('Invalid character found!')
        elif char == '(':
            stack.push(char)
        else:
            if stack.isEmpty():
                return False
            else:
                stack.pop()
    if not stack.isEmpty():
        return False
    return True

print(check_paranthesis('((()))'))
print(check_paranthesis('(()'))
print(check_paranthesis('))))))))'))
print(check_paranthesis('(((())))'))
print(check_paranthesis('(((((('))
