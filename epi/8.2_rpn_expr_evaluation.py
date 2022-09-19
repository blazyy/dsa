def evaluate_rpn(expression):
    results = []
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '/': lambda y, x: x / y,
        '*': lambda y, x: x * y,
    }
    for token in expression:
        if token in OPERATORS:
            results.append(OPERATORS[token](results.pop(), results.pop()))
        else:
            results.append(int(token))
    return results[-1]


'''
The algorithm below for parsing polish notation expression (pre-fix), is pretty easy.
For the first operation (2 operands and an operator), the order is N -> N -> O when
popped from stack (number -> number -> operator). For every other consequent
operation, the order is N -> O -> N. Depending on the order, we basically just do
the same thing as we did for reverse polish notation.
'''


def evaluate_pn(expression):
    results = []
    second_operation = False
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '/': lambda y, x: x / y,
        '*': lambda y, x: x * y,
    }

    for token in expression:
        results.append(token)
        if len(results) == 3:
            if not second_operation:
                second_operation = True
                op2, op1, operator = results.pop(), results.pop(), results.pop()
            else:
                op2, operator, op1 = results.pop(), results.pop(), results.pop()
            results.append(OPERATORS[operator](int(op1), int(op2)))
    return results[-1]


print(evaluate_rpn('34+2*1+'))
print(evaluate_pn('+34*2+1'))
