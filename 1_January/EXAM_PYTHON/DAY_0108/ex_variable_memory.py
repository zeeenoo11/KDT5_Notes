# ---------------------------------------------
# 참조형 변수 -> 데이터의 주소 저장
# ---------------------------------------------
num = 12
print(f'num -> {id(num)}, {type(num)}') # num -> 140719703534848, <class 'int'>

num = 3.
print(f'num -> {id(num)}, {type(num)}')

num = 'Hi'
print(f'num -> {id(num)}, {type(num)}')

num1 = []
print(f'num1 -> {id(num1)}, {type(num1)}')

num2 = [1, 2.1]
print(f'num2 -> {id(num2)}, {type(num2)}')
print(f'num[0] -> {id(num2[0])}, {type(num2[0])}')
print(f'num[1] -> {id(num2[1])}, {type(num2[1])}')

print('-'*50) # 값 변경

num2[0] = 100
print(f'num2 -> {id(num2)}, {type(num2)}') # num -> 2065583762624, <class 'list'>
print(f'num[0] -> {id(num2[0])}, {type(num2[0])}') # num[0] -> 140719703537664, <class 'int'>
# num의 주소는 바뀌지 않고 num[0]의 주소만 바뀐다.

num2 = num1
print(f'num2 -> {id(num2)}, {type(num2)}')
print(f'num1 -> {id(num1)}, {type(num1)}')