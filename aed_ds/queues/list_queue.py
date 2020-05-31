from .tad_queue import Queue
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import FullQueueException, EmptyQueueException

class ListQueue(Queue):
    def __init__(self, limit=15):
        self.queue = SinglyLinkedList
        self.num_elements = 0
        self.limit = limit
    
    def is_empty(self): 
        return self.num_elements == 0

    def is_full(self): 
        return self.num_elements == self.limit

    def size(self): 
        return self.num_elements

    def enqueue(self, element): 
        if self.is_full():
            raise FullQueueException()
        return self.queue.insert_last(element)

    def dequeue(self): 
        if self.is_empty():
            raise EmptyQueueException()
        return self.queue.remove_first(element)
