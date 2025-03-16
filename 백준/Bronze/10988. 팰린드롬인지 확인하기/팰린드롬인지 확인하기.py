word = input()
max = len(word) // 2
state = 1

for i in range(max):
    if word[i] != word[-1-i]:
        state = 0
        break

print(state)