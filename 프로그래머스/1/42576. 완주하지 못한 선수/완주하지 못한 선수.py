from collections import defaultdict

def solution(participant, completion):
    participant_dict = defaultdict(int)
    
    for p in participant:
        participant_dict[p] += 1
    
    for c in completion:
        participant_dict[c] -= 1
        if participant_dict[c] == 0:
            del participant_dict[c]
    
    return list(participant_dict.keys())[0]
