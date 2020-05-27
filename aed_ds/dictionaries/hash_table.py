from .tad_dictionary import Dictionary
from .item import Item
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList

import ctypes

class HashTable(Dictionary):
    def __init__(self, size=101):
        self.num_items = 0
        self.array_size = size
        self.table = (ctypes.py_object * self.array_size)()
        
        for idx in range(self.array_size):
            self.table[idx] = SinglyLinkedList()

    def hash_function(self, key):
        return sum([ord(c) for c in key]) % self.array_size

    # Returns true if key already exists
    def key_exists(self, key): 
        idx = self.hash_function(key)   
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            cur_item = it.next()
            if cur_item.get_key() == key:
                return True
    
    # Returns the number of elements in the dictionary.
    def size(self): 
        return self.num_items

    # Returns true if the dictionary is full.
    def is_full(self): 
        if self.num_items == 0:
            return False
        return (self.num_items / self.array_size) >= 0.3

    # Returns the value associated with key k.
    # Throws NoSuchElementException
    def get(self, key):
        idx = self.hash_function(key)
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            cur_item = it.next()
            if cur_item.get_key() == key:
                return cur_item.get_value()
        raise NoSuchElementException()

    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException
    def insert(self, key, value): 
        if self.key_exists():
            raise DuplicatedKeyException()
        idx = self.hash_function(key)
        item = Item(key, value)
        self.table[idx].insert_last(item)
        self.num_items += 1
                
    # Updates the value associated with key k.
    # Throws NoSuchElementException
    def update(self, key, value): pass

    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    def remove(self, key): pass

    # Returns a List with all the keys in the dictionary.
    def keys(self): pass

    # Returns a List with all the values in the dictionary.
    def values(self): pass

    # Returns a List of lists, with all the key value pairs in the dictionary.
    def items(self): pass