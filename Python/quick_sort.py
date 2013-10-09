#! /usr/bin/python

"""Quick Sort Using Python.
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"


def quick_sort(l):
    less = []
    pivotList = []
    more = []
    
    if len(l) <= 1:
        return l

    else:
        pivot = l[0]
        for ele in l:
            if ele < pivot:
                less.append(ele)
            elif ele > pivot:
                more.append(ele)
            else:
                pivotList.append(ele)

        less = quick_sort(less)
        more = quick_sort(more)
        
        return less + pivotList + more

inp = [3, 1, 0, -30, -50, 100]
print quick_sort(inp)
