from parse import *



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
            parent.right = BSTNode(parent, "RAW", line_mod, None, None)
            return parent.right
        else:
            parent.left = BSTNode(parent, "RAW", line, None, None)
    else:
        # Default case is to parse as content
        parent.left = BSTNode(parent, "RAW", line, None, None)
    return parent.left
        