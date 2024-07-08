def solution(spell, dic):
    sorted_spell = ''.join(sorted(spell))
    
    for word in dic:
        if ''.join(sorted(word)) == sorted_spell:
            return 1
    return 2