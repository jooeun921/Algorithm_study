from string import ascii_lowercase
aList = list(ascii_lowercase)

L = int(input())
a_list = input()
ans = 0

for i in range(L):
    ans += (aList.index(a_list[i]) + 1) * (31 ** i)
print(ans % 1234567891)