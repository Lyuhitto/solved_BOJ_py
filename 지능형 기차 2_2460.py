board = 0
board_max = 0

for _ in range(10):
    alighting, boarding = map(int, input().split())
    board += (boarding - alighting)
    board_max = board if board > board_max else board_max

print(board_max)
