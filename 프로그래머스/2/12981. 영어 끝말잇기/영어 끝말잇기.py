def solution(n, words):
    used_words = set() 
    prev_word = words[0][0]

    for i, word in enumerate(words):
        if word in used_words or word[0] != prev_word[-1] or len(word) < 2:
            person = (i % n) + 1  
            turn = (i // n) + 1  
            return [person, turn]
        
        used_words.add(word)
        prev_word = word  
    
    return [0, 0]