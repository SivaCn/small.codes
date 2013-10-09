#! /usr/bin/python

###############################################################################
# Simple String reverse (with more complexity)
###############################################################################

"""
    Reverse a String in Python.

    Write an iterative function to reverse a string.
    Do the same thing as a recursive function.
"""

## ------ Built-in Imports ------ ##
## ------ Built-in Imports ------ ##

__all__ = ['Search']

__author__ = r'Siva Cn (http://www.cnsiva.com)'


class Stuff():
    def __init__(self, data):
        self.data = data
        self.out = []
        print self.data

    def reverse(self):
        try:
            _temp = self.data[0]
            self.data = self.data[1:]
        except IndexError:
            return

        self.out.insert(0, _temp)
        self.reverse()
        
        return ''.join(self.out)

if __name__ == "__main__":
    """."""
    inp = "Sivakumar C N"

    obj = Stuff(inp)
    print obj.reverse()
