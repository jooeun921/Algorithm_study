from string import ascii_lowercase
alphabet_dict = {}
for i in ascii_lowercase:
	alphabet_dict[i] = -1
alpha = input()
for i in range(len(alpha)):
	if alphabet_dict[alpha[i]] == -1:
		alphabet_dict[alpha[i]] = i
print(*alphabet_dict.values())