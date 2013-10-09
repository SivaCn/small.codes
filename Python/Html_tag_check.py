#! /usr/bin/python

###############################################################################
# HTML tag nesting Checker
###############################################################################

"""HTML checking Tag Nesting."""

# -*- coding: utf-8 -*-

## ------ Built-in Imports ------ ##
import re
## ------ Built-in Imports ------ ##

__all__ = ['Search']

__author__ = r'Siva Cn (http://www.cnsiva.com)'

class Nest:
    def __init__(self, inp):
        self.inp = inp
        self.stack = []

    def check(self):
        self.inp = self.inp.replace(">", "> ").replace("<", " <")
        self.inp = self.inp.splitlines()
        self.inp = [
                    inner_ele.strip() \
                    for ele in self.inp \
                    for inner_ele in ele.split(" ") \
                    if inner_ele.strip()
                    ]

        pat = re.compile("<(.*)>")

        for ele in self.inp:
            match_obj = re.search(pat, ele)
            if match_obj:
                matched_str = match_obj.group()
                if not '/' in matched_str:
                    self.stack.append(matched_str)
                else:
                    _item = self.stack.pop()
                    if _item != matched_str.replace("/", ""):
                        return False
        return True

if __name__ == "__main__":
    """."""
    sample = """<html>
       <head>
          <title>
             Example
          </title>
       </head>

       <body>
          <h1>Hello, world</h1>
       </body>
    </html>"""

    obj = Nest(sample)
    print "Result: ", obj.check()

