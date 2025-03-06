a, b = map(int, input().split())
ans_1 = 0
for x in range(1, min(a, b) + 1):
	if a%x == 0 and b%x == 0:
		ans_1 = max(ans_1, x)
ans_2 = (a//ans_1)*b
print(ans_1)
print(ans_2)