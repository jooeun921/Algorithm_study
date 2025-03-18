import re
alpha = 'c=|c-|dz=|d-|lj|nj|s=|z='
cra = input()
result = re.sub(alpha, 'X', cra)  # 패턴을 'X'로 치환
print(len(result))