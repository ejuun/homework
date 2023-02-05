# fn_d(91) 
# 출력 예시 
# 101

#d(123) = 1+2+3+123 

#1
# d = int(input())
# n = int(input())
# k = int(input())

def  fn_d(n):
    sum_number = 0

    n = str(n)

    for i in n[::]:
        sum_number += int(i)
    sum_number += int(n)
    return print(sum_number)