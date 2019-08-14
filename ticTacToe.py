# First, we define the board (a completely clear board since each key's value
# is a single-space string):
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# Now we write a function to display the board onto the screen:
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# The turn starts with X
turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Which space would you like to mark?')
    print('Enter top/mid/low-L/M/R')
    move = input()

    # Check to determine if the space is already occupied. If so, have the
    # player make another selection
    while theBoard[move] != ' ':
        print('That space is already take, try again.')
        move = input()

    # Include exception handling (KeyError) here if a player enters an invalid
    # position such as mid-m rather than mid-M


    theBoard[move] = turn
    # After the mark occurs, the program needs to check if the most recent mark
    # concludes the game with a winner
    # There also needs to be a way to check if the game concludes in a draw.
    # For now, I can just write code that waits until the for loop runs out.
    # If no winner is determined by that time, print a statement stating the
    # match is a draw

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print(theBoard)
