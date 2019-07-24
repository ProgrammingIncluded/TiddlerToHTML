
# File to contain output rules for tiddler tree
def html_output(node):
    if node == None:
        return ""

    # Go through it in order traversal
    res = ""

    # Keep going left until we have not
    res += html_output_rules_pre(node)
    res += html_output(node.right)
    res += html_output_rules_post(node)
    res += html_output(node.left)


    # Arrive at first value, traverse
    return res

# Pre traverse output
def html_output_rules_pre(node):
    if node == None:
        return ""

    if node.type == "RAW":
        return ""
        
    elif node.type[0] == "H":
        return "<h" + str(node.type[1]) + ">\n"

    if node.type == "ROOT":
        return ""

    return "ERROR"

# Post traverse output
def html_output_rules_post(node):
    if node == None:
        return ""

    if node.type == "RAW":
        return node.value
    
    elif node.type[0] == "H":
        return "</h" + str(node.type[1]) + ">\n"

    if node.type == "ROOT":
        return ""

    return "ERROR"