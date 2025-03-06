aList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

L = int(input())
a_list = input()
ans = 0

for i in range(L):
    ans += (aList.index(a_list[i]) + 1) * (31 ** i)
print(ans)