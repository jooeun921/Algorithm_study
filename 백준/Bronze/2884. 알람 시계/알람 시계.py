h, m = map(int, input().split())
h_li = list(range(0, 24))
if m < 45:
    m_ans = 15 + m
    h_ans = h_li[h-1]
else:
    h_ans = h
    m_ans = m - 45
print(h_ans, m_ans)