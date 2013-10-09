#! /usr/bin/python

"""Simple Linked List implementation Using Python.
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"


class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node

class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print node.data
            node = node.next

if __name__ == "__main__":
    """."""
    ll = linked_list()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(5)

    ll.list_print()
