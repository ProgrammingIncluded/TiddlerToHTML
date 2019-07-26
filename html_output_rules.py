
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
    elif node.type[0] == "I":
        return "<i>"
    elif node.type[0] == "U":
        return "<u>"
    elif node.type[0] == "B":
        return "<b>"
    elif node.type[0] == "Q":
        return '<div class="quote">\n'
    elif node.type == "LU":
        return "<ul>\n"
    elif node.type == "LI":
        return "<li>\n"
    elif node.type == "LO":
        return "<ol>\n"


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

    elif node.type[0] == "I":
        return "</i>"

    elif node.type[0] == "U":
        return "</u>"

    elif node.type[0] == "B":
        return "</b>"

    elif node.type[0] == "Q":
        return '</div class="quote">\n'

    elif node.type == "LU":
        return "</ul>"

    elif node.type == "LI":
        return "</li>\n"

    elif node.type == "LO":
        return "</ol>"

    if node.type == "ROOT":
        return ""

    return "ERROR"