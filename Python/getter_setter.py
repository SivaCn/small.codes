#! /usr/bin/python

"""Python Getter and Setter @property.
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"


class C(object):
    def __init__(self):
        self._x = [1,2,3,4,5]

    @property
    def x(self):
        """I'm the 'x' property."""
        print "getter of x called"
        return self._x

    @x.setter
    def x(self, value):
        print "setter of x called"
        self._x.append(value)

    @x.deleter
    def x(self):
        print "deleter of x called"
        print 'popped', self._x.pop()


obj = C()
obj.x = 20
print obj.x
del obj.x
print obj.x
del obj.x
