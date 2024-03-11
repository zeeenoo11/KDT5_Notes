# 1. 데이터 저장하기
# 1.1 이메일
num1 = 'kim1234@naver.com'
print(num1[:7])
# 1.2 도메인 이름
num2 = 'http://www.naver.com'
print(num2[11:])
# 1.3 이름 출력
num3 = '홍길동'
print(num3[1:])
# 1.4 대문자, 소문자 분리; 홀짝 구분
num4 = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
print(num4[::2])
print(num4[1::2])
# 1.5 숫자 출력
num5 = 'ABC1DRF2GHI3JKL4MNO5PQR6STU7VWX8YZ'
print(num5[3::4])
# 1.6 주민번호에서 생년월일과 숫자 구분
num6 = '881120-1068234'
print(num6[:6])
print(num6[7:])

# 2. 2, 8, 16진수 출력
decimal1 = int(input('[입력] 정수 입력 : '))
print(f"""[출력]
10진수 : {decimal1}
16진수 : {hex(decimal1)} 
8진수  :  {oct(decimal1)}
2진수  : {bin(decimal1)}""")

# 3. 3개 단어 받고 가장 큰 단어, 작은 단어 출력
# 3.1 단어 입력
print('[입력] ',end='')
word1, word2, word3 = input(), input(), input()

# 3.2 비교하고 출력하기
print(f"""[출력] 코드 값이 가장 큰   단어 : {max(word1,word2,word3)}
\t   코드 값이 가장 작은 단어 : {min(word1,word2,word3)}""")

# 4. 조건을 만족하는 코드 작성
line1 = '"오늘은 행복한 목요일입니다."'
print("[내가 정한 메시지]",line1)
in_word = input("[입력] 단어 입력 : ")
print("[출력]", in_word, "단어 메시지 존재 여부 : ",in_word in line1)

# 5. 코드 작성
word_code = input('단어 입력 : ')
print("[출력]",word_code,"코드값 :",hex(ord(word_code[0])),hex(ord(word_code[1])),hex(ord(word_code[2])))
