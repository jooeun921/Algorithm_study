from sys import stdin

tri_list = list(int(stdin.readline()) for _ in range(3))

if tri_list == [60, 60, 60]:
    print("Equilateral")
elif sum(tri_list) == 180:
    if tri_list[0] == tri_list[1] or tri_list[1] == tri_list[2] or tri_list[0] == tri_list[2]:
        print("Isosceles")
    else: print("Scalene")
else:
    print("Error")