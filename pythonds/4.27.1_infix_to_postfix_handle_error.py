from operator import is_
from stack import Stack

def infix_to_postfix_handle_error(expr):
    stack = Stack()
    balance_check_stack = Stack()
    is_balanced = True
    precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    output = []
    for char in expr:
        if char == ' ':
            continue
        elif char == '(':
            stack.push(char)
            balance_check_stack.push(char)
        elif char in precedence:
            while stack.getSize() > 0 and stack.peek() in precedence and precedence[stack.peek()] > precedence[char]:
                output.append(stack.pop())
            stack.push(char)
        elif char == ')':
            if balance_check_stack.pop() != '(':
                is_balanced = False
            while stack.getSize() > 0 and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            output.append(char)
    while stack.getSize() > 0:
        output.append(stack.pop())
    if not is_balanced or balance_check_stack.getSize() > 0:
        return 'Unbalanced parentheses, cannot process.'
    return ' '.join(item for item in output)


print(infix_to_postfix_handle_error("A * B + C * D"))
print(infix_to_postfix_handle_error("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix_handle_error("( A + B ) * C - (( D - E ) * ( F + G )"))