from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    num_list = list(map(int, stdin.readline().split()))
    num_list_even = [x for x in num_list if x % 2 == 0]
    num_list_even.sort()
    print(sum(num_list_even), num_list_even[0])