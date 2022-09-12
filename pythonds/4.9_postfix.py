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


def eval_postfix(expr):
    def do_math(op1, op2, operator):
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        elif operator == '/':
            return op1 / op2
    stack = Stack()
    for char in expr:
        if char == ' ':
            continue
        elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            stack.push(char)
        else:
            op2, op1 = int(stack.pop()), int(stack.pop())
            new_num = do_math(op1, op2, char)
            stack.push(new_num)
    return stack.pop()


print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(eval_postfix('7 8 + 3 2 + /'))