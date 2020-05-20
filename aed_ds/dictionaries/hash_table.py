from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList

class HashTable(Dictionary):
    def __init__(self, size=101):
        self.num_items = 0
        self.keys = SinglyLinkedList()

    # Returns the number of elements in the dictionary.
    def size(self): pass

    # Returns true if the dictionary is full.
    def is_full(self): pass

    # Returns the value associated with key k.
    # Throws NoSuchElementException
    def get(self, k): pass

    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException
    def insert(self, k, v): pass

    # Updates the value associated with key k.
    # Throws NoSuchElementException
    def update(self, k, v): pass

    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    def remove(self, k): pass

    # Returns a List with all the keys in the dictionary.
    def keys(self): pass

    # Returns a List with all the values in the dictionary.
    def values(self): pass

    # Returns a List of lists, with all the key value pairs in the dictionary.
    def items(self): pass
