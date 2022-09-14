from stack import Stack

'''
A valid postfix expression will have:
1) n operators with n + 1 operands.
2) first two elements which are operands followed by an operator
We can check the first condition using a counter.
The second condition can be validated using an if condition. When an operator
is seen and there aren't 2 operands, break code immediately, return false.
We only need to check for operators in the 2nd condition here because operands
are taken into account by the counter.
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
