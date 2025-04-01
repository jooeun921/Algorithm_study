from collections import Counter

def peragram(s):
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 == 1)
    return max(0, odd_count - 1)

s = input().strip()
print(peragram(s))