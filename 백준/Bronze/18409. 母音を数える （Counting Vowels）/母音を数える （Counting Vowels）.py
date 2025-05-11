N = int(input())
S = input()

vowels = {'a', 'i', 'u', 'e', 'o'}
count = sum(1 for char in S if char in vowels)

print(count)