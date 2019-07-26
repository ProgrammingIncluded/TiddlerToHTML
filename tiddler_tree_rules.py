import re
from BSTNode import *

# Global variables to keep track
TOKENS = {"//" : "I", "__" : "U", "''": "B"}
INQUOTE = False

# Numbers to denote how far into the list
# List like TOKENS
D_TOKENS = {"*": "LU", "#":"LO"}
# Negative means no list
INLIST = {k:-1 for k in D_TOKENS.keys()}


# Append more data to the RAW node
def append_raw(node, data):
    if node.type == "RAW":
        node.value += data
    return node

# Exit current scope in tree
# Returns first node outside scope
def exit_scope(node, scope = None):
    # Default case
    if node.parent == None:
        return node

    cur = node
    done = False
    while not done:
        p = cur.parent

        # Only valid if we have a right child
        if p.right != None:
            if scope == None:
                if p.type != "RAW" and p.right.ID == cur.ID:
                    done = True
            else:
                if p.type == scope and p.right.ID == cur.ID:
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

# Function to help parse bullet point like syntax
def parse_bull(tid, parent, line_mod, new_indent, cur_indent):

    # Check if we changed heights
    diff = new_indent - cur_indent

    # Move our node accordingly
    if diff > 0:
        # Keep adding layers until we arrive
        # at the right level
        while diff != 0:
            parent.left = BSTNode(parent, tid, "", None, None)
            parent = parent.left
            diff -= 1
        parent.right = BSTNode(parent, "LI", "", None, None)
        parent = parent.right
        parent.right = BSTNode(parent, "RAW", line_mod, None, None)
        return parent, new_indent
    elif diff < 0:
        # Keeping going up layers until we leave. 
        while diff != 0:
            parent = exit_scope(parent, tid)
            diff -= 1

    # Append our li value
    parent.left = BSTNode(parent, "LI", "", None, None)
    parent = parent.left
    parent.right = BSTNode(parent, "RAW", line_mod, None, None)
    return parent, new_indent


# Helper function in order to parse each line as a tree node value
# Returns left most node
def tiddler_tree_rules(parent, line):
    
    global INQUOTE
    global INLIST

    # Get a copy of list indentation
    # Clip to 0
    cur_indent = {k:max(v, 0) for k, v in INLIST.items()}

    # Check if we have to reset the bullet list
    for k, v in INLIST.items():
        if v == 0:
            # Move out of the unlist
            parent = exit_scope(parent, D_TOKENS[k])
            INLIST[k] = -1
        elif v > 0:
            # Set it to 0 unless we see another list
            INLIST[k] = 0

    values = line.split(' ', 1)

    # Count number of header values for headers
    if len(values) >= 2:
        token = values[0]
        line_mod = values[1]

        # Parse headers
        if token[0] == "!":
            # Count number of exclamations
            num = count_front_symbol(token, "!")
            # Add type to the left
            parent.left =  BSTNode(parent, "H" + str(num), "H" + str(num), None, None)
            parent.left.right = BSTNode(parent.left, "RAW", line_mod, None, None)
            return parent.left

        # Parse list related functions
        # Can only have one list, no recursive lists.
        for k, v in D_TOKENS.items():
            if token[0] == k:
                # Count number of stars
                num = count_front_symbol(token, k)
                parent, INLIST[k] = parse_bull(v, parent, line_mod, num, cur_indent[k])
                return parent


    # Parse quotes
    if line[0:3] == "<<<":
        if not INQUOTE:
            parent.left = BSTNode(parent, "Q", "Q", None, None)
            parent.left.right = BSTNode(parent.left, "RAW", "", None, None)
            INQUOTE = True
            return parent.left.right
        else:
            INQUOTE = False
            return exit_scope(parent, "Q")
    
    # Create a raw and pass it in if it isn't already
    if parent.type != "RAW":
        parent.left = BSTNode(parent, "RAW", "", None, None)
        parent = parent.left
    return parse_raw(parent, line)
        