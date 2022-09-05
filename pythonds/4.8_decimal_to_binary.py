from stack import Stack

def decimal_to_base(number, base):
    stack = Stack()
    digits = '0123456789ABDCDEF'
    while number:
        stack.push(number % base)
        number //= base
    ans = []
    while not stack.isEmpty():
        ans.append(digits[stack.pop()])
    return ''.join(ans)

print(decimal_to_base(25, 2))
print(decimal_to_base(25, 16))
print(decimal_to_base(262121, 8))