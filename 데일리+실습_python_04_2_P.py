students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

dic_student = {}
for stu in students:
    if stu in dic_student:
        dic_student[stu] += 1
    else:
        dic_student[stu] = 1
        
print(dic_student)