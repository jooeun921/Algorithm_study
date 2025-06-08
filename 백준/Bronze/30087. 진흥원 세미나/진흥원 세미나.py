N = int(input())

s_dict = {'Algorithm':204, 'DataAnalysis':207, 'ArtificialIntelligence':302, 'CyberSecurity':'B101', 'Network':303, 'Startup':501, 'TestStrategy':105}

for _ in range(N):
    s = input()
    if s in s_dict:
        print(s_dict[s])
