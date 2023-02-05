# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 
#-----------------------------------------------------
#HINT
#문자열 자체 정렬(사전순)

#sorted

#문자열 합치기
# word_dict = {}
#if 'aet' not in word_dict:
#   word_dict['aet'] = ['eat']
#else:
#   word_dict['aet'].append('')
# 딕셔너리에 저장 키값으로(sotred), value에 원래 값 grouping
#.join(iterable(문자열))

# a= ''.join(['a','e','t'])
# print(a)

# b = '-',map(str,[1,2,3])
# print(b)

# A = ['eat','tea','tan','ate','nat','bat']

# sort_A = []
# for i in range(len(A)):
#     sort_A.append(sorted(A[i]))
# sorset = set([''.join(j) for j in sort_A])
# print(sorset)

A = ['eat','tea','tan','ate','nat','bat']

dic_A = {}
for str in A:
    s= ''.join(sorted(str))
    dic_A[s] = dic_A.get(s,[]) + [str]
print(list(dic_A.values()))