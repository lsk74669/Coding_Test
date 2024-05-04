def solution(n):
    answer = [[0]*n for _ in range(n)]
    
    x, y = 0, 0
    dx, dy = 0, 1
    current = 1
    
    while current <= n*n:
        answer[x][y] = current
        current += 1
        
        nx, ny = x + dx, y + dy
        
        if nx >= n or ny >= n or nx < 0 or ny < 0 or answer[nx][ny] != 0:
            if dx == 0 and dy == 1:
                dx, dy = 1, 0
            elif dx == 1 and dy == 0:
                dx, dy = 0, -1
            elif dx == 0 and dy == -1:
                dx, dy = -1, 0
            elif dx == -1 and dy == 0:
                dx, dy = 0, 1
            nx, ny = x + dx, y + dy
        
        x, y = nx, ny

    return answer