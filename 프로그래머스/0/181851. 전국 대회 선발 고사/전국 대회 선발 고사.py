def solution(rank, attendance):
    rank_dict = {}
    idx_list = []
    
    for idx, r in enumerate(rank):
        rank_dict[r] = idx
    
    for i in range(1, len(rank)+1):
        if attendance[rank_dict[i]] == True:
            idx_list.append(rank_dict[i])
    
    answer = 10000*idx_list[0] + 100 * idx_list[1] + idx_list[2]      
    
    return answer