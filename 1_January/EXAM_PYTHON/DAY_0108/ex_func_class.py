# ----------------------------------------------
# 함수와 클래스
# ----------------------------------------------
# 변수에 어떤 데이터를 저장하고 있는 지 확인 함수 -> type(함수명)
import random

data = 1
print(f'data type -> {type(data)}') #  data type -> <class 'int'>

data = 'Good'
print(f'data type -> {type(data)}') # data type -> <class 'str'>

# 함수명의 타입 : 'builtin_function_or_method' = 내장함수
print(f'id() type -> {type(id)}')   # id() type -> <class 'builtin_function_or_method'>

# 사용자 정의 함수의 타입 확인하기
# --------------------------------------------------
# 함수 기능 : 2개 정수 더한 후 결과 출력 가능
# 함수 이름 : addTwo
# 매개 변수 : n1, n2
# 함수 결과 : 없음
# --------------------------------------------------
def addTwo(n1, n2):
    print(n1+n2)

# 함수의 타입 출력 : 'function' => 함수도 클래스에 속하는 객체이다
print(type(addTwo))     # <class 'function'>


# ----------------------------------------------------
# 함수와 변수
# - 함수명은 코드의 시작 주소를 저장하고 있음
# - 함수명을 변수에 대입 가능
# ----------------------------------------------------
test = addTwo

print(f'test   => {id(test), type(test)}') # test   => (1707343491280, <class 'function'>)
print(f'addTwo   => {id(addTwo), type(addTwo)}') # addTwo   => (1707343491280, <class 'function'>)
# 두 주소가 같다: 변수에 함수 주소를 저장 가능하다!

test(1,2)
addTwo(4,5)  # 둘다 addTwo 함수에서 연산을 한다
# ----------------------------------------------
# [활용 예]
# - 1~10 범위에서 임의의 정수 5개를 저장
# - 중복된 정수 저장 가능
# ----------------------------------------------

randList = [random.randint(1,10) for num in range(5)]
# 교수님은 num, for, append 순으로 작성
print(randList)

# 5개의 정수에서 최대값, 최소값, 내림차순 정렬된 값 출력

print(f'최대값 : {max(randList)}')
print(f'최소값 : {min(randList)}')
print(f'정 렬 : {sorted(randList,reverse=True)}')
print(f'합 계 : {sum(randList)}')
print(f'갯 수 : {len(randList)}')

# 여러 개의 "함수 이름"을 변수에 저장 => 리스트 사용

funcs = [max, min, sorted, sum, len]
for func in funcs:
    if func == sorted:       # sorted 내림차순 : 따로 분류해서
        print(func(randList, reverse=True)) # reverse=True
    else: print(func(randList))

# => 함수명 저장 후 print(func(randList)) 하면 연산이 된다!

# funcs = [max, min, sorted, sum, len]
# keys = ['최대값','최소값','정 렬','합 계', '갯 수']
# randDict = dict(zip(keys, funcs))
# print(randDict)
# randDict = {'최대값': max, '최소값': min, '정 렬': sorted, '합 계': sum, '갯 수': len}

# ----------------------------------------------
# [활용 예2]
# - 1~10 범위에서 임의의 정수 5개를 저장
# - 중복된 정수 저장 가능
# - (New!) 안내문 넣기 (예: '최댓값 : ')
# ----------------------------------------------
# 딕셔너리로 출력문 앞 단어 넣기
randDict = {'최대값': max, '최소값': min, '정 렬': sorted, '합 계': sum, '갯 수': len}
for name, func in randDict.items():
    if func == sorted:       # sorted 내림차순 : 따로 분류해서
        print(name,':',func(randList, reverse=True)) # reverse=True
    else: print(name,':',func(randList))


# { : } 내에서 ^ 가운데 정렬, > 오른쪽 정렬

# 매개 변수 이름을 입력하는 이유: 그냥 변수를 똑같은 이름으로 선언,,
# 헷갈릴텐데 왜 그러시지 : 글로벌과 지역의 차이를 보여주는 것?
#