# we can use the LIFO protocol to reverse a data sequence
import stack

def reverse_file(filename):
    new_stack = stack.Stack()
    with open(filename, "r") as f:
        for line in f:
            new_stack.push(line.rstrip("\n"))

    with open(filename, "w") as second:
        while not stack.is_empty():
            second.write(new_stack.pop() + "\n")

c