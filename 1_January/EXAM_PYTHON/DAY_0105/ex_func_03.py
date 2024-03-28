# ------------------------------------------------------
# 다양한 함수의 형태 - (2) 반환값이 없는 함수
# ---------------------------------------------------------
# <팀원 간 공유하는 정보> (예시)
# 함수 기능 : 2개의 숫자의 합계를 계산한 후 결과를 반환
# 함수 이름 : addTwo
# 매개 변수 : x , y
# 반 환 값 : 없음
# ---------------------------------------------------------
def addTwo(x, y):
    value = x + y
    print(f'{x} + {y} = {x+y}')
    # 반환값 없음

# 함수 호출
addTwo(1,2)

# 특징 : 매개 변수와 동일한 수의 데이터를 입력해야한다
# ---------------------------------------------------------
# <팀원 간 공유하는 정보> (예시)
# 함수 기능 : 입력된 영단어를 모두 대문자로 변환
# 함수 이름 : convertCase
# 매개 변수 : word
# 반 환 값 : 없음
# ---------------------------------------------------------
def convertCase(word):
    word = word.upper()

# ---------------------------------------------------------
# <팀원 간 공유하는 정보> (예시)
# 함수 기능 : 시퀀스 객체의 원소 모두 대문자로 변환
# 함수 이름 : convertCase2
# 매개 변수 : dataList(list consisted of  str)
# 반 환 값 : 없음
# ---------------------------------------------------------
def convertCase2(dataList):
    # for idx in range(len(dataList)):
    #     dataList[idx] = dataList[idx].upper()
    # for idx,data in enumerate(dataList):
    #     dataList[idx] = data.upper()
    listRet = list(map(lambda x: x.upper(), dataList))
    return listRet # 얘는 dataList를 바꾸진 않음

datas = ["a", "b", "c", "d"]
print(convertCase2(datas))
print(datas)

# return이 필요한 경우: 이렇게 리턴값을 정할 수 있다
def convertCase_return(word):
    return word.upper()

print(convertCase_return('Apple'))