from sys import stdin
readline = stdin.readline
평점 = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0,"F":0.0}
등급합산 = 0
학점합산 = 0
for _ in range(20):
    과목, 학점, 등급 = map(str, readline().strip().split())
    if 등급 != 'P':
        등급합산 += 평점[등급] * float(학점)
        학점합산 += float(학점)
print(등급합산 / 학점합산)