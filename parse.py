# Count the number of symbols in a given 
# beginning of a line
def count_front_symbol(line, sym):
    count = 0
    for c in line:
        if c != sym:
            break
        count += 1
    return count

# Node for tree parsing.
# Requires parents, type, value, and children.
class BSTNode():

    # parent should be node type
    # type is of string
    # value is of string
    # children should be of array value
    #
    def __init__(self, parent, typ, value, left, right):
        self.parent = parent
        self.type = typ
        self.value = value
        self.left = left
        self.right = right

    # Printing helper
    def __str__(self):
        res = ""
        # Print ourselves
        res += self.value
        if len(self.value) == 0 or self.value[-1] != "\n":
            res += "\n"

        if self.left != None:
            res += str(self.left)
        else:
            res += "No Left\n"

        if self.right != None:
            res += str(self.right)
        else:
            res += "No Right\n"
        
        return res
        