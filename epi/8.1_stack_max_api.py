'''
Design a stack that includes a max operation, in addition to push and pop. The max method should
return the maximum value stored in the stack.

Hint: Use additional storage to track the maximum value.
'''

'''
Notes for future self:

This solution is good for stacks where number of distinct values is small.
Of course, also works for other situations but is especially optimized for stacks
where a lot of the numbers are repeated.
'''

class MaxStack:
    class MaxWithCount:
        def __init__(self, val):
            self.val = val
            self.count = 1

        def __repr__(self):
            return f'{self.val}:{self.count}'

    def __init__(self):
        self.items = []
        self.max_vals = []

    def empty(self):
        return len(self.items) == 0

    def push(self, val):
        if len(self.max_vals) == 0 or val > self.max_vals[-1].val:
            self.max_vals.append(self.MaxWithCount(val))
        elif val == self.max_vals[-1].val:
            self.max_vals[-1].count += 1
        self.items.append(val)

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        if self.items[-1] == self.max_vals[-1].val:
            if self.max_vals[-1].count == 1:
                self.max_vals.pop()
            else:
                self.max_vals[-1].count -= 1
        self.items.pop()

    def max(self):
        return self.max_vals[-1].val

ms = MaxStack()

[ms.push(val) for val in [2, 2, 1, 4, 5, 5, 3]]
ms.pop()
ms.pop()
ms.pop()
ms.pop()
ms.push(0)
ms.push(3)

print('Stack: ', ms.items)
print('Aux Stack: ', ms.max_vals)