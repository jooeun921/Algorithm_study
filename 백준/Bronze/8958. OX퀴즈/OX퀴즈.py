T = int(input())
for _ in range(T):
    li = input()
    score = 0
    mul = 0
    for i in range(len(li)):
        if li[i] == 'O':
            mul += 1
            score += 1*mul
        else:
            mul = 0
    print(score)