def insert_at_bottom(stack, item):

    if not stack:

        stack.append(item)

    else:

        top = stack.pop()

        insert_at_bottom(stack, item)

        stack.append(top)

def reverse_stack(stack):

    if stack:

        top = stack.pop()

        reverse_stack(stack)

        insert_at_bottom(stack, top)

# Example usage

stack = [1, 2, 3, 4, 5]

print("Original stack:", stack)

reverse_stack(stack)

print("Reversed stack:",stack)