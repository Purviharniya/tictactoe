def tictactoe():
    boardpos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    wincommbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(boardpos[0], boardpos[1], boardpos[2])
        print(boardpos[3], boardpos[4], boardpos[5])
        print(boardpos[6], boardpos[7], boardpos[8])
        print()

    def player1():
        n = choose()
        if boardpos[n] == "X" or boardpos[n] == "O":
            print("\nYou can't go there, the position is already filled. Try again")
            player1()
        else:
            boardpos[n] = "X"

    def player2():
        n = choose()
        if boardpos[n] == "X" or boardpos[n] == "O":
            print("\nYou can't go there, the position is alreday filled. Try again")
            player2()
        else:
            boardpos[n] = "O"

    def choose():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                   print("\nThat's not a number. Try again")
                   continue

    def check():
        count = 0
        for a in wincommbinations:
            if boardpos[a[0]] == boardpos[a[1]] == boardpos[a[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True

            if boardpos[a[0]] == boardpos[a[1]] == boardpos[a[2]] == "O":
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if boardpos[a] == "X" or boardpos[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while not end:
        draw()
        end = check()
        if end == True:
            break
        print("Player 1 choose where to place a cross")
        player1()
        print()
        draw()
        end = check()
        if end == True:
            break
        print("Player 2 choose where to place a nought")
        player2()
        print()

    if input("Play again (y/n)\n") == "y":
        print()
        tictactoe()

tictactoe()
