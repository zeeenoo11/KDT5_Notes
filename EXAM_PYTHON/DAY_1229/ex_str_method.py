# ------------------------------------------------
# str 데이터 타입 전용의 함수: 메서드(Method)
# o 메서드 :
#       1. 특정 데이터 타입에서만 사용 가능한 함수
#       2. int method, float method 라고 부름
#       3. . 을 찍어 사용: 변수명.method()
#       4. 예) msg.upper()        "goood".upper()
# ------------------------------------------------

print('Good'.lower())   # .lower()
print('Good'.upper())   # .upper()
print("GOOD".isupper())  # .isupper()
print("good".islower())  # .islower()

print("123".isdecimal()) # .isdecimal()
print("A".isalpha(), "한글".isalpha()) # .isalpha()
# "한글"도 .isalpha(), .isalnum() 가능!

# .startswith() .endswith()
print("!12#".startswith('!'))
print("!12#".endswith('#'))
print("image_001.jpg".endswith('jpg'))
print("image_001.jpg".endswith(('jpg','png')))

# .replace('old', 'new')
name = 'Guldongu'
print(name.replace('ul','i'))    # 모든 'u'를 'i'로 바꿈
