from .tad_stack import Stack
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyStackException, FullStackException

class ListStack(Stack):
    def __init__(self, limit=15):
        self.stack = SinglyLinkedList
        self.num_elements = 0
        self.limit = limit

    def is_empty(self): 
        return self.num_elements == 0

    def is_full(self): 
        return self.num_elements == self.limit

    def size(self): 
        return self.num_elements

    def top(self):
        if self.is_empty():
            raise EmptyStackException()
        return self.stack.get_last()

    def push(self, element):
        if self.is_full():
            raise FullStackException()
        return self.stack.insert_last(element)

    def pop(self):
        if self.is_empty():
            raise EmptyStackException()
        return self.stack.remove_last()

