def is_well_formed_single(expression):
    count = 0
    for token in expression:
        if token == '(':
            count += 1
        else:
            count -= 1
    return count == 0


def is_well_formed(expression):
    stack = []
    lookup = {'(': ')', '{': '}', '[': ']'}
    for token in expression:
        if token in lookup:
            stack.append(token)
        else:
            if not stack or token != lookup[stack.pop()]:
                return False
    return not stack


print(is_well_formed_single('()()()'))
print(is_well_formed_single('(())'))
print(is_well_formed_single('(()'))
print(is_well_formed_single('(((((('))

print(is_well_formed('()[]{}'))
print(is_well_formed('([{}])'))
print(is_well_formed('([[]{}])'))
print(is_well_formed('([[{})'))