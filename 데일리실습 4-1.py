pass_word = 1234

chance = 0
while chance < 3:
    pw_input = int(input('비밀번호를 입력하세요 :'))
    if pw_input == pass_word:
        print('맞았습니다.')
        break
    else:
        chance += 1
        print(f'틀렸습니다. {chance}번 틀렸습니다.')
        
