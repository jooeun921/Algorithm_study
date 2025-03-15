n = int(input())

for i in range(n):
    odd = 2*i + 1
    space = n-1-i
    print(" "*space+"*"*odd)
for j in range(n-1):
    odd_2 = 2 * (n-2-j) + 1
    space_2 = j+1
    print(" "*space_2+"*"*odd_2)