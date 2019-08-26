"""
We need to find the phone numbers and email addresses in a web page or
document. We will write a program that searches for these phone numbers and
email addresses in the clipboard. That way, all we need to do is press
CTRL-A to select all of the text, and then CTRL-C to copy it to the clipboard.
The program can replace the text on the clipboard with just the phone numbers
and email addresses found.

Before diving into the code, it's helpful to write out a high level plan, then
start thinking about more of the details. For example, at a high level, we
want this program to do three things:

1. Get text off the clipboard
2. Find all phone numbers and email addresses in the text
3. Paste those found in part 2 onto the clipboard

Thinking more about the details, we can start to identify key components:

1. Use the pyperclip module to copy/paste strings
2. Create TWO regex's (one for phone numbers and another for emails)
3. Find ALL matches (not just the first match)
4. Neatly format the matched strings into a single string to paste
5. Display a message if NO matches are found
"""

import pyperclip, re

# Create a regex for phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                 # area code (optional)
    (\s|-|\.)?                         # separator (optional if area code)
    (\d{3})                            # first 3 digits
    (\s|-|\.)                          # separator
    (\d{4})                            # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?     # extension
)''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                  # username
    @                                  # @ symbol
    [a-zA-Z0-9.-]+                     # domain name
    (\.[a-zA-Z]{2,4})                  # dot something
)''', re.VERBOSE)
# This does NOT match ALL email addresses, but it does match the most common

# Find matches in clipboard text and format the matches so they are all
# consistent (no parentheses around area code and '-' as separator)
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Create a single string of all phone numbers and emails, then copy to the
# clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')
