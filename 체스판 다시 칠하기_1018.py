import sys


def redraw_chess(height: int, width: int, first_board: list) -> int:
    min_answer = 64
    for x in range(height - 7):
        for y in range(width - 7):
            tmp_board = [first_board[x + _][y:y + 8] for _ in range(8)]
            answer = compare_chess(tmp_board)
            if min_answer > answer:
                min_answer = answer
    return min_answer


def compare_chess(board: list) -> int:
    board_w = 'W'
    board_b = 'B'
    count_w = 0
    count_b = 0

    # if board[0][0] == 'W'
    for i in range(8):
        for j in range(8):
            tmp_i = i % 2
            tmp_j = j % 2
            if tmp_i == tmp_j:
                if board[i][j] != board_w:
                    count_w += 1
            else:
                if board[i][j] == board_w:
                    count_w += 1

    # if board[0][0] == 'B'
    for i in range(8):
        for j in range(8):
            tmp_i = i % 2
            tmp_j = j % 2
            if tmp_i == tmp_j:
                if board[i][j] != board_b:
                    count_b += 1
            else:
                if board[i][j] == board_b:
                    count_b += 1

    return min(count_w, count_b)


n, m = map(int, sys.stdin.readline().strip().split())
get_chess = [list(sys.stdin.readline().strip()) for _ in range(n)]

print(redraw_chess(n, m, get_chess))
