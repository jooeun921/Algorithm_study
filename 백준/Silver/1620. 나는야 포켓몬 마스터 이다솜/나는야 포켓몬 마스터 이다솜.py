import sys
readline = sys.stdin.readline
n, m = map(int, input().split())

pokemon = [readline().strip() for _ in range(n)]
pokemon_dic = {name: i + 1 for i, name in enumerate(pokemon)}

for _ in range(m):
    quest = input().strip()
    if quest.isdigit():
        print(pokemon[int(quest) - 1])
    else:
        print(pokemon_dic[quest])