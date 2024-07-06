def solution(keyinput, board):
    position = [0, 0]
    
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    move = {
        'up': [0, 1],
        'down': [0, -1],
        'left': [-1, 0],
        'right': [1, 0]
    }
    
    for key in keyinput:
        dx, dy = move[key]
        new_x = position[0] + dx
        new_y = position[1] + dy
        
        if -max_x <= new_x <= max_x:
            position[0] = new_x
        if -max_y <= new_y <= max_y:
            position[1] = new_y
    
    return position