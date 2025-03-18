word = input()
word_upper = word.upper()
count = {}

for i in word_upper:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

most_frequent = [k for k, v in count.items() if v == max(count.values())]
print("?" if len(most_frequent) > 1 else most_frequent[0])