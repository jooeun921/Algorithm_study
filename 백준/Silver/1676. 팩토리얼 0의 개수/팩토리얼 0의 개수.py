N = int(input())
count = 0
power_5 = 5
while N >= power_5:
    count += N // power_5
    power_5 *= 5
print(count)