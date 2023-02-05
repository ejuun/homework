str_lst = input('문자열을 입력하세요. : ').split()

for i in range(len(str_lst)):
    str_lst[i] = str_lst[i].lower()

count = 0
for j in range(len(str_lst)-1):
    if str_lst[j+1][0] != str_lst[j][-1]:
        count +=1

if count >=1:
    print('Fail') 
else:
    print('Pass')
