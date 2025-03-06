while True:
	a = list(input())
	if a == ['0']:
		break
	a_f = list(a[-i] for i in range(1, len(a)+1))
	if a == a_f:
		print("yes")
	else:
		print("no")