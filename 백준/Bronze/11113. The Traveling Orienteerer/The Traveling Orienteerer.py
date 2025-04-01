from sys import stdin
from math import sqrt

m = int(stdin.readline())
race_map = [list(map(float, stdin.readline().split())) for _ in range(m)]

T = int(stdin.readline())
for _ in range(T):
    trial = int(stdin.readline())
    course = list(map(int, stdin.readline().split()))
    road = 0.0
    for j in range(trial-1):
        state_1 = course[j]
        state_2 = course[j+1]
        road += sqrt((race_map[state_1][0] - race_map[state_2][0])**2 + (race_map[state_1][1] - race_map[state_2][1])**2)
    print(round(road))
    