#! /usr/bin/env python
#-*- encoding: utf-8 -*-

"""Node class for Trie and PATRICIA

    TNode or PNode
    Each Node has two method:
        * get_child_node(key)
            see child_node
            if there is child whose key is key, return that child.
        * append_child_node(key)
            make child which has key
            append to self child and change child to brother
"""


class TNode(object):
    """Node class for Trie"""
    def __init__(self, key, child_node=None, brother_node=None):
        self.key = key
        self.child_node = child_node
        self.brother_node = brother_node

    def get_child_node(self, key):
        child = self.child_node
        while child:
            if child.key == key:
                break
            child = child.brother_node
        return child

    def append_child_node(self, key):
        new_child = TNode(key, brother_node=self.child_node)
        self.child_node = new_child
        return self.child_node


class PNode(object):
    """Node class for PATRICA"""
    def __init__(self, key, child_node=None, brother_node=None):
        self.key = key
        self.child_node = child_node
        self.brother_node = brother_node

    def get_child_node(self, key_head):
        child = self.child_node
        while child:
            if child.key[0] == key_head:
                break
            child = child.brother_node
        return child

    def append_child_node(self, key):
        new_child = PNode(key, brother_node=self.child_node)
        self.child_node = new_child
        return self.child_node

# End of Line
