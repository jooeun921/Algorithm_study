n = int(input())
li = list(map(int, input().split()))
v = int(input())
ans = 0
for i in range(n):
    if li[i] == v:
        ans += 1
print(ans)


# 처음 풀이인데, 사실 위에를 먼저 생각했다가 값이 없을 때 문제가 생기지 않나? 싶었음. 그래서 만든 방식인데,
# 위로 한번 해보니까 되더라~
# import sys
# board = [list(sys.stdin.readline().strip()) for _ in range(5)]
# ans = ''
# length = len(board)
# while board != [[], [], [], [], []]:
#     for i in range(5):
#         if len(board[i]) != 0:
#             ans += board[i].pop(0)

# print(ans)