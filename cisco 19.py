rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
print(rooms)
EMPTY = "EMPTY"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
print(board)
board[0][7] = ROOK
print(board)
board[7][0] = ROOK
print(board)
board[7][7] = ROOK
print(board)
