def solution(s):
    num_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i, word in enumerate(num_words):
        s = s.replace(word, str(i))
    
    return int(s)
