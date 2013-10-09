#! /usr/bin/python

"""Selection Sort Using Python.
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"

def sel_sort(l):
    for i in xrange(len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                _temp = l[i]
                l[i] = l[j]
                l[j] = _temp
        print l

    return l  

if __name__ == "__main__":
    """."""
    inp = [3, 2, 5, 0, 1]
    print sel_sort(inp)
