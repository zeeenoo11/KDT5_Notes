# -------------------------------------------
# <팀원 간 공유하는 정보> (예시)
# 함수 기능 : 팩토리얼 계산 후 결과 반환
# 함수 이름 : Factorial
# 매개 변수 : x
# 반 환 값 : ret
# -------------------------------------------
def Factorial(x):
    ret = 1
    for i in range(1,x+1): ret *= i
    return ret
# -------------------------------------------
# <팀원 간 공유하는 정보> (예시)
# 함수 기능 : 팩토리얼 계산 후 문자열 반환
#            예시) 3! = 3 * 2 * 1
# 함수 이름 : Factorial2
# 매개 변수 : x
# 반 환 값 : 계산 문자열
# -------------------------------------------
# 1안 : 차례로 출력
def Factorial2(x):
    print(f'{x}! =',end=' ')
    for i in range(x,1,-1):
        print(i,end=' * ')
    print('1 =', Factorial(x))
    return                        # None 출력 안하려면? -> print() X
# 2안: str에 덧붙이기
def Factorial2_2(x):
    intRet = 1
    strRet = f"{str(x)}! = "
    for i in range(x,0,-1):
        intRet *= i
        strRet += str(i) + (' * ' if i != 1 else ' = ')
    strRet += str(intRet)
    return strRet
# ------------------------------------------------
x_input = int(input('Enter Number: '))
print(Factorial(x_input))
print()
Factorial2(x_input)             # 자체 print 있으므로 호출만
print()
print(Factorial2_2(x_input))
