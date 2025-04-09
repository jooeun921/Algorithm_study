from sys import stdin

while True:
    a, b = map(int, stdin.readline().split())
    if a == 0 and b == 0:
        break
    else:
        if a > b:
            print("Yes")
        else:
            print("No")