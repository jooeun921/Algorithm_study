def solution(n, w, num):
    box_list = {}
    
    for i in range(n):
        box_num = i + 1
        row = i // w
        col_row = i%w
        if row % 2 == 0:
            col = w-1-col_row
        else:
            col = col_row
        box_list[box_num] = (row, col)
        
    target_row, target_col = box_list[num]
    cnt = 0
    
    for box, (r, c) in box_list.items():
        if c == target_col and r >= target_row:
            cnt += 1
    return cnt