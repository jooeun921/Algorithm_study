def solution(record):
    answer = []
    id_name = {}
    command_list = []

    for i in range(len(record)):
        command, id, *name = map(str, record[i].split(' '))
        if command == 'Enter':
            id_name[id] = name[0]
            command_list.append([command, id])
        elif command == 'Leave':
            command_list.append([command, id])
        elif command == 'Change':
            id_name[id] = name[0]
    
    for com, id in command_list:
        if com == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(id_name[id]))
        elif com == 'Leave':
            answer.append("{}님이 나갔습니다.".format(id_name[id]))
    
    return answer