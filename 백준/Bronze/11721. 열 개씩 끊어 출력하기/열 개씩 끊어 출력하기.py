from sys import stdin

sen = stdin.readline()
for i in range(0, len(sen), 10):
    print(sen[i:i+10])