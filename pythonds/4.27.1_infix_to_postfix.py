from stack import Stack

def infix_to_postfix(expr):
    stack = Stack()
    precedence = {'^': 3, '*': 2, '/':2, '+':1, '-':1}
    output = []
    for char in expr:
        if char == ' ':
            continue
        elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            output.append(char)
        elif char in '+-/*':
            if not stack.isEmpty() and stack.peek() != '(' and precedence[stack.peek()] >= precedence[char]:
                output.append(stack.pop())
            stack.push(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(':
                if stack.getSize() == 1 and stack.peek() != '(':
                    raise Exception(f'Invalid expression: Unbalanced parantheses.')
                output.append(stack.pop())
            stack.pop()
        else:
            raise Exception(f'Invalid character found in expression: {char}')
    while not stack.isEmpty():
        output.append(stack.pop())
    return ''.join(map(str, output))


print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
# print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F & G )"))
print(infix_to_postfix("( A + B ) * C - (( D - E ) * ( F + G )"))

# print(eval_postfix('7 8 + 3 2 + /'))
