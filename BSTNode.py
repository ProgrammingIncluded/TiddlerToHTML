# Count the number of symbols in a given 
# beginning of a line
def count_front_symbol(line, sym):
    count = 0
    for c in line:
        if c != sym:
            break
        count += 1
    return count

UID = 0

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
        global UID
        self.ID = str(UID)
        UID += 1

    # Printing helper
    def __str__(self):
        res = ""
        # Print ourselves
        res += "ID: " + self.ID + "\n"
        res += " " + self.value
        if len(self.value) == 0 or self.value[-1] != "\n":
            res += "\n"

        if self.left != None:
            res += "LEFT : " + str(self.left)
        else:
            res += "No Left\n"

        if self.right != None:
            res += "RIGHT: " + str(self.right)
        else:
            res += "No Right\n"
        
        return res
        