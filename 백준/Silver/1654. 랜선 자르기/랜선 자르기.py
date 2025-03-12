K, N = map(int, input().split())
line = list(int(input()) for _ in range(K))

low, high = 1, max(line)

while low <= high:
    mid = (low + high) // 2
    count = sum(l // mid for l in line)

    if count >= N:
        low = mid + 1
    else:
        high = mid - 1

print(high)