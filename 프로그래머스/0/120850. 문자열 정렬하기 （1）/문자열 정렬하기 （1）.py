def solution(my_string):
    numbers = [int(char) for char in my_string if char.isdigit()]
    return sorted(numbers)