entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

import collections
en_count = collections.Counter(entry_record)
ex_count = collections.Counter(exit_record)
#1
sorted_en = sorted(en_count.items(), key=lambda x:x[1], reverse= True)

print('입장 기록 많은 Top3')
i = 0
while i <3:
    print(f'{sorted_en[0][0]} {sorted_en[0][1]}회')
    i+=1
    sorted_en.pop(0)
print('')
#2
en_ex = en_count - ex_count #입장 - 퇴장(입장 기록이 더 많다)
ex_en = ex_count - en_count #퇴장 - 입장(퇴장 기록이 더 많다)
print('출입 기록이 수상한 사람')
for i,j in en_ex.items():
    print(f'{i}은 입장 기록이 {j}회 더 많아 수상합니다.')
for a,b in ex_en.items():
    print(f'{a}은 퇴장 기록이 {b}회 더 많아 수상합니다.')