# --------------------------------------------
# 함수 안의 함수를 호출
# --------------------------------------------
hello = 'Hey'
def print_Hello():
    hello = "hello~!"

    def print_message():
        msg = hello + "!!" # 여기서 hello는 젤 가까운 곳에서 찾는다
        print(msg)

    print_message()      # print 출력
print_Hello()            # 더 멀리 있는 hello는 반영X

def ff():
    x = 100  # nonlocal이 닿지 않음
    def a():
        x = 10 # 함수 a()의 지역 변수; nonlocal로 인해 변경됨

        def b():
            nonlocal x  # 가장 가까운 바깥 함수에서 x 찾음
            x = 20      # 함수 b()의 지역 변수
        b()
        print('1.', x) # 1. 20  => nonlocal 이 a()의 x를 바꿈
    a()
    print('2.', x)     # 2. 100 => ff()의 x를 바꾸지 않음

ff() # 최상위 함수 실행

# ------------------------------------------------------------------
# 클로저 : 함수가 함수를 리턴; 바깥 함수의 변수는 리턴된 함수에 입력
#
# ------------------------------------------------------------------
def calc():
    a, b = 3, 5  # 전역 변수 줄이는 법!
    def mul_add(x): # 함수 내 함수 선언
        return a * x + b
    return mul_add  # 젤 중요한 포인트; 함수를 리턴한다

c = calc()  # 함수를 변수에 저장; calc(1)로 생각하면
print(c(1),c(2),c(3),c(4),c(5))  # calc()에 입력된 값은 mul_add()에 들어감