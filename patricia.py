#! /usr/bin/env python
#-*- encoding: utf-8 -*-

"""PATRICIA (Practical Algorithm To Retrieve Information Coded in Alphanumeric)"""

from node import PNode


class Patricia(object):
    """Patrica class"""
    def __init__(self):
        self.root_node = PNode(None)
        self.leaf_key = [None]

    def find_longest_match(self, key):
        focus_node = self.root_node
        key_pos = 0
        while key_pos < len(key):
            child_node = focus_node.get_child_node(key[key_pos])
            if not child_node:
                break
            node_key_pos = 1
            while node_key_pos < len(child_node.key):
                if (key_pos + node_key_pos >= len(key)
                    or key[key_pos + node_key_pos] != child_node.key[node_key_pos]):
                    return child_node, key_pos + node_key_pos, node_key_pos
                node_key_pos += 1
            key_pos += node_key_pos
            focus_node = child_node
        return focus_node, key_pos, 0

    def search_nodes(self, search_key):
        focus_node, key_pos, node_key_pos = self.find_longest_match(search_key)
        if (key_pos == len(search_key)
            and focus_node.get_child_node(self.leaf_key[0])
            and node_key_pos == 0):
            return True
        return False

    def append_nodes(self, new_key):
        focus_node, key_pos, node_key_pos = self.find_longest_match(new_key)
        if node_key_pos > 0: # need to divide focus_node to focus_node and focus_node_new
            focus_node_new = PNode(focus_node.key[node_key_pos:], child_node=focus_node.child_node)
            focus_node.key = focus_node.key[:node_key_pos]
            focus_node.child_node = focus_node_new
        if key_pos < len(new_key):
            focus_node.append_child_node(new_key[key_pos:]).append_child_node(self.leaf_key)
        else:
            if not focus_node.get_child_node(self.leaf_key):
                focus_node.append_child_node(self.leaf_key)


if __name__ == '__main__':
    patricia = Patricia()
    patricia.append_nodes("192.168.0.1")
    patricia.append_nodes("127.0.0.1")
    patricia.append_nodes("193.23.12.1")

    if patricia.search_nodes("192.168.0.0"):
        print "yes"
    else:
        print "no"

# End of Line
