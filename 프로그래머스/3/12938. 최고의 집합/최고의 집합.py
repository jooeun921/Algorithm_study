def solution(n, s):
    if n > s: return [-1] 
    
    mid, step = s//n, s%n
    answer = [mid for i in range(n-step)] + [mid+1 for i in range(step)]
    
    return answer