first = input()
second = input()
third = input()

if first.isdigit():
    ans = int(first) + 3
elif second.isdigit():
    ans = int(second) + 2
elif third.isdigit():
    ans = int(third) + 1

if ans % 15 == 0:
    print("FizzBuzz")
elif ans % 3 == 0:
    print("Fizz")
elif ans % 5 == 0:
    print("Buzz")
else:
    print(ans)