from sys import stdin

N = int(stdin.readline())
for _ in range(N):
    password = stdin.readline().strip()
    length = len(password)
    if 6 <= length and length <= 9:
        print("yes")
    else:
        print("no")