#! /usr/bin/python

"""Queue implementation Using Python.
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"


class Queue:
    """
        Class for the Linear queue datastructure.
    """
    def __init__(self, queue=None):
        """
            Constructor.
        """
        self.queue = queue
        if self.queue != []:
            self.front = 0
            self.rear = len(self.queue)
        else:
            self.front = None
            self.rear = None

    def enqueue(self, item=None):
        """
            enqueue an element or a list of element to queue.
        """
        if isinstance(item, list):
            for element in item:
                self.queue.insert(len(self.queue), element)
        else:
            self.queue.insert(self.rear, item)
            self.rear += 1
        print self.queue

    def dequeue(self):
        """
            dequeue the top element from the queue.
        """
        if not self.isEmpty():
            item = self.queue[0]
            self.queue = self.queue[1:]
            return item
        return None

    def isEmpty(self):
        """
            Check if the queue is empty or not.
        """
        return self.queue == []

    def reverse(self):
        """
            Reverses the queue, Use it only when needed,
            this will alter the data structure.
        """
        low = 0
        high = -1
        li_len = len(self.queue)

        for low in xrange(li_len/2):
            
            high = -(low+1)
            temp = self.queue[low]
            self.queue[low] = self.queue[high]
            self.queue[high] = temp

if __name__ == '__main__':
    """
    """
    obj = Queue([1,2,3,4,5])
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    print obj.dequeue()
    print obj.queue
    print obj.dequeue()
    print obj.queue 
    obj.reverse()
    print obj.queue 
