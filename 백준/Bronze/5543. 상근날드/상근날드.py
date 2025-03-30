from sys import stdin

상덕버거 = int(stdin.readline())
중덕버거 = int(stdin.readline())
하덕버거 = int(stdin.readline())
콜라 = int(stdin.readline())
사이다 = int(stdin.readline())

햄부르스딱스 = min(상덕버거, 중덕버거, 하덕버거)
음료 = min(콜라, 사이다)

print(햄부르스딱스 + 음료 - 50)
