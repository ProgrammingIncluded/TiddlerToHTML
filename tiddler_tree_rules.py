import re
from parse import *

# Append more data to the RAW node
def append_raw(node, data):
    if node.type == "RAW":
        node.value += data
    return node

# Parse text and format it.
# Assuming text modifiers are in the same line.
# Assumed node passed is raw node.
def parse_raw(raw, line):
    values = line.split(" ")
    node = raw

    for v in values:
        # restore our values with spaces
        vst = v.strip()
        res = v
        ind = 0
        if res[-1] != "\n":
            res += " "

        if vst[0:2] == "//":
            node.left = BSTNode(node, "I", "I", None, None)
            node = node.left
            # creating a new raw node
            node.right = BSTNode(node, "RAW", "", None, None)
            ind = 2
            node = node.right

        # Append our raws 
        node = append_raw(node, res[ind:])

        # Check ending values
        if vst[-2:] == "//":
            # Need to append if not the same token
            node.value = node.value[:-3]
            node = node.parent
            # Create a new RAW
            node.left = BSTNode(node, "RAW", "", None, None)
            node = node.left

    return node

# Helper function in order to parse each line as a tree node value
def tiddler_tree_rules(parent, line):
    
    values = line.split(' ', 1)

    # Count number of header values
    if len(values) >= 2:
        token = values[0]
        line_mod = values[1]

        if token[0] == "!":
            # Count number of exclamations
            num = count_front_symbol(token, "!")
            # Add type to the left
            parent.left =  BSTNode(parent, "H" + str(num), "H" + str(num), None, None)
            parent.left.right = BSTNode(parent, "RAW", line_mod, None, None)
            return parent.left
    
    # Create a raw and pass it in
    parent.left = BSTNode(parent, "RAW", "", None, None)
    return parse_raw(parent.left, line)
        