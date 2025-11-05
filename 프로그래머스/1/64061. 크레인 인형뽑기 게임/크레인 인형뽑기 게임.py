def solution(board, moves):
    stack = []
    cnt = 0

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                if stack and stack[-1] == board[i][move-1]:
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(board[i][move-1])
                board[i][move-1] = 0
                break
    return cnt