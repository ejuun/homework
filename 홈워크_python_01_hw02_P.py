s = input('숫자를 입력해주세요 : ')

s_list = list(s)
s_sum = 0

for i in range(len(s_list)):
    s_sum += int(s_list[i])

print(s_sum)
