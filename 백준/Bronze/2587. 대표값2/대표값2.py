from sys import stdin

num_list = [ int(stdin.readline().strip()) for _ in range(5)]
num_list.sort()
print(sum(num_list)//5)
print(num_list[2])