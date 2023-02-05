# 입력 예시
A = [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]

new_list = []
new_list.append(A[0])

for i in range(len(A)-1):
    if A[i+1] !=A[i]:
        new_list.append(A[i+1])

print(new_list)