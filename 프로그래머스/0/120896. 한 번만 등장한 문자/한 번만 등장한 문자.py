def solution(s):
    return "".join(sorted([ cha for cha in set(s) if s.count(cha) == 1]))