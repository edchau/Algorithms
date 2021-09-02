"""
Reverse Stack using Recursion
"""

def reverse_stack(stack):
    if len(stack) != 0:
        val = stack.pop()
        reverse_stack(stack)
        push_to_stack(stack, val)

def push_to_stack(stack, val):
    if len(stack) == 0:
        stack.append(val)
        return
    
    # need to pop off current top
    # before adding value to 
    # reverse the stack
    top = stack.pop()
    push_to_stack(stack, val)
    stack.append(top)

stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)
