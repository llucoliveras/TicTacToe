import functions as FUN

game = [0,0,0,0,0,0,0,0,0]

playerOne = True
win = False
inputs = 0

while inputs < 9 and not win:
    while True:
        
        square = -1

        FUN.screenClean()
        FUN.showGame(game)
        
        while square < 0 or square > 8:
            
            if playerOne: print("Player 1, choose a square from 1 to 9")
            else: print("Player 2, choose a square from 1 to 9")
            
            square = input()
            if square == "": square = -1
        square = int(square) - 1

        if game[square] != 0: print("Square already ocupied")
        else: break
    
    if game[square] == 0: game[square] = 1 if playerOne else 2

    if FUN.checkWin(game):

        FUN.screenClean()
        FUN.showGame(game)

        if playerOne:
            print("Congrats, Player 1 [X] wins!")
            win = True
        else:
            print("Congrats, Player 2 [O] wins!")
            win = True
    
    playerOne = not playerOne
    inputs += 1

if not win:
    
    FUN.screenClean()
    FUN.showGame(game)

    print("Unlucky, both players lost. Better luck next time!\n")