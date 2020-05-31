from .tad_queue import Queue
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import FullQueueException, EmptyQueueException

class ArrayQueue(Queue):
    # Returns true iff the queue contains no elements.
    def is_empty(self): pass

    # Returns true iff the queue cannot contain more elements.
    def is_full(self): pass

    # Returns the number of elements in the queue.
    def size(self): pass

    # Inserts the specified element at the rear of the queue.
    # Throws FullQueueException
    def enqueue(self, element): pass

    # Removes and returns the element at the front of the queue.
    # Throws EmptyQueueException
    def dequeue(self): pass