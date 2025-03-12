n = int(input())
num_list = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1

for num in num_list:
    while current <= num:
        stack.append(current)
        result.append("+")
        current += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit()

print("\n".join(result))