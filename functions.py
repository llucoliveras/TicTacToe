import os

topLine    = "┌───┬───┬───┐"
midLine    = "├───┼───┼───┤"
bottomLine = "└───┴───┴───┘"

def screenClean(): os.system('cls' if os.name == 'nt' else 'clear')

def convertData(value):
    if value == 0: return "·"
    if value == 1: return "X"
    if value == 2: return "O"

def showGame(data):
    text = [topLine]
    rows = 0
    while rows < 3:
        line = ""
        column = 0
        while column < 3:
            if column == 3 - 1:
                line += f"│ {convertData(data[rows * 3 + column])} │"
            else:
                line += f"│ {convertData(data[rows * 3 + column])} "
            column += 1
        text.append(line)
        text.append(midLine)
        rows += 1
    text.pop()
    text.append(bottomLine)
    for line in text:
        print(line)

def checkWin(data):
    if data[0] != 0 and data[0] == data[1] and data[1] == data[2]: return True #     first line
    if data[3] != 0 and data[3] == data[4] and data[4] == data[5]: return True #    second line
    if data[6] != 0 and data[6] == data[7] and data[7] == data[8]: return True #     third line
    if data[0] != 0 and data[0] == data[3] and data[3] == data[6]: return True #     first column
    if data[1] != 0 and data[1] == data[4] and data[4] == data[7]: return True #    second column
    if data[2] != 0 and data[2] == data[5] and data[5] == data[8]: return True #     third column
    if data[0] != 0 and data[0] == data[4] and data[4] == data[8]: return True # backslash diagonal
    if data[2] != 0 and data[2] == data[4] and data[4] == data[6]: return True #     slash diagonal
    return False