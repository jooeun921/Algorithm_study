def NToTen(n, num):
    return int(num, n)

def TenToN(n, num):
    if num == 0:
        return "0"
    result = ""
    while num:
        num, remainder = divmod(num, n)
        result = str(remainder) + result
    return result

def solution(expressions):
    answer, answer_format = [], []
    max_format, hint = 0, []
    
    for e in expressions:
        num1, func, num2, _, ans = e.split(" ")
        max_format = max(max_format, max(map(int, num1 + num2)))
        
        if ans != "X": 
            hint.append(e)
            max_format = max(max_format, max(map(int, ans)))
        else:
            answer.append(e)
    
    for n in range(max_format + 1, 10):
        check = True
        for h in hint:
            num1, func, num2, _, ans = h.split(" ")
            num1, num2, ans = NToTen(n, num1), NToTen(n, num2), NToTen(n, ans)
            
            if (func == '+' and num1 + num2 != ans) or (func == '-' and num1 - num2 != ans):
                check = False
                break
        
        if check:
            answer_format.append(n)
    
    for idx in range(len(answer)):
        num1, func, num2, _, ans = answer[idx].split(" ")
        ans_set = set()
        
        for a in answer_format:
            num_1, num_2 = NToTen(a, num1), NToTen(a, num2)
            
            if func == "+":
                ans_set.add(TenToN(a, num_1 + num_2))
            elif func == "-":
                ans_set.add(TenToN(a, num_1 - num_2))
        
        answer[idx] = ' '.join([num1, func, num2, _, list(ans_set)[0]]) if len(ans_set) == 1 else ' '.join([num1, func, num2, _, "?"])
    
    return answer

express = ["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]
print(solution(express))