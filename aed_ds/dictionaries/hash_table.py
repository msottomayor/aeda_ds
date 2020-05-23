from .tad_dictionary import Dictionary
from .item import Item
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList

class HashTable(Dictionary):

    def __init__(self, size=101):
        self.num_items = 0
        self.list_keys = SinglyLinkedList()
        self.lenght = size

    def hash_function(self, key):
        return hash(key)

    def size(self):
        return self.num_items

    def is_full(self):
        return self.size() == self.lenght

    # Returns the value associated with key k.
    # Throws NoSuchElementException
    def get(self, k): pass

    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException
    def insert(self, k, v):
        if self.list_keys.find(k) != -1:
            raise DuplicatedKeyException()
        self.list_keys.insert_last(k)
        key = self.hash_function(k)
        new_item = Item(key, v)        
        self.num_items += 1

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
