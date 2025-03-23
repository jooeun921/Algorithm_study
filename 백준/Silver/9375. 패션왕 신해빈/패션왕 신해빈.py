from sys import stdin

T = int(stdin.readline().strip())
for _ in range(T):
    cloth_num = int(stdin.readline().strip())
    clothes = {}
    for _ in range(cloth_num):
        item, category = stdin.readline().strip().split()
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
    
    result = 1
    for count in clothes.values():
        result *= (count + 1)

    print(result-1)