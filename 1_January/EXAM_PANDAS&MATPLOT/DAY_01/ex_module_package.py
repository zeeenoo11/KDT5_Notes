# ------------------------------------------------------
# 모듈과 패키지
# - 관계
#   * 모  듈 : 특정 기능/목적의 변수, 함수, 클래스를 저장한 하나의 파이썬 파일.py
#   * 패키지 : 특정 기능/목적의 모듈을 담고 있는 단위
# - 문법 : import 모듈명 (or 패키지명)
# -------------------------------------------------------
# 사용할 모듈 로딩
import math                  # 내장 모듈 : math 모듈 내 모든 변수, 함수, 클래스 다 사용
import math as m             # 별칭 지정
from math import factorial   # 모듈 내 특정 함수만 사용 -> 바로 사용 가능
from math import factorial as fac   # 함수명의 별칭

# 사용자 정의 함수
def factorial(x):    # 똑같은 이름을 쓰면 사용자 지정이 사용된다
    return x         # 그럼 가져온 모듈에 별칭 지정하면 댐


# 모듈 내의 요소(변수, 함수, 클래스) 사용 방법
# -> 모듈명.변수 or 모듈명.함수()
print(math.pi, math.pow(2,3))

# 별칭 활용
print(m.pi)

# from Module import Function 형식
print(factorial(4))   # 모듈명 없이 바로 사용
print(fac(4))         # 함수 별칭 활용