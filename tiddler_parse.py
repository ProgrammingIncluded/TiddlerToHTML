import sys
import os

from tiddler_tree_rules import * 
from html_output_rules import *
from parse import BSTNode

# Function to output help string.
def help_str():
    s = "Please supply a path to a folder with tiddler files.\n"
    s += "Usage:\n"
    s += sys.argv[0] + " " + "<foldername> <output folder>\n\n"
    s += "Converts all .tid files into HTML files with custom CSS."
    return s

# Create the file name from our files.
def create_file_name(og):
    # Remove file extension
    noext = og[:-5]
    
    # Parse name
    # Replace spaces
    res = noext.replace(' ', '-')
    
    # Lowercase
    res = res.lower()

    return res + ".html"

# Create the parse tree for the tiddler
def tid_tree(filename):
    with open(filename, "r") as infile:
        root = BSTNode(None, "ROOT", "ROOT", None, None)
        parent = root
        for line in infile:
            parent = tiddler_tree_rules(parent, line)

    return root

def convert_tid_tree(filename, inroot):
    with open(filename, "w") as outfile:
        outfile.write(html_output(inroot))

# Work with specific files only
def main():
    # Check proper arguments
    if len(sys.argv) < 3:
        print(help_str())
        return 1

    infold = os.path.isdir(sys.argv[1])
    outfold = os.path.isdir(sys.argv[2])

    if not infold or not outfold:
        print("Invalid folder given. Please try again.")
        return 1
    
    for f in os.listdir(sys.argv[1]):
        if not f.endswith(".tid"):
            continue

        # Create output file name
        outfile = sys.argv[2] + "/" + create_file_name(f)

        # Create parse tree from file
        inroot = tid_tree(f)
        print(inroot)

        # Once we have the tree, read the tree
        # and convert to html
        convert_tid_tree(outfile, inroot)
        
        
            
    
    
    
if __name__ == "__main__":
    main()
