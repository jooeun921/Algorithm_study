N, L = input().split()
N = int(N)
L = str(L)

count = 0
number = 1

while True:
    if L not in str(number):
        count += 1
        if count == N:
            print(number)
            break
    number += 1