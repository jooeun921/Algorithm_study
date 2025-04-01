from sys import stdin

T = int(stdin.readline().strip())

for _ in range(T):
    words = stdin.readline().strip().split()
    decoded_message = ""

    for word in words:
        value = sum(ord(c) - ord('a') for c in word) % 27
        decoded_message += chr(ord('a') + value) if value < 26 else ' '

    print(decoded_message)