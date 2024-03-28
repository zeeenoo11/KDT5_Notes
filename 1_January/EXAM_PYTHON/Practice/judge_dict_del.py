# -----------------------------------------------------------
# 25장 : 문자열 여러 개와 숫자 여러 개가 두 줄로 입력
#        첫 번째 줄은 키, 두 번째 줄은 값으로 딕셔너리 생성
#        키가 'delta', 값이 30인 두 키-값을 삭제하시오
# -----------------------------------------------------------
keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

# x에 새로 딕셔너리 입력; key가 delta이거나 value가 30이면 포함하지 않음
x = {key:value for key, value in x.items() if key != 'delta' and value != 30}

print(x)