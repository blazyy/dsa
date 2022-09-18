from stack import Stack

def do_operation(op1, op2, op):
    op1, op2 = int(op1), int(op2)
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op2 - op1
    elif op == '/':
        return op2 / op1
    elif op == '*':
        return op2 * op1

def infix_evaluator(expr):
    op_stack = Stack()
    val_stack = Stack()
    precedence = {'*': 2, '/': 2, '+': 1, '-': 1}
    digit_seen = False
    try:
        for char in expr:
            if char == ' ':
                digit_seen = False
                continue
            elif char == '(':
                digit_seen = False
                op_stack.push(char)
            elif char in '0123456789':
                if digit_seen:
                    val_stack.push(val_stack.pop() + char)
                else:
                    val_stack.push(char)
                digit_seen = True
            elif char in '+-/*':
                digit_seen = False
                while op_stack.getSize() and op_stack.peek() in '+-/*' and precedence[op_stack.peek()] >= precedence[char]:
                    val_stack.push(do_operation(val_stack.pop(), val_stack.pop(), op_stack.pop()))
                op_stack.push(char)
            elif char == ')':
                digit_seen = False
                while op_stack.peek() != '(':
                    val_stack.push(do_operation(val_stack.pop(), val_stack.pop(), op_stack.pop()))
                op_stack.pop()
        while op_stack.getSize():
            val_stack.push(do_operation(val_stack.pop(), val_stack.pop(), op_stack.pop()))
        return val_stack.pop()
    except:
        print('Incorrect arithmetic expression!')

# print(infix_evaluator('10 + 2 * 6'))
# print(infix_evaluator('100 * 2 + 12'))
# print(infix_evaluator('100 * ( 2 + 12 )'))
# print(infix_evaluator('100 * ( 2 + 12 ) / 14'))
# print(infix_evaluator('3 4 +'))

# Very basic calculator - cannot handle decimal operations

ans = ''
while(True):
    expr = input(f'-> {ans} ')
    if expr == 'clear':
        ans = ''
    elif expr == 'exit':
        exit(0)
    else:
        ans = infix_evaluator(str(ans) + expr)