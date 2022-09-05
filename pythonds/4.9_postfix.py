from stack import Stack

def infix_to_postfix(expr):
    output = []
    stack = Stack()
    precedence = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2}
    for char in expr:
        if char == ' ':
            continue
        elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            output.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while not stack.isEmpty() and stack.peek() != '(' and precedence[stack.peek()] >= precedence[char]:
                output.append(stack.pop())
            stack.push(char)
    while not stack.isEmpty():
        output.append(stack.pop())
    return ' '.join(map(str, output)) 


print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))