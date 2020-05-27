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
        
        for i in range(self.array_size):
            self.table[i] = SinglyLinkedList()

    def hash_function(self, key):
        return sum([ord(c) for c in key]) % self.array_size

    def key_exists(self, key): 
        idx = self.hash_function(key)   
        it = self.table[idx].iterator()
        while it.has_next():
            cur_item = it.next()
            if cur_item.get_key() == key:
                return True
    
    def size(self): 
        return self.num_items

    def is_full(self): 
        if self.num_items == 0:
            return False
        return (self.num_items / self.array_size) >= 0.3

    def get(self, key):
        idx = self.hash_function(key)
        it = self.table[idx].iterator()
        while it.has_next():
            cur_item = it.next()
            if cur_item.get_key() == key:
                return cur_item.get_value()
        raise NoSuchElementException()

    def insert(self, key, value): 
        if self.key_exists(key):
            raise DuplicatedKeyException()
        idx = self.hash_function(key)
        item = Item(key, value)
        self.table[idx].insert_last(item)
        self.num_items += 1
                
    def update(self, key, value):
        idx = self.hash_function(key)
        it = self.table[idx].iterator()
        while it.has_next():
            cur_item = it.next()
            if cur_item.get_key() == key:
                return cur_item.set_value(value)
        
    def remove(self, key):
        if not self.key_exists(key):
            raise NoSuchElementException()
        collision_list = self.table[self.hash_function(key)]
        it = collision_list.iterator()
        while it.has_next():
            pos = 0
            cur_item = it.next()
            if cur_item.get_key() == key:
                return collision_list.remove(pos)
            cur_item = cur_item.net()
            pos += 1
        
    def keys(self):
        for idx in range(self.array_size):  
            colision_list = self.table[idx]
            it = colision_list.iterator()
            while it.has_next():
                cur_item = it.next()
                if cur_item.get_key():
                    print(cur_item.get_key())
        
    def values(self): 
        for idx in range(self.array_size):  
            colision_list = self.table[idx]
            it = colision_list.iterator()
            while it.has_next():
                cur_item = it.next()
                if cur_item.get_key():
                    print(cur_item.get_value())

    def items(self): 
        for idx in range(self.array_size):  
            colision_list = self.table[idx]
            it = colision_list.iterator()
            while it.has_next():
                cur_item = it.next()
                if cur_item.get_key():
                    print(f'{cur_item.get_key()}: {cur_item.get_value()}')