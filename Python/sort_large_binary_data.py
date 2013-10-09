#! /usr/bin/python

"""Sorting a larger collection of 0's and 1's.

eg [1, 0, 1, 0,1, 0, 1, 0,1, 0, 1, 0,.....1, 0, 1, 0,]
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"


class Sort():
    """
    """
    def __init__(self):
        """
        """
        pass

    def quick_sort(self, l):
        """
        """
        less = []
        pivotList = []
        more = []
        
        if len(l) <= 1:
            return l

        else:
            pivot = l[0]
##            print l
##            print pivot
            for ele in l:
                if ele < pivot:
                    less.append(ele)
                elif ele > pivot:
                    more.append(ele)
                else:
                    pivotList.append(ele)
            
            less = self.quick_sort(less)
            more = self.quick_sort(more)

##            print less, pivotList, more
            return less + pivotList + more

if __name__ == "__main__":
    """
    """
    inp = [1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,1]

##    inp = [1, 4, 0, 2, 5, -2]

    print Sort().quick_sort(inp)
