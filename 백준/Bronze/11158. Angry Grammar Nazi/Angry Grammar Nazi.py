from sys import stdin

T = int(stdin.readline().strip())

for _ in range(T):
    sentence = stdin.readline().strip()
    words = sentence.split()
    count = 0
    i = 0

    while i < len(words):  
        word = words[i]

        if word in {"u", "ur"}:
            count += 1
        
        if i < len(words) - 1:
            if words[i] == "would" and words[i + 1] == "of":
                count += 1
                i += 1
            elif words[i] == "should" and words[i + 1] == "of":
                count += 1
                i += 1

        if "lol" in word:
            count += 1

        i += 1

    print(count * 10)