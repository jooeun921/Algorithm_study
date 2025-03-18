n = int(input())
count = 0

for _ in range(n):
    word = input()
    seen = set()
    prev = ''
    
    group = True
    
    for char in word:
        if char in seen and char != prev: # set에 있으므로 이전에 이미 한번 나왔으면서, 이전 char에는 없는 경우 -> 그룹 단어가 안됨.
            group = False
            break
        seen.add(char)
        prev = char
    
    if group:
        count += 1

print(count)