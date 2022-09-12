from stack import Stack

'''
A valid postfix expression will have:
1) n operators with n + 1 operands.
2) first two elements which are operands followed by an operator
'''

def eval_postfix_handle_error(expr):
    stack = Stack()
    counter = 0
    incorrect = False
    for char in expr:
        if char == ' ':
            continue
        elif char in '+-/*':
            if stack.getSize() < 2:
                incorrect = True
                break
            op1 = stack.pop()
            op2 = stack.pop()
            counter -= 1
            if char == '+':
                stack.push(op2 + op1)
            elif char == '-':
                stack.push(op2 - op1)
            elif char == '*':
                stack.push(op1 * op2)
            elif char == '/':
                stack.push(op2 / op1)
        else:
            stack.push(int(char))
            counter += 1
    if counter != 1 or incorrect:
        return 'Invalid expression'
    return stack.pop()

print(eval_postfix_handle_error('7 8 + 3 2 + /'))
print(eval_postfix_handle_error('7 8 9 2 + 3 2 + / '))
print(eval_postfix_handle_error('7 8 + 3 2 + / /'))
print(eval_postfix_handle_error('7 8 + 3 2 + / 3'))
