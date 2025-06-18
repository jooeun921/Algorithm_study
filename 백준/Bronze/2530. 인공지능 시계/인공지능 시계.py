h, m, s = map(int, input().split())
cook = int(input())

total = (h*3600 + m*60 + s + cook)%(24*3600)
h_new = total//3600
m_new = (total%3600)//60
s_new = total%60

print(h_new, m_new, s_new)