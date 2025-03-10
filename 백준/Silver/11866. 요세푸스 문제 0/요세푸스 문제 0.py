N, K  = map(int, input().split())
N_list = [i for i in range(1, N+1)]
ans = []
state = 0

while len(N_list) != 0:
    state = (state + K - 1) % len(N_list)
    ans.append(N_list.pop(state))
    
print("<" + ", ".join(map(str, ans)) + ">")