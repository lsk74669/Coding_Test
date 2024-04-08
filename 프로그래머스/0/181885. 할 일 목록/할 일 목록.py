def solution(todo_list, finished):
    answer = []

    for idx, fin in enumerate(finished):
        if fin == False:
            answer.append(todo_list[idx])
    return answer