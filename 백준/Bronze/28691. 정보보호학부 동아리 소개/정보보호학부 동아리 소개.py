name = input()

group = {'M':"MatKor", "W":"WiCys", "C":"CyKor", "A":"AlKor", "$":"$clear"}

if name in group:
    print(group[name])