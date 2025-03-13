h_now, m_now = map(int, input().split())
roast = int(input()) + m_now

print((roast//60 + h_now)%24, roast%60)