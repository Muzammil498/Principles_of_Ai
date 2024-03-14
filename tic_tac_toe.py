import random

matrix = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
count = 0

def print_board():
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def check_winner(player):
    for x in range(3):
        if matrix[x][0] == player and matrix[x][1] == player and matrix[x][2] == player:
            return True
        if matrix[0][x] == player and matrix[1][x] == player and matrix[2][x] == player:
            return True

    if matrix[0][0] == player and matrix[1][1] == player and matrix[2][2] == player:
        return True

    if matrix[0][2] == player and matrix[1][1] == player and matrix[2][0] == player:
        return True

    return False

while True:
    # Player 1's turn
    row = int(input("Player 1, enter the row: "))
    col = int(input("Player 1, enter the column: "))

    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid row or column")
        continue
    elif matrix[row][col] == 'X' or matrix[row][col] == 'O':
        print("Cell already occupied. Try again.")
        continue
    else:
        matrix[row][col] = 'X'
        count += 1

        print_board()

        if check_winner('X'):
            print("Player 1(X) won the game")
            exit(0)

        if count == 9:
            print("It's a tie!")
            exit(0)

    # Player 2's turn (computer)
    print("Player 2's turn (Computer):")
    while True:
        comp_row = random.randint(0, 2)
        comp_col = random.randint(0, 2)

        if matrix[comp_row][comp_col] == '*':
            matrix[comp_row][comp_col] = 'O'
            count += 1
            break

    print_board()

    if check_winner('O'):
        print("Player 2(O) won the game")
        exit(0)

    if count == 9:
        print("It's a tie!")
        exit(0)
