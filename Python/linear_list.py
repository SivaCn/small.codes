#! /usr/bin/python

"""Python Linear Linked List.
"""

# -*- coding: utf-8 -*-

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Meta:
    def __init__(self):
        self.root = None
        self.smaller = 0
        self.higher = 0

class BST:
    def __init__(self, root):
        self.tree = Meta()
        _root = Node(root)
        self.tree.root = _root
        self.smaller = root
        self.higher = root

    def insert(self, data):
        _temp = Node(data)
        walker = self.tree.root
        
        walk_par = walker
        
        while walker:
            '''
            if walker.data >= data:
                walker = walker.left
            else:
                walker = walker.right
            '''
            walk_par = walker
            walker = walker.right
        walk_par.right = _temp

    def print_tree(self):
        walker = self.tree.root
        if walker:
            print walker.data
            walker = walker.right

if __name__ == "__main__":
    tree = BST(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(25)
    tree.insert(1)
    tree.insert(3)
    tree.print_tree()

