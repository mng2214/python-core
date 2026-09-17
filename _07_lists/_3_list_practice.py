board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

col = int(input("X player, select a column: "))
row = int(input("X player, select a row: "))

col -= 1
row -= 1

board[row][col] = "X"
print(board[0])
print(board[1])
print(board[2])