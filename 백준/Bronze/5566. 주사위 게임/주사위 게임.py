N, M = map(int, input().split()) #N = 맵길이 M = 주사위 던진 횟수. 그 뒤로 N개줄과 M개줄이 입력값으로 들어옴.
map = []
state = 0 # 위치
step = 0 # 지시사항 = map[state]
count = 0
for n in range(N):
    map.append(int(input()))
for m in range(M):
    dice = int(input())
    count += 1
    state += dice
    if state >= N-1:
        print(count)
        break
    state += map[state]
    if state >= N-1:
        print(count)
        break