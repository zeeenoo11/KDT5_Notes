# -----------------------------------------------
# 메서드 두 번째 강의
# -----------------------------------------------
data = "Merry Christmas"

print('index of C :',data.index('C'))      # 문자의 위치를 알려준다
print('index of Ch :',data.index('Ch'))    # 문자열도 가능

print('index of r :',data.index('r',7))    # start: 시작 인덱스
first_r = data.index('r')
second_r = data.index('r',first_r+1)
third_r = data.index('r',second_r+1)

print('index of r :',data.index('r',first_r+1))           # start: 1st 인덱스 +1
print('index of r :',data.index('r',data.index('r')+1))   # 많이 안쓰면 안에 넣어두자

# ! 의 인덱스를 찾기 : 없으면 Error
# print(f"data.index(!) -> {data.index('!')}")    # ValueError: substring not found

# find : 없어도 Error 뜨지 않는다; -1을 반환
print(data.find('!'))


"""
.split() : 문자열을 분리
"""
data = "Happy New Year"

# str 에서 공백을 기준으로 str 나누기
datas = data.split()
print(type(datas),datas)

# list에 저장된 원소 하나씩 읽기
print(f"datas[0] => {datas[0]}")
print(f"datas[1] => {datas[1]}")
print(f"datas[2] => {datas[2]}")
