# ---------------------------------------------------
# list type
# - 여러 종류의 여러 개의 데이터를 저장하는 타입
# - 문법 : [element1, element2, ... ]
# - 특징 : 데이터 하나 하나를 요소element라 한다
#          인덱싱
# ----------------------------------------------------
# 리스트 데이터 생성
# 숫자를 메모리에 저장
list1 = [10, 10, 20, 30, 40, 50]
print('id(list1) ->',id(list1))
print('id(list1[0]) ->',id(list1[0]))
print('id(list1[1]) ->',id(list1[1]))
print('id(list1[2]) ->',id(list1[2]))
print("마지막 3개만 출력하기:",list1[-3:])
print("짝수 인덱스만 출력하기:",list1[::2])

# 다양한 데이터 타입이 올 수 있다: 실수, str, bool, list
mixture = [10, '10', 'Hi', False, ['a', 'b']]
print('mixture[0] =>', mixture[0], type(mixture[0]))
print('mixture[1] =>', mixture[1], type(mixture[1]))
print('mixture[2] =>', mixture[2], type(mixture[2]))
print('mixture[3] =>', mixture[3], type(mixture[3]))
print('mixture[4] =>', mixture[4], type(mixture[4]))
# 리스트 내 리스트 요소 호출: list[0][0]
print(mixture[4][0])