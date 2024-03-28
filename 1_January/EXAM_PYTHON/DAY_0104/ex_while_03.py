# ----------------------------------------------
# 반복문 while : 반복의 횟수가 정해지지 않은 경우
# -----------------------------------------------
# [요청] 사용자가 'x' 입력 전까지 저장하기
# -----------------------------------------------
"""
data = []
while True:
    word = input('Input here: ')
    if word.lower() != 'x':
    # if word in ('x', 'X'):      # in 함수도 가능!
        data.append(word)
        print('OK')
    else: break
print(data)
"""
# -------------------------------
# [요청] 사용자로부터 x/X, 입력 전까지 계속 정수 입력
#        입력 받은 정수만큼 알파벳 출력
# [예시] 출력 원하는 알파벳 수 입력 : 5
#        abcde
# [예시] 출력 원하는 알파벳 수 입력 : 27
#        abcd ....z <End>
# [예시] 출력 원하는 알파벳 수 입력 : x
#        <End>
# --------------------------------
"""
# 조건부 무한 반복
while True:
    # 0. 정수 입력
    alpha_num = input("Numbers of Alphabet : ")
    # 1. 숫자 입력
    if alpha_num.isdigit():
        # 1.1 under 26
        if int(alpha_num) <= 26:
            str_total = ""         # str 입력으로 해보기
            for i in range(int(alpha_num)):
                str_total += chr(97+i)
            print(str_total)

        else: # 1.2 over 27 -> <End>
            for i in range(26):
                print(chr(97+i),end='')   # 바로 출력해보기
            print(" <End>")
            break

    # 2. 'x' 입력
    elif alpha_num.lower() == 'x':
        print("<End>"); break

    # 3. 이외 문자 입력 시 오류 출력
    else: print("Wrong Number, Try Again.")
"""

# isEnd 사용법
"""
isEnd = False
for n in range(100):
    if isEnd: break  # flag 심어두기 (isEnd)

    print('out: ', n)

    for n2 in range(100):
        if n2 > 10:
            isEnd = True
            break
        print(n2, ':', n, '번째')
"""

n, n2, isEnd = 1, 1, False
while n < 100:
    if isEnd: break
    print('out: ', n)
    while n2 < 100:
        if n2 > 10:
            isEnd = True; break
        print(n2,':',n,'번째')
        n2 += 1
    n += 1