def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}
    
    for call in callings:
        idx = rank[call]
        if idx > 0:
            pre_player = players[idx - 1]  
            players[idx - 1], players[idx] = players[idx], players[idx - 1]
            rank[call] -= 1
            rank[pre_player] += 1
    
    return players
