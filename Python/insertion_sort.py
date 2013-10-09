#! /usr/bin/python

"""Insertin Sort Using Python.
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"

def in_sort(l):
    for idx, e in enumerate(l[:-1]):
        if l[idx] > l[idx+1]:
            for rev in range(0, idx+1):
                _temp = l[idx+1]
                if l[rev] > _temp:
                    l.remove(l[idx+1])
                    l.insert(rev, _temp)

    return l

if __name__ == "__main__":
    """."""
    inp = [5,4,3,2,1,0,-100,-50]
    print inp
    print in_sort(inp)
