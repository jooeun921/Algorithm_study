music = list(map(int, input().split()))
asc = list(range(1, 9))
des = list(range(8, 0, -1))

if music == asc:
    print("ascending")
elif music == des:
    print("descending")
else:
    print("mixed")