#! /usr/bin/python

###############################################################################
# A Bubble sort Program
###############################################################################

""" *** Bubble Sort *** """

# -*- coding: utf-8 -*-

## ------ Built-in Imports ------ ##

## ------ Built-in Imports ------ ##

__all__ = ['Search']

__author__ = r'Siva Cn (http://www.cnsiva.com)'


def bsort(_list):
    
    for i in xrange(len(_list) - 1):
        for j in xrange(len(_list) - 1):
            if _list[j] > _list[j+1]:
                _temp = _list[j]
                _list[j] = _list[j+1]
                _list[j+1] = _temp

    return _list

if __name__ == "__main__":
    """."""
    inp = [4, 5, 2, 6, -200]
    print bsort(inp)

