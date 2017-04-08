from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "JAK STATKI NA NIEBIE"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    guess_row = int(raw_input("Ktory wiersz:"))
    guess_col = int(raw_input("Ktora kolumna :"))
    guess_row = guess_row -1
    guess_col = guess_col -1

    if guess_row == ship_row and guess_col == ship_col:
        print "Brawo! Zatopiles statek!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "No srry, ale wypadles poza plansze"
        elif(board[guess_row][guess_col] == "X"):
            print "Juz to zgadles, sprobuj co innego"
        else:
            print "Zle!"
            board[guess_row][guess_col] = "X"
        if turn == 8:
            print "Gejm Olwer"
    # Print (turn + 1) here!
    print "Runda", turn + 1
    print_board(board)