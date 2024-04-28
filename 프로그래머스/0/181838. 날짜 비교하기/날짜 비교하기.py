import datetime

def solution(date1, date2):
    date_1 = datetime.datetime(date1[0], date1[1], date1[2])
    date_2 = datetime.datetime(date2[0], date2[1], date2[2])
    
    if date_1 < date_2:
        return 1
    else:
        return 0
