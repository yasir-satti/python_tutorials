# Directory Tree Generator
#
# Directories are like family trees:
# each directory has a particular relationship with other directories.
# No directory ever stays on its own, except an empty root directory.
# When you’re working with files and directories, it is difficult to see
# the relationship between directories, as you can only see what exists
# in the current directory. You’re either using a file manager or working
# from the command-line.
#
# With a Directory Tree Generator, you can see the relationship between
# files and directories like a tree or a map.
# This makes it easier to understand the positioning of files and directories.
# A directory tree map is important when you’re explaining certain concepts,
# and a Directory Tree Generator makes it easier to get a visual representation
# of the file and directory relationships.
#
# Examples of Directory Tree Generators
# Here are some implementations of the Directory Tree Generator idea:
# 1. Tree
# 2. Dirtreex
#
# Technical Details
# The main objective of the Directory Tree Generator is to visualize the relationships
# between files and directories. The os library can be very useful in listing the
# files and directories in a chosen directory.
#
# Using a framework such as docopt or argparse helps abstract a lot of stuff,
# allowing you to focus on writing code for the application’s logic.
# In the application’s logic, you can decide how you want to represent files or
# directories. Using different colours is a brilliant way to go about it. You can 
# use the colored library to print the files and directories in different colours.
# You can also decide how deep you’d like the Directory Tree Generator to go. For example,
# if a directory has children directories twelve levels deep, you may decide to go only 
# as deep as the fifth level.
# 
# If you wish, you can also let the user decide how deep they want the Directory Tree
# Generator to go.
#
# Extra Challenge
# Since the results of the generated directory tree will be on the command-line, you can
# go one step further. You can have the generator create images of the directory tree, 
# so it’ll basically turn the text into an image.
# You’ll find the pillow library useful for doing this.