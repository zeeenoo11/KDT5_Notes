# ---------------------------------------------------------
# <팀원 간 공유하는 정보> (예시)
# 함수 기능 : 유동적인 변수 개수를 받는 함수
#            *data : 0 ~ 개
# 함수 이름 : programInfo
# 매개 변수 : 없음
# 반 환 값 : str
# ---------------------------------------------------------
def typeIs(*x):
    return type(x), sum(x)

print(typeIs(1, 2, 3))
print(typeIs())
print(typeIs(1))

# range, list 등 시퀀스일 때: * -> 언패킹 후 하나씩 전달
print(typeIs(*range(1,11)))

# * 사용 예시2
list1 = [1,2,3,4]
print(*list1,sep='-')

a = [11,22,33,44]
aTuple = 'a', 'b', 'c'
aDict = {'jj':100, 'title1':200}

# Dict 에선 ** : value
print(*aDict, sep=', ')    # jj, title1
