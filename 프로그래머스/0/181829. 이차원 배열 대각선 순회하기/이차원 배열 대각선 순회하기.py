def solution(board, k):
    answer = 0
    
    num_rows = len(board)
    num_cols = len(board[0])
    
    for i in range(num_rows):
        for j in range(num_cols):
            if i + j <= k:
                answer += board[i][j]
                
    return answer
