"""
This program repeatedly asks users for their age and password until they
provide valid input.

NOTE: This idea will be helpful whenever you want to repeatedly ask a user
for input where there is a chance they might type in an error (like the
ticTacToe.py game/file).

NOTE: There is NO need within the if conditional to ask the user to once again
enter their age. If the condition is not met, the user told that they must
enter a number for their age and is simply brought back up to the beginning
of the loop. The same thing happens when asked to provide a password.
"""

while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        # The only way to break out of this loop is to provide a valid (i.e.
        # decimal) age; otherwise, the user stays in the loop.
        break
    print('Please enter a number for your age')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and nunbers.')
