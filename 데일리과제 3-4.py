s_triangle = map(str,input().split())

s_list = [int(str) for str in s_triangle]

sorted(s_list)

if s_list[0] == s_list[1] == s_list[2]:
    print('정삼각형')
elif s_list[1] == s_list[0] or s_list[1] == s_list[2]:
    print('이등변삼각형')
    if s_list[2] **2 == (s_list[0] **2) + (s_list[1] **2):
        print('직각 이등변 삼각형')
elif s_list[2] **2 == (s_list[0] **2) + (s_list[1] **2):
    print('직각 삼각형')
elif s_list[2] < s_list[0] + s_list[1]:
    print('삼각형')
else:
    print('삼각형이 아닙니다.')