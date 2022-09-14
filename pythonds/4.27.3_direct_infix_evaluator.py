from stack import Stack


def do_operation(op1, op2, operator):
    op1, op2 = int(op1), int(op2)
    if operator == '+':
        return op2 + op1
    elif operator == '-':
        return op2 - op1
    elif operator == '*':
        return op2 * op1
    elif operator == '/':
        return op2 / op1

# Called Shunting Yard algorithm. If you understand infix to postfix and postfix evaluation, this algorithm is dead easy
# value stack contains numbers, operator stack contains operators plus opening brace
# Using the digit_seen flag to keep track of multidigit numbers

def direct_infix_evaluator(expr):
    value_stack = Stack()
    operator_stack = Stack()
    precedence = {'*': 3, '/': 3, '+': 2, '-': 2}
    digit_seen = False
    for char in expr:
        if char == ' ':
            digit_seen = False
            continue
        elif char in '(':
            digit_seen = False
            operator_stack.push(char)
        elif char in '0123456789':
            if digit_seen:
                value_stack.push(value_stack.pop() + char)
            else:
                value_stack.push(char)
            digit_seen = True
        elif char in '+-/*':
            digit_seen = False
            while operator_stack.getSize() and operator_stack.peek() in '+-/*' and precedence[operator_stack.peek()] >= precedence[char]:
                value_stack.push(do_operation(value_stack.pop(), value_stack.pop(), operator_stack.pop()))
            operator_stack.push(char)
        elif char == ')':
            digit_seen = False
            while operator_stack.peek() != '(':
                value_stack.push(do_operation(value_stack.pop(), value_stack.pop(), operator_stack.pop()))
            operator_stack.pop()
    while operator_stack.getSize():
        value_stack.push(do_operation(value_stack.pop(), value_stack.pop(), operator_stack.pop()))
    return value_stack.pop()
        

print(direct_infix_evaluator('10 + 2 * 6'))
print(direct_infix_evaluator('100 * 2 + 12'))
print(direct_infix_evaluator('100 * ( 2 + 12 )'))
print(direct_infix_evaluator('100 * ( 2 + 12 ) / 14'))
