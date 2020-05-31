import unittest

from .test_stack import TestStack
from aed_ds.stacks.list_stack import ListStack
from aed_ds.exceptions import EmptyListException, InvalidPositionException
from aed_ds.lists.singly_linked_list import SinglyLinkedList


class TestListStack(TestStack, unittest.TestCase):
    def build_stack(self):
        self.stack = ListStack()
    
    def setUp(self):
        self.build_stack()