#! /usr/bin/python

###############################################################################
# String Reverse Module
###############################################################################

"""String Reverse Using Stack (Linked List)."""

# -*- coding: utf-8 -*-

## ------ Built-in Imports ------ ##
## ------ Built-in Imports ------ ##

__all__ = ['Search']
__author__ = r'Siva Cn (http://www.cnsiva.com)'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, stack_size=10):
        self.stack_size = stack_size
        self.start = None
        self.size = 0

    def push(self, item=None):
        if self.size == self.stack_size:
            print "Stack is Full"
            return False

        _temp = Node(item)
        _temp.next = self.start
        self.start = _temp
        self.size += 1

    def pop(self):
        if self.size != 0:
            _item = self.start.data
            _temp_link = self.start
            self.start = self.start.next
            del _temp_link
            self.size -= 1
            return _item
        else:
            return None

    def peek(self):
        if self.start:
            return self.start.data
        else:
            return None

    def show(self):
        walker = self.start
        while walker:
            print walker.data, 
            walker = walker.next

if __name__ == "__main__":
    """."""
    stack_size = 100
    obj = Stack(stack_size)

    for ele in list(raw_input()):
        obj.push(ele)

    #obj.show()

    _list = []
    for ele in xrange(stack_size):
        _item = obj.pop() 
        if _item:
            _list.append(_item)
        else: break

    print ''.join(_list)


