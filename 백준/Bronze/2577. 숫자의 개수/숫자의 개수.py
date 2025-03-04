a = int(input())
b = int(input())
c = int(input())
result = str(a*b*c)
li = [0] * 10

for di in result:
    li[int(di)] += 1

for i in range(10):
    print(li[i])