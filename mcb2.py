"""
PROJECT: MULTICLIPBOARD
We want to write a program for a clipboard that can hold many different pieces of text. The extension of this file is *.pyw* so that Python will not show a Terminal window when it runs this program.

This program will save each piece of clipboard text under a keyword. For example, when you run `py mcb_project.pyw save spam`, the current contents of the clipboard will be save with the keyword `spam`. This test can later be loaded to the clipboard again by running `py mcb_project.pyw spam`. And if the user forgets what keywords they have, they can run `py mcb_project.pyw list` to copy a list of all keywords to the clipboard.

The program must do the following:

- The command line argument for the keyword is checked
- If the argument is `save`, then the clipboard contents are saved to the keyword
- If the argument is `list`, then all the keywords are copied to the clipboard
- Otherwise, the text for the keyword is copied to the clipboard

This means the code will need to do the following:

- Read the command line arguments from `sys.argv`
- Read and write to the clipboard
- Save and load to a shelf file
"""

# STEP 1: COMMENTS AND SHELF SETUP; SKELETON SCRIPT

#! python3
# mcb_project.pyw - Saves and loads pieces of text to the clipboard
# Usage:  py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#	  py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#	  py.exe mob.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys

"""
Whenever the user wants to save a new piece of clipboard text, you'll save it to a shelf file. Then, when the user wants to paste the text back to their clipboard, you'll open the shelf file and load it back into your program. The shelf file can be named with the prefix `mcb`.
"""

mcbShelf = shelve.open('mcb')

# STEP 2: SAVE CLIPBOARD CONTENT WITH A KEYWORD

"""
If the first command line argument (which will always be at index 1 of the sys.argv list) is `save`, the second command line argument is the keyword for the current content of the clipboard. The keyword will be used as the key for `mcbShelf`, and the value will be the text currently on the clipboard
"""

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) ==  2:
    # List keywords and load content

    # STEP 3: LIST KEYWORDS AND LOAD A KEYWORD’S CONTENT

    # If there is only one command line argument, check to see if it’s `list`
    # If so, a string representation of the list of shelf keys will be copied to the clipboard
    # The user can paste this list into an open text editor to read it

    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))

    # Otherwise, assume the command line argument is a keyword. If the keyword exists in the `mcbShelf` shelf
    # as a key, you can load the value onto the clipboard

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
