#! /usr/bin/python

"""
A program for matched paranthesis

{()()()[][()()]}

"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"

import re
import stack_linkedlist as stack

data = """
({{()()()[][()()]}})
"""

stack = stack.Stack()

def parse_data(data_list):
    """
    """
    default_tokens = {'}': '{', ']': '[', ')': '('}
    _list = [e.strip().strip('\n').strip() for e in data_list if e.strip() or e.strip('\n')]

##    for ele in _list:
##        print 'ele:', ele, 'stack.top():', stack.top()
##        if (ele in default_tokens.keys()) and (stack.top() == default_tokens[ele]):
##            popped = stack.pop()
##            print 'popped:', popped
##        elif (ele in default_tokens.values() and stack.top() != ele):
##            stack.push(ele)
##            print 'pushing:', ele
##        elif not stack.top():
##            stack.push(ele)
##            print 'pushing:', ele

    for ele in _list:
        if ele in default_tokens.keys():
            if stack.top() == default_tokens[ele]:
                popped = stack.pop()
                #print 'popping:', popped
            else:
                stack.push(ele)
                #print 'pushing:', ele
        else:
            stack.push(ele)
            #print 'pushing:', ele

    print 'Stack:', stack._print()
    if stack.top():
        print 'Not Balanced'
    else:
        print 'Balanced'

if __name__ == '__main__':
    """
    """
    parse_data(list(data))    
