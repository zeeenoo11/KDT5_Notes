# --------------------------------
# str 관련 내장 함수
# --------------------------------
# len()
msg = 'MerryChristmas2024!'
print(f'len(msg) => msg')
print(len("2024"))


# ord( ) : 코드값 출력하기 (인코딩)
print(ord('A'))
code_H = ord('H')
code_e = ord('e')
code_l = ord('l')
code_o = ord('o')
print('Hello ->', bin(code_H)[2:], bin(code_e)[2:], bin(code_l)[2:], bin(code_l)[2:], bin(code_o)[2:])
# 시험 내기 좋은 유형

# 글자 간 간격
print(ord('5') - ord('0'))

# chr( ) : 코드값을 문자로 변환하기 (디코딩)
print(chr(65))