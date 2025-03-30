from sys import stdin
from math import lcm, gcd

분자1, 분모1 = map(int, stdin.readline().split())
분자2, 분모2 = map(int, stdin.readline().split())
분모 = lcm(분모1, 분모2)
분자 = (분자1 * (분모//분모1)) + (분자2 * (분모//분모2))

최소공배수 = gcd(분모, 분자)
if 최소공배수 != -1:
    분자 //= 최소공배수
    분모 //= 최소공배수

print(분자, 분모)