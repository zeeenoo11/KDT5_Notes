# -----------------------------------
# [예문] 자동차 클래스
# 클래스 이름 : Car
# 클래스 속성 : 바퀴, 색상, 차번호, 차종류, 제조사
#              12 inch, red, 1234, Kona, Hyendai
# 클래스 기능 : 주행, 정지
# -----------------------------------
# 현대차만 다루는 경우: 제조사는 모두 현대
# -> 제조사 : 클래스 속성
# -> 차종류 : 인스턴스 속성

class Car:
    # [ Class Attrib. ]
    maker = 'Hyendai'

    # [ 생성자 Method ]
    def __init__(self, wheel, color, number, kind):
        # [ hip 영역에 저장 ]
        self.wheel=wheel
        self.color=color
        self.number=number
        self.kind=kind
    
    # [ 인스턴스 Method ]
    def driving(self, where):
        print(f'no.{self.number} car moving toward {where}.')
        # self의 변수를 쓰려면 self.number

    def stop(self):
        print(f'no.{self.number} car is stopped.')

    def back(self):
        print(f'no.{self.number} car moves forward.')

# -----------------------------k
# 자동차 인스턴스 생성
# -----------------------------
myCar = Car(19, 'red', 1111, 'SUV')
secondCar = Car(20, 'Hotpink', 1212, 'K7')
print(myCar)


# ------------------------------------------------
# [예문2] 사랑 클래스
# 클래스 이름 : Love
# 클래스 속성 : Kind, giver, taker
#              
# 클래스 기능 : 챙겨주기, 함께하기, 안아주기, 희생하기
# ------------------------------------------------
class Love:

    def __init__(self, kind):
        self.kind = kind

    def takeCare(self):
        pass

    def takeTime(self):
        pass

    def hug(self):
        pass

    def sacrifice(self):
        pass

# ------------------------------------------------
# [예문3] 계산기 클래스
# 클래스 이름 : Calc
# 클래스 속성 : Kind, color, size, price
#              
# 클래스 기능 : add, extract, product, divide
# - 데이터는 속성 또는 기능에서 매개변수를 받는다
# ------------------------------------------------
class Calc:
    # para
    brand = "CASIO"
    __size = (70, 120)       #* 매개변수로 빼둬도 좋음

    # __init__
    def __init__(self, kind, color, price, info) -> None:
        self.color = color
        # self.__size = (70, 120)   # 비공개 속성: 클래스 밖에서 작업 불가
        self.kind = kind
        self.price = price
        self.data = 0        #* para로 안 받아도 변수 선언 가능하다
        self.__info = info   #* 생성 시에만 입력, 이후엔 불변

    # private instance method
    def getInfo(self):
        return self.__info   # 원랜 안보이지만, 이 함수를 통해 호출 가능

    def setInfo(self, info):
        self.__info = info

    # private :
    @property
    def info(self): return self.__info
    # - 표현은 연속적; 
    # - 위 info => 아래 info
    @info.setter
    def info(self, info): self.__info=info
        
    
    # Method
    def add(self, nums):
        self.data += nums

    def extract(self, nums):
        pass

    def product(self, nums):
        pass

    def divide(self, nums):
        if nums: self.data = self.data/nums
        else: return '0으로 나눌 수 없습니다'

    def data(self):  #* 결과 출력 : 누적이면 init -> self.result
        return self.data

# -----------------------------------------------------
# Calc Class로 인스턴스 생성 -> Hip
# -----------------------------------------------------
def main():
    cl = Calc('Engnieering', 'Black', 250, 'Yes')


# ------------- [ Public Attribute ] ------------------
# 인스턴스 속성 읽기 => 공개 속성만 읽기 가능
# print(cl.data, cl.color)

# 인스턴스 속성 변경
    cl.color = 'red'


# ------------- [ private Attribute ] -----------------
# 인스턴스 비공개 속성 읽기/쓰기 -> getter, setter
    print(cl.getInfo(), cl.info)        # Yes Yes
    # cl.info : 속성읽기; info라는 함수가 실행된 것

# 인스턴스 비공개 속성 변경
    cl.setInfo('Mine')          # 함수로 동작 혹은
    cl.info = "It's Mine"       # 메서드로 동작
    print(cl.getInfo(), cl.info)  # It's Mine , It's Mine

# ----------------------------------------------------
# clac class로 계산기 정보 확인 -> 클래스 변수만 확인 가능
#                                인스턴스  변수나 메서드 사용 불가
#                                self 값이 없음!
# ----------------------------------------------------
    print(Calc.brand)       # CASIO

# 인스턴스 메서드에 접근 불가
# Calc.add(10, 20)


# print(Calc.self.result)