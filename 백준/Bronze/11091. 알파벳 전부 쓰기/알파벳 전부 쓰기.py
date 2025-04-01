from sys import stdin
import re

N = int(stdin.readline())

for _ in range(N):
    alpha_list = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    sentence = stdin.readline().replace(' ', '').strip().lower()
    sentence_re = re.sub(r'[0-9.,?!\'\"]', '', sentence)
    
    for a in sentence_re:
        alpha_list[a] += 1
    
    ans = []
    for a in alpha_list:
        if alpha_list[a] == 0:
            ans.append(a)
    
    if len(ans) == 0:
        print("pangram")
    else:
        print("missing ", *ans, sep='')
