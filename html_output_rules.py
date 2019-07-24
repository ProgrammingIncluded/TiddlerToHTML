
# File to contain output rules for tiddler tree
def html_output(node):
    if node == None:
        return ""

    # Go through it in order traversal
    res = ""

    # Left then Right
    res += html_output_rules_pre(node.left)
    res += html_output_rules_pre(node.right)
    res += html_output(node.right)
    res += html_output(node.left)
    res += html_output_rules_post(node.left)
    res += html_output_rules_post(node.right)

    # Arrive at first value, traverse
    return res

# Pre traverse output
def html_output_rules_pre(node):
    if node == None:
        return ""

    if node.type == "RAW":
        return node.value 
        
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
        return ""
    elif node.type[0] == "H":
        return "</h" + str(node.type[1]) + ">\n"

    if node.type == "ROOT":
        return ""

    return "ERROR"