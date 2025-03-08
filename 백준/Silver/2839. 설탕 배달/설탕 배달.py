c_3 = [0, 2, 4, 1, 3]
N = int(input())
a = c_3[N%5]
b = (N - a*3) // 5
print(a+b if b>=0 else -1)