#! /usr/bin/python

"""Stack implementation (Linked List) Using Python.
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"

class node:
    def __init__(self):
        self.data = None
        self.next = None

class Stack:
    def __init__(self):
        self.cur_node = None

    def isEmpty(self):
        return self.cur_node == None

    def top(self):
        """
        """
        if self.cur_node:
            return self.cur_node.data
        else:
            return None

    def push(self, data):
        new_node = node()
        new_node.data = data
        new_node.next = self.cur_node
        self.cur_node = new_node

    def pop(self):
        if self.cur_node:
            data = self.cur_node.data
            self.cur_node = self.cur_node.next
            return data
        else:
            return None

    def _print(self):
        node = self.cur_node
        while node:
            print node.data, 
            node = node.next

if __name__ == '__main__':
    """
    """
    ll = Stack()
    print ll.isEmpty()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll._print()
    print 'popped', ll.pop()
    ll._print()
    print 'popped', ll.pop()
    ll._print()
    print 'popped', ll.pop()
    ll._print()
    print 'popped', ll.pop()
    ll._print()
    print 'popped', ll.pop()
    ll._print()
    print 'popped', ll.pop()
    ll._print()
    print 'popped', ll.pop()
    ll._print()
