#! python3

"""
The goal of this project is to create a password manager (though it will be
insecure, this program demonstrates some essential fundamentals).
"""

passwords = {'gmail': 'F937asGEB39sd3DR32',
             'fb': '34FEskb44DDSkd345df3g',
             'blog': 'd3d36FDS33dDdd93kd3'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python passwordLocker.py [account] - copy account password')
    sys.exit()

""" first command line arg is the account name"""
account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account name ' + account)
