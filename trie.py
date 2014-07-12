#! /usr/bin/env python
#-*- encoding: utf-8 -*-

"""Trie class"""

from node import TNode


class Trie(object):
    """Trie which uses TNode"""
    def __init__(self):
        self.root_node = TNode(None)
        self.leaf_key = None

    def search_nodes(self, search_key):
        focus_node = self.root_node
        for element in search_key:
            child_node = focus_node.get_child_node(element)
            if not child_node:
                return False
            focus_node = child_node
        if focus_node.get_child_node(self.leaf_key):
            return True
        else:
            return False

    def append_nodes(self, new_key):
        focus_node = self.root_node
        for element in new_key:
            child_node = focus_node.get_child_node(element)
            if not child_node:
                child_node = focus_node.append_child_node(element)
            focus_node = child_node
        if not focus_node.get_child_node(self.leaf_key):
            focus_node.append_child_node(self.leaf_key)

if __name__ == '__main__':
    trie = Trie()
    trie.append_nodes("192.168.0.1")
    trie.append_nodes("127.0.0.1")

    if trie.search_nodes("192.168.0.1"):
        print "yes"
    else:
        print "no"

    if trie.search_nodes("127.0.0.2"):
        print "yes"
    else:
        print "no"



# End of Line
