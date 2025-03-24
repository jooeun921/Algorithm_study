def solution(video_len, pos, op_start, op_end, commands):
    def time_to_seconds(t):
        minutes, seconds = map(int, t.split(":"))
        return minutes * 60 + seconds
    
    def seconds_to_time(s):
        minutes = s // 60
        seconds = s % 60
        return f"{minutes:02}:{seconds:02}"

    pos_seconds = time_to_seconds(pos)
    video_len_seconds = time_to_seconds(video_len)
    op_start_seconds = time_to_seconds(op_start)
    op_end_seconds = time_to_seconds(op_end)

    if op_start_seconds <= pos_seconds <= op_end_seconds:
        pos_seconds = op_end_seconds
    
    for command in commands:
        if command == "prev":
            pos_seconds -= 10
            if pos_seconds < 0:
                pos_seconds = 0
        elif command == "next":
            pos_seconds += 10
            if pos_seconds > video_len_seconds:
                pos_seconds = video_len_seconds

        if op_start_seconds <= pos_seconds <= op_end_seconds:
            pos_seconds = op_end_seconds

    return seconds_to_time(pos_seconds)
