#! /usr/bin/python

"""Circular Queue implementation Using Python.
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"


class CircularQueue:
    """
        Class for the Linear queue datastructure.
    """
    def __init__(self, queue=None, queue_size=10):
        """
            Constructor.
        """
        self.queue = queue
        self.queue_size = queue_size
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
            
            if len(self.queue) == self.queue_size:
                print 'Queue is full'
                return False
            if self.rear + 1 == self.queue_size:
                self.rear = 0

            print self.rear
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
            self.front -= 1
            return item
        return None

    def isEmpty(self):
        """
            Check if the queue is empty or not.
        """
        return self.queue == []

if __name__ == '__main__':
    """
    """
    obj = CircularQueue([1,2,3,4,5])
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    print obj.dequeue()
    print obj.queue
    print obj.dequeue()
    print obj.queue 
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
