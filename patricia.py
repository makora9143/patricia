#! /usr/bin/env python
#-*- encoding: utf-8 -*-

"""PATRICIA (Practical Algorithm To Retrieve Information Coded in Alphanumeric)"""

from node import PNode

class Patricia(object):
    """Patrica class"""
    def __init__(self):
        self.root_node = PNode(None)
        self.leaf_key = [None]

    def search_nodes(self, search_key):
        pass

    def append_nodes(self, new_key):
        pass

# End of Line
