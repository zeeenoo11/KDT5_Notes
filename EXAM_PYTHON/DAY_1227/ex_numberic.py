# --------------------------------------------------------
# 수치 데이터 살펴보기
# 정수 -> class int
# 실수 -> class float
# -------------------------------------------------------
# [실습] 2개 정수를 입력 받기
# -> input() 함수 2개 사용
# -> str => int 타입 캐스팅
num1 = int(input('정수1: '))
num2 = int(input('정수2: '))

print("%d > %d => %s" %(num1, num2, num1>num2))
# 마찬가지로  > < <= >= == != 가능

# 86페이지까지!
# 연습 문제
DISTANCE  = 12   # m 단위
print(0.2467 * DISTANCE + 4.159)

# 심사 문제
AP = 102
damage = AP * 0.6 + 225
print(damage)


a,b,c = map(int, input('세 정수 입력:').split())
print(a+b+c)


korean, english, math, science = map(int, input().split())
avg = (korean + english + math + science) / 4
print('average =', int(avg))