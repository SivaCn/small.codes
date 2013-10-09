#! /usr/bin/python

"""
Convert the following values to binary using (divide by 2)
Show the stack of remainders.
    17
    45
    96
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"

import linked_list

def generate_bin(int_val):
    """
    """
    obj = linked_list.linked_list()
    while True:
        rem = (int_val/2)
        mod = (int_val % 2)
        int_val = rem
        obj.add_node(mod)
        print 'mod: ', mod, 'rem', rem, 'int_val', int_val
        if int_val == 0:
            break

    print obj.list_print()

if __name__ == '__main__':
    """
    """
    int_val = int(raw_input('Integer: '))
    generate_bin(int_val)
    
