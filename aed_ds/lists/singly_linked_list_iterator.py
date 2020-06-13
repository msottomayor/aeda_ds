from ..exceptions import *
from ..tad_iterator import Iterator
from aed_ds.exceptions import EmptyListException, NoSuchElementException

class SinglyLinkedListIterator(Iterator):
    def __init__(self, singly_linked_list):
        self.singly_linked_list = singly_linked_list
        self.rewind()

    def has_next(self):
        return self.current_node != None

    def next(self):
        if not self.has_next():
            raise NoSuchElementException()
        element = self.current_node.get_element()
        self.current_node = self.current_node.get_next()
        return element

    def rewind(self):
        self.current_node = self.singly_linked_list.head
