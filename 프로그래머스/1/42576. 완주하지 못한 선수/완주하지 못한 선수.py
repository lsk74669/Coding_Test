def solution(participant, completion):
    participant_dict = dict()
    for part in participant:
        participant_dict[part] = participant_dict.get(part, 0) + 1
    
    for comp in completion:
        if comp in participant_dict:
            participant_dict[comp] -= 1
    
    for part in participant_dict:
        if participant_dict[part] == 1:
            return part
    return 0