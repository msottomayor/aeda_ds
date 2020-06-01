from .tad_stack import Stack
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyStackException, FullStackException

import ctypes

class ArrayStack(Stack):
    def __init__(self,limit=None):
        self.limit = limit
        self.stack = (ctypes.py_object * self.limit)()

    # Returns true iff the stack contains no elements.
    def is_empty(self): 
        return self.stack[0] == None

    # Returns true iff the stack cannot contain more elements.
    def is_full(self): pass

    # Returns the number of elements in the stack.
    def size(self): 
        return 8

    # Returns the element at the top of the stack.
    # Throws EmptyStackException
    def top(self): pass

    # Inserts the specified element onto the top of the stack.
    # Throws FullStackException
    def push(self, element): pass

    # Removes and returns the element at the top of the stack.
    # Throws EmptyStackException
    def pop(self): pass


if __name__ == "__main__":
    stack = ArrayStack(10)
    for i in range(self.size()):
        print(stack[i])