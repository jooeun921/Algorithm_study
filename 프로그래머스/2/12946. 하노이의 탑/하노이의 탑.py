def solution(n):
    
    def hanoi(n, start, end, via, moves):
        if n == 1:
            moves.append([start, end])
            return
        
        hanoi(n-1, start, via, end, moves)
        moves.append([start, end])
        hanoi(n-1, via, end, start, moves)

    moves = []
    hanoi(n, 1, 3, 2, moves)    
    
    return moves