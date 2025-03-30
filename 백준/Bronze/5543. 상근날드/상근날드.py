from sys import stdin

햄부기 = min(int(stdin.readline()) for _ in range(3))
음료 = min(int(stdin.readline()) for _ in range(2))
print(햄부기 + 음료 - 50)