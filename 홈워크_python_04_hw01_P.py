words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

before_words = []

for i in range(len(words)-1):
    if i >= 1:
        before_words.append(words[i-1])

    if words[i+1][0] != words[i][-1]:
        print(f'{i+1}번 졌습니다. 끝말잇기가 틀렸습니다.')
        break

    for j in range(len(before_words)):
        if words[i] == before_words[j]:
            print(f'{i+1}번 졌습니다. 이전 등장했던 단어{before_words[j]}를 사용했습니다.')
            break

  