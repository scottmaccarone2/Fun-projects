"""
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
"""

def printTable(list):
    # First, within each list, we find the max length of all strings. This will
    # tell us how wide each column needs to be (using .rjust())
    colWidths = [0] * len(list)
    numStrings = len(list[0])
    for listNum in range(len(list)):
        lengths = []
        for i in range(numStrings):
            lengths.append(len(list[listNum][i]))
        colWidths[listNum] = max(lengths)

    # Now we need to find a way to print each list as a column AND print each
    # list side by side, probably using concatenation
    for i in range(numStrings):
        printedRow = ''
        for listNum in range(len(list)):
            printedRow = (printedRow
                         + ' '
                         + list[listNum][i].rjust(colWidths[listNum]))
        print(printedRow)
