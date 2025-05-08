N, M, K = map(int, input().split())

max_teams = 0
for teams in range(0, 51):
    if N >= teams * 2 and M >= teams and N + M - teams * 3 >= K:
        max_teams = teams

print(max_teams)
