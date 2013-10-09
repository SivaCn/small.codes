#! /usr/bin/python

###############################################################################
# Simple String reverse (An Efficient Way)
###############################################################################

"""
    Reverse a String in Python.
"""

## ------ Built-in Imports ------ ##
## ------ Built-in Imports ------ ##

__all__ = ['Search']

__author__ = r'Siva Cn (http://www.cnsiva.com)'

class Str():
    def __init__(self, _str):
        self.input = _str

    def reverse(self):
        _list = list(self.input)
        for i in xrange(len(_list)/2):
            _temp = _list[i]
            _list[i] = _list[-(i+1)]
            _list[-(i+1)] = _temp
        return ''.join(_list)

if __name__ == "__main__":
    """."""
    inp = "Siva Cn"
    obj = Str(inp)
    print obj.reverse()

