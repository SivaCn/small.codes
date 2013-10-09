#! /usr/bin/python

"""Stack implementation Using Python.
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"


class Stack:
    """
        Class for the Stack datastructure.
    """
    def __init__(self):
        """
            Constructor.
        """
        self.stack = []

    def push(self, item=None):
        """
            push an element or a list of element to Stack.
        """
        if isinstance(item, list):
            for element in item:
                self.stack.insert(len(self.stack), element)
        else:
            self.stack.insert(len(self.stack), item)
        print self.stack

    def pop(self):
        """
            pop the top element from the stack.
        """
        if not self.isEmpty():
            return self.stack.remove(-1)
        return None

    def isEmpty(self):
        """
            Check if the stack is empty or not.
        """
        return self.stack == []

    def reverse(self):
        """
            Reverses the stack, Use it only when needed,
            this will alter the data structure.
        """
        low = 0
        high = -1
        li_len = len(self.stack)

        for low in xrange(li_len/2):
            
            high = -(low+1)
            temp = self.stack[low]
            self.stack[low] = self.stack[high]
            self.stack[high] = temp

        print self.stack

if __name__ == '__main__':
    """
    """
    obj = Stack()
    obj.push('hjhf')
    obj.push([1,2,3,4,5])
    obj.push(2)
    print obj.pop()
    obj.reverse()
