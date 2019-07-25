import re
from parse import *

TOKENS = {"//" : "I", "__" : "U", "''": "B"}

# Append more data to the RAW node
def append_raw(node, data):
    if node.type == "RAW":
        node.value += data
    return node

# Exit current scope in tree
# Returns first node outside scope
def exit_scope(node):
    # Default case
    if node.parent == None:
        return node

    cur = node
    done = False
    while not done:
        p = cur.parent

        if p.type != "RAW" and p.right.ID == cur.ID:
            done = True

        if p.type == "ROOT":
            done = True

        cur = p
        
    
    return cur


# Parse text and format it.
# Assuming text modifiers are in the same line.
# Assumed node passed is raw node.
def parse_raw(raw, line):
    values = line.split(" ")
    node = raw

    bits = {v:False for v in TOKENS.values()}

    for v in values:
        res = v
        if res[-1] != "\n":
            res += " "

        for k, l in TOKENS.items():
            # restore our values with spaces
              # Do a find
            sfind = res.find(k)
            if sfind != -1 and not bits[l]:
                # remove the value
                res = res[:sfind] + res[sfind + 2:]
                node.left = BSTNode(node, l, l, None, None)
                node = node.left
                # creating a new raw node
                # TODO: Optimize toe merge into one node
                node.right = BSTNode(node, "RAW", "", None, None)
                node = node.right

                # toggle state
                bits[l] = True

        # See if we have another end token
        endresults = {l: -2 for l in TOKENS.values()}
        for k, l in TOKENS.items():
            efind = res.find(k)
            if efind != -1:
                res = res[:efind] + res[efind+2:]
            endresults[l] = efind

        # Append our raws 
        node = append_raw(node, res)

        for k, l in TOKENS.items():
            # Check ending values
            if endresults[l] != -1 and bits[l]:
                # Move backup the nodes
                node = exit_scope(node)
                # Create a new RAW
                # TODO: Optimize this node so only do it after all values.
                node.left = BSTNode(node, "RAW", "", None, None)
                node = node.left

                # Toggle back to false
                bits[l] = False

    # Go to left most node on top scope for our convenience
    while raw.left != None:
        raw = raw.left
    return raw

# Helper function in order to parse each line as a tree node value
# Returns left most node
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
    
    # Create a raw and pass it in if it isn't already
    if parent.type != "RAW":
        parent.left = BSTNode(parent, "RAW", "", None, None)
        parent = parent.left
    return parse_raw(parent, line)
        