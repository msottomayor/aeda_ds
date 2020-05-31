from .tad_stack import Stack
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyStackException, FullStackException

class ArrayStack(Stack):
    # Returns true iff the stack contains no elements.
    def is_empty(self): pass

    # Returns true iff the stack cannot contain more elements.
    def is_full(self): pass

    # Returns the number of elements in the stack.
    def size(self): pass

    # Returns the element at the top of the stack.
    # Throws EmptyStackException
    def top(self): pass

    # Inserts the specified element onto the top of the stack.
    # Throws FullStackException
    def push(self, element): pass

    # Removes and returns the element at the top of the stack.
    # Throws EmptyStackException
    def pop(self): pass
