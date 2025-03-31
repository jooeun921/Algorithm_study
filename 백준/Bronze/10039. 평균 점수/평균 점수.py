from sys import stdin

score = []

for _ in range(5):
    score_stu = int(stdin.readline())
    if score_stu < 40:
        score_stu = 40
    score.append(score_stu)

print(sum(score)//5)
