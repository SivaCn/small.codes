#! /usr/bin/python

"""
Another example of the parentheses matching problem comes from hypertext
markup language (HTML). In HTML, tags exist in both opening and closing
forms and must be balanced to properly describe a web document.
This very simple HTML document:

    <html>
       <head>
          <title>
             Example
          </title>
       </head>
            
       <body>
          <h1>Hello, world</h1>
       </body>
    </html>

is intended only to show the matching and nesting structure for tags in
the language. Write a program that can check an HTML document for proper
opening and closing tags.

"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"


import re
import stack_linkedlist as stack

data = """
<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>
"""

stack = stack.Stack()

def stack_oper(tag):
    """
    """
    close_tag = list(tag)
    if close_tag[1] == '/':
        close_tag.remove('/')
    close_tag = ''.join(close_tag)

    if stack.isEmpty():
        stack.push(tag)
        
    else:
        if stack.top() and (stack.top() != close_tag):
            stack.push(tag)

        elif stack.top() and (stack.top() == close_tag):
            stack.pop()

def parse_html(data):
    """
    """
    data = [ele.strip() for ele in data if ele.strip()]
    data = ''.join(data)

    tok_start = False
    tag = []

    i = 0
    try:
        while data[i]:
            if '<' == data[i]:
                tok_start = True
                tag = []
            if tok_start:
                tag.append(data[i])

            if '>' == data[i]:
                html_tag = ''.join(tag)
                stack_oper(html_tag)
                tok_start = False
            i += 1

    except IndexError:
        ## Reached the end of the String
        ## Actually not an Error
        pass

    if stack.isEmpty():
        ## Stack is Empty since all the tags were matched
        print 'PROPER HTML FILE'
    else:
        print 'IMPROPER HTML FILE'

if __name__ == '__main__':
    """
    """
    parse_html(data.splitlines())
    
