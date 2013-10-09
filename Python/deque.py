#! /usr/bin/python

"""Deque implementation Using Python.
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"


class Deque:
    """
        Class for the double ended queue datastructure.
    """
    def __init__(self, queue=None):
        """
            Constructor.
        """
        self.queue = []
        self.front = 0
        self.rear = -1

        if not queue:
            self.queue = []

        if isinstance(queue, list):
            for ele in queue:
                self.queue.insert(len(queue), ele)

        if isinstance(queue, (int, float, str, bool)):
            self.queue = queue

        if self.queue:
            self.front = 0
            self.rear = len(self.queue)

    def _print(self):
        """
        """
        print 'queue:', self.queue, ', front:', self.front, ', rear:', self.rear

    def insert_rear(self, item=None):
        """
            insert an element or a list of element to the rear of the queue.
        """
        if isinstance(item, list):
            for element in item:
                self.queue.insert(len(self.queue), element)
                self.rear += 1
                self._print()
        else:
            self.queue.insert(self.rear, item)
            self.rear += 1
            self._print()

    def insert_front(self, item=None):
        """
            insert an element or a list of element to the front of the queue.
        """
        if isinstance(item, list):
            item = item[::-1]
            for element in item:
                self.queue.insert(self.front, element)
                self.rear += 1
                self._print()
        else:
            self.queue.insert(self.front, item)
            self.rear += 1
            self._print()

    def remove_front(self):
        """
            remove an element from the front of the queue.
        """
        if not self.isEmpty():
            item = self.queue[0]
            self.queue = self.queue[1:]
            self.rear -= 1
            self._print()
            return item

        self._print()
        return None

    def remove_rear(self):
        """
            remove an element from the rear of the queue.
        """
        if not self.isEmpty():
            item = self.queue[-1]
            self.queue = self.queue[:-1]
            self.rear -= 1
            self._print()
            return item

        self._print()
        return None

    def isEmpty(self):
        """
            Check if the queue is empty or not.
        """
        return self.queue == []

if __name__ == '__main__':
    """
    """
    obj = Deque()
    obj._print()
    #obj.insert_rear([6,7,8])
    obj.insert_rear(2)
    obj.insert_rear(3)
    obj.insert_rear(4)
    obj.insert_rear(5)
    obj.insert_front(['c', 8, 9])
    print obj.remove_front()
    print obj.remove_rear()
##    obj._print()

    """
    ## Sample output
    queue: [] , front: 0 , rear: -1
    queue: [2] , front: 0 , rear: 0
    queue: [3, 2] , front: 0 , rear: 1
    queue: [3, 4, 2] , front: 0 , rear: 2
    queue: [3, 4, 5, 2] , front: 0 , rear: 3
    queue: [9, 3, 4, 5, 2] , front: 0 , rear: 4
    queue: [8, 9, 3, 4, 5, 2] , front: 0 , rear: 5
    queue: ['c', 8, 9, 3, 4, 5, 2] , front: 0 , rear: 6
    queue: [8, 9, 3, 4, 5, 2] , front: 0 , rear: 5
    c
    queue: [8, 9, 3, 4, 5] , front: 0 , rear: 4
    2
    """
