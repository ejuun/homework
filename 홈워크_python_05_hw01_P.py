# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}
#달력 출력 : calendar.calendar
#윤년 출력 : calendar.isleap(year)
#calendar.MONDAY

# calendar.weekday(year, month, day)
import calendar

year = int(input())

isleap = calendar.isleap(year)

while True:
    if isleap == True:
        print('윤년입니다. 연도를 다시 입력해주세요.')
        year = int(input())
        isleap = calendar.isleap(year)

    else:
        cal = calendar.calendar(year)
        print(cal) 
        break

year1 = int(input())
month = int(input())
day = int(input()) 

date_dict = {}
date_dict['년'] = year1
date_dict['월'] = month
date_dict['일'] = day

date = calendar.weekday(year1, month, day)
if date == 0 :
    print('경고 월요일입니다.')    
    date_dict['요일'] = '월요일'
    print(date_dict)
elif date == 1 :
    print('화요일입니다.')    
    date_dict['요일'] = '화요일'
    print(date_dict)
elif date == 2 :
    print('수요일입니다.')    
    date_dict['요일'] = '수요일'
    print(date_dict)
elif date == 3 :
    print('목요일입니다.')    
    date_dict['요일'] = '목요일'
    print(date_dict)
elif date == 4 :
    print('금요일입니다.')    
    date_dict['요일'] = '금요일'
    print(date_dict)
elif date == 5 :
    print('토요일입니다.')    
    date_dict['요일'] = '토요일'
    print(date_dict)
elif date == 6 :
    print('일요일입니다.')    
    date_dict['요일'] = '일요일'
    print(date_dict)    