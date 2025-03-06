n = int(input()) - 1
t = 1
while True:
	if n <= 0:
		break
	n -= 6*t
	t += 1

print(t)