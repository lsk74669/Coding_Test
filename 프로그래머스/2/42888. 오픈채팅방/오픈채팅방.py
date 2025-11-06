def solution(record):
    user_dict = {}
    for r in record:
        if r.split()[0] in ('Enter', 'Change'):
            user_dict[r.split()[1]] = r.split()[2]
    result = []
    for r in record:
        if r.split()[0] == 'Enter':
            result.append(f'{user_dict[r.split()[1]]}님이 들어왔습니다.')
        elif r.split()[0] == 'Leave':
            result.append(f'{user_dict[r.split()[1]]}님이 나갔습니다.')
    return result