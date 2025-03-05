ans = set()
for _ in range(10):
    num = int(input()) % 42
    ans.add(f'{num}')
print(len(ans))