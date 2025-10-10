def solution(s):
    ans = []
    str_list = list(s)
    for i in str_list:
        if str_list.count(i) == 1:
            ans.append(i)
    if len(ans) >= 1:
        ans.sort()
        answer = ''.join(ans)
    else:
        answer = ''
    return answer