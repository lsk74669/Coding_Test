def solution(keymap, targets):
    min_presses = {}

    for i, keys in enumerate(keymap):
        for idx, char in enumerate(keys):
            if char in min_presses:
                min_presses[char] = min(min_presses[char], idx + 1)
            else:
                min_presses[char] = idx + 1

    answer = []
    for target in targets:
        press_cnt = 0
        for char in target:
            if char in min_presses:
                press_cnt += min_presses[char]
            else:
                press_cnt = -1
                break
        answer.append(press_cnt)
    
    return answer
