import sys
board = [list(sys.stdin.readline().strip()) for _ in range(5)]
ans = ''
length = len(board)
while board != [[], [], [], [], []]:
    for i in range(5):
        if len(board[i]) != 0:
            ans += board[i].pop(0)

print(ans)