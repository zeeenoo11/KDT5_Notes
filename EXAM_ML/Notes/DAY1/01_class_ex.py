

# < 클래스 >
# - 구성 요소 : 매서드(함수) + 속성/필드(변수)
# - 구성 요소 종류
#       - 클래스 변수(클래스 속성)
#           : 클래스 내부에 선언된 변수
#             인스턴스 생성 없이 사용 가능
#       - 인스턴스 변수(인스턴스 속성)
#           : 인스턴스 변수는 인스턴스 생성 시 동적으로 할당
#             반드시 인스턴스 생성 후 사용 가능
# ======================================================
# (클래스 예시)
# class A:
#   manufact = 'KIA'            # = 클래스 변수
#   def __init__(self):
#       self.field1 = 'type'   # = 인스턴스 변수
# ------------------------------------------------------
# [ 클래스 생성 ]
# - 구성요소 : 속성 + 매서드 => 모두 없는 클래스
# - 기본 상속 : Object => __속성명__ 또는 __메서드명__
class A:
    pass

# [ 객체 인스턴스 생성 ]
# => 생성 함수: 클래스이름()

a1 = A()

# [ 속성과 매서드 확인하기 ]
# - __dict__ : 딕셔너리 형태로 클래스 내부 모든 속성과 메서드 확인 가능
# - __dir__() : 클래스 내부 모든 속성과 메서드 확인 가능

print("A 인스턴스 a1의 속성과 메서드 =>", a1.__dict__)      # {}
print("A 인스턴스 a1의 속성과 메서드 =>", a1.__dir__())
# ['__module__', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']#
# => 인스턴스 변수까지

print("A 클래스의 속성과 메서드     =>", A.__dict__)
# {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
# print("A 클래스 a1 속성과 메서드  =>", A.__dir__()    # 오류 : 클래스엔 __dir__() 안됨 (이유가 뭐였지)
# ---------------------------------------------------------
# [ 클래스 구성 2 ]
# - 구성요소 : 속성 + 매서드 => 모두 없는 클래스
# - 기본 상속 : Object => __속성명__ 또는 __메서드명__
# ---------------------------------------------------------
class B:

    # 인스턴스 객체 생성 및 속성 초기화 메서드
    def __init__(self, num, name):
        # self로 지정된 힙 메모리 주소에서 부터 속성 저장
        self.num = num
        self.name = name

    # 인스턴스 매서드
    def print_info(self):
        print(f"num : {self.num}, name : {self.name}")

    # 연산자 매핑 매서드 구현
    def __add__(self, other):
        print('__add__')
        return self.num + other.num


# [ 객체 인스턴스 생성 ]
# => 생성 함수: 클래스이름()

b1 = B(100, 'BB!B')
b2 = B(200, 'BB!C')


# [ 속성과 매서드 확인하기 ]
# - __dict__ : 딕셔너리 형태로 클래스 내부 모든 속성과 메서드 확인 가능
# - __dir__() : 클래스 내부 모든 속성과 메서드 확인 가능

print("B 인스턴스 b1의 속성과 메서드 =>", b1.__dict__)
# {'num': 100, 'name': 'BB!B'}
print("B 인스턴스 b1의 속성과 메서드 =>", b1.__dir__())
# ['num', 'name', '__module__', '__init__', 'print_info', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
# => 인스턴스 변수까지 리스트로 출력

print("B 클래스의 속성과 메서드     =>", B.__dict__)
# {'__module__': '__main__', '__init__': <function B.__init__ at 0x0000026BCA41C820>, 'print_info': <function B.print_info at 0x0000026BCA41E430>, '__dict__': <attribute '__dict__' of 'B' objects>, '__weakref__': <attribute '__weakref__' of 'B' objects>, '__doc__': None}

# ---------------------------------------------------------
# [ 클래스 구성 3 ]
# - 구성요소 : 속성 + 매서드 => 모두 없는 클래스
# - 기본 상속 : Object => __속성명__ 또는 __메서드명__
# ---------------------------------------------------------
class C:
    # 클래스 변수 => C 클래스로 생성된 모든 인스턴스에서 공유
    #             => 인스턴스 생성 없이 사용 가능
    loc = 'Daegu'


    # 인스턴스 객체 생성 및 속성 초기화 메서드
    def __init__(self, num, name):
        # self로 지정된 힙 메모리 주소에서 부터 속성 저장
        self.num = num
        self.name = name

    #
    def print_info(self):
        print(f"num : {self.num}, name : {self.name}")

# [ 객체 인스턴스 생성 ]
# => 생성 함수: 클래스이름()

c1 = C(100, 'CC')

# [ 속성과 매서드 확인하기 ]
# - __dict__ : 딕셔너리 형태로 클래스 내부 모든 속성과 메서드 확인 가능
# - __dir__() : 클래스 내부 모든 속성과 메서드 확인 가능

print("B 인스턴스 b1의 속성과 메서드 =>", b1.__dict__)
# {'num': 100, 'name': 'BB!B'}
print("B 인스턴스 b1의 속성과 메서드 =>", b1.__dir__())
# ['num', 'name', '__module__', '__init__', 'print_info', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
# => 인스턴스 변수까지 리스트로 출력

print("B 클래스의 속성과 메서드     =>", B.__dict__)
# {'__module__': '__main__', '__init__': <function B.__init__ at 0x0000026BCA41C820>, 'print_info': <function B.print_info at 0x0000026BCA41E430>, '__dict__': <attribute '__dict__' of 'B' objects>, '__weakref__': <attribute '__weakref__' of 'B' objects>, '__doc__': None}

# 인스턴스 매서드 사용
c1.print_info()             # num : 100, name : CC

# 인스턴스 속성 사용
print(c1.name)              # CC

# 클래스 속성 사용
print("loc =>", C.loc)      # loc => Daegu

# 인스턴스 메서드는 클래스명으로 사용 불가!!
# C.print_info()
# Error : print_info() missing 1 required positional argument: 'self'
#         -> self를 선언하라는 말
# ---------------------------------------------------------------------

# [ 클래스 구성 4 ]
# - 구성요소 : 속성 + 매서드 => 모두 없는 클래스
# - 기본 상속 : Object => __속성명__ 또는 __메서드명__
# ---------------------------------------------------------
class DCalc:
    # 클래스 변수 => C 클래스로 생성된 모든 인스턴스에서 공유
    #             => 인스턴스 생성 없이 사용 가능
    name = 'CASIO'

    # 클래스 매서드 : 인스턴스 생성 없이 사용 (cls)
    @classmethod        # decorator (annotation)
    def addNum(cls, a, b):
        print(cls.name)     # cls; self 대신 사용된다
        print(DCalc.name)   # 클래스명으로도 호출 가능
        return a+b
    @classmethod
    def minusNum(cls, a, b):
        return a-b

    # cls가 의미한 것: class 매서드다!

    def print_info(self):
        print(f"num : {self.num}, name : {self.name}")



print(f'DCalc.name :', DCalc.name)
print(f'DCalc.addNum(10, 20):', DCalc.addNum(10, 20))
print(f'DCalc.minusNum(10, 20):', DCalc.minusNum(10, 20))



# ---------------------------------------------------------------------
# [ 오버로드를 확인하기 ]
# - 함수 오버로딩 : 함수명이 같아도 변수가 다르면 다르게 인식

# 일반 함수
def test(a, b):
    print(a, b)

def test(a, b, c):
    print(a, b, c)

# test(10, 20)
test(10, 20, 30)
# - 위 두 함수 동시 실행 시 오류 발생
# - 파이썬은 함수 오버로딩을 지원하지 않는다.
# - 마지막 동일한 함수명에 덮어씌움

# [ 객체 / 인스턴스의 연산 ]
print("ABC" + "123")
print([1,2,3]+[4,5,6])  # [1, 2, 3, 4, 5, 6]
# 이것도 가능할까?
print(b1 + b2)          # __add__
                        # +를 실행하면 __add__() 호출
                        # return 값 반환; b1:self, b2:other
# print(b1 - b2)        # __minus__ 는 없으므로 에러

# => 인스턴스끼리 연산하고 싶으면 매직함수를 다 넣어놔야한다.

# - 오버라이딩은 아니다
#   : 오버라이딩은
#   : 매개변수가 달라지므로 "오버로딩"


# ===============================================
# 상속
# - 다중 상속 허용 class A(B, C, D)
#       : => B, C, D 순으로 검색함
# -----------------------------------------------


class A:
    @classmethod
    def print_info(cls):
        print('A')


class B:
    @classmethod
    def print_info(cls):
        print('B')


class AB(A, B):     # A에서 먼저 탐색: A 출력
    pass


class AC(B, A):     # B 먼저 : B 출력
    pass


AB.print_info()     # A
AC.print_info()     # B
