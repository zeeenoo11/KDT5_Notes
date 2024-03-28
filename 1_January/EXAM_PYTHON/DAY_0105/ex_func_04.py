# ------------------------------------------------------
# 다양한 함수의 형태 - (3) return 키워드
# - 함수를 즉시 종료할 수 있다
# ---------------------------------------------------------
def Factorial(x):
    if not x:      # x가 0일때; 즉시 함수 종료
        return 1   # 1을 출력하는 것; 값이 없으면 None
    ret = 1
    for i in range(1,x+1): ret *= i
    return ret

print(Factorial(0))   # 1
print(Factorial(10))   # 6
