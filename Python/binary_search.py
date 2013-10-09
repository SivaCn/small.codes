#! /usr/bin/python

"""
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"


class Binary:
    def __init__(self, _list):
        self._list = _list
        self.indices = []
        self.temp_list = []
        self.mid = None

    def search(self, item):

        self.indices = [ele for ele in xrange(len(self._list))]

        i = 0
        while True:
            _len = len(self._list)
            if _len %2 == 0:
                mid = len(self._list) / 2
            else:
                mid = len(self._list) / 2 + 1
            mid = mid - 1
            #print 'mid:', mid, 'self._list[mid]:', self._list[mid]

            if self._list[mid] == item:
                print 'found'
                break
            elif self._list[mid] > item:
                self._list = self._list[:mid]
                print mid, self._list
            elif self._list[mid] < item:
                self._list = self._list[mid:]

            #print 'iter:', i
            i = i +1
            print self._list

if __name__ == '__main__':

    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, 45, 68, 666]
    #print testlist
    obj = Binary(testlist)
    obj.search(32)
