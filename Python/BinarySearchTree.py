#! /usr/bin/python

"""Binary Search Tree
An Independent Binary Search Tree Program with three ways of
traversals (inorder, preorder and postorder)
"""

# -*- coding: utf-8 -*-

__all__ = ['BST']

__author__ = "Siva Cn (cnsiva.in@gmail.com)"
__website__ = "http://www.cnsiva.com"
__copyright__ = "Copyright (c) 2013 www.cnsiva.com"

class Node:
    """Referential Structure used to create new nodes"""
    def __init__(self, data):
        """Constructor."""
        self.data = data
        self.left = None
        self.right = None


class Meta:
    """A meta class contains info about the tree at any
    moment.
    """
    def __init__(self):
        """Constructor."""
        self.root = None
        self.size = 0
        self.small = 0
        self.big = 0


class BST:
    def __init__(self, root):
        """Constructor."""
        self.tree = Meta()
        _root = Node(root)
        self.tree.root = _root
        self.tree.size += 1
        self.tree.small = root

    def insert(self, data):
        """Insert a new node with in the tree.
        """
        _temp = Node(data)
        walker = self.tree.root

        while walker:
            if walker.data > data:
                if walker.left:
                    walker = walker.left
                else:
                    walker.left = _temp
                    break
            else:
                if walker.right:
                    walker = walker.right
                else:
                    walker.right = _temp
                    break
        self.tree.size += 1

        if self.tree.small > data:
            self.tree.small = data
        if self.tree.big < data:
            self.tree.big = data

    def show_inorder(self, walker=None):
        """Display the Tree as it traverses LEFT -> ROOT -> RIGHT."""
        if not walker:
            walker = self.tree.root

        if walker.left: self.show_inorder(walker.left)
        print walker.data, 
        if walker.right: self.show_inorder(walker.right)

    def show_preorder(self, walker=None):
        """Display the Tree as it traverses ROOT -> LEFT -> RIGHT."""
        if not walker:
            walker = self.tree.root

        print walker.data, 
        if walker.left: self.show_preorder(walker.left)
        if walker.right: self.show_preorder(walker.right)

    def show_postorder(self, walker=None):
        """Display the Tree as it traverses LEFT -> RIGHT -> ROOT."""
        if not walker:
            walker = self.tree.root

        if walker.left: self.show_postorder(walker.left)
        if walker.right: self.show_postorder(walker.right)
        print walker.data, 

if __name__ == "__main__":
    """This is the first block of Statements to be executed."""
    tree = BST(10)   # Root Node
    tree.insert(5)   # child
    tree.insert(5)   # child
    tree.insert(15)  # child
    tree.insert(25)  # child
    tree.insert(1)   # child
    tree.insert(2)   # child
    tree.insert(20)  # child
    tree.insert(500) # child
    tree.insert(3)   # child

    tree.show_inorder()
    print "\t --> IN-ORDER TRAVERSAL"
    tree.show_preorder()
    print "\t --> PRE-ORDER TRAVERSAL"
    tree.show_postorder()
    print "\t --> POST-ORDER TRAVERSAL"

    print "Smallest: {}".format(tree.tree.small)
    print "Biggest: {}".format(tree.tree.big)
