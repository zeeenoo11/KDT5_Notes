# -----------------------------------------
# 리스트 안에 모든 원소를 더한 합계 출력
# -----------------------------------------
datas = ['1', '4', '9']   # int로 반환해야함

# for문으로 하나씩 변경
for idx, d in enumerate(datas):
    datas[idx] = int(d)

# 내장함수 map()
datas = list(map(int, datas))
print(datas)

# ------ [추가] 모든 원소에 *100 ---------
# 1. 함수를 선언하기
def multiValue(x):
    return x*100
datas = list(map(multiValue, datas))
print(datas)

# 2. lambda 사용
datas = list(map((lambda x:x*100), datas))
print(datas)

# 인사말 출력:
def greeting():
    print('Hi')

greeting()   # 함수 만들어서 표현하기
print((lambda : "Hi")())  # 람다로 표현하기

