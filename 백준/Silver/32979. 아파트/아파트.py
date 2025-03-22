from sys import stdin
from collections import deque

N = int(stdin.readline())
T = int(stdin.readline())
apt = deque(stdin.readline().strip().split())
T_num = stdin.readline().split()
lose_people = []

for i in range(T):
    game_num = int(T_num[i])-1
    apt.rotate(-game_num)
    lose_people.append(apt[0])

print(*lose_people)