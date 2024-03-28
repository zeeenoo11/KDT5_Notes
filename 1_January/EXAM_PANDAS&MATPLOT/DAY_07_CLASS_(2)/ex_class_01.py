# --------------------------------------------------------
# [ 사용자 정의 클래스 ]
# 
# - 클래스 정의 : 밤하늘의 별을 저장하는 데이터
# - 클래스 이름 : Star
# - 클래스 속성 : 크기, 색상, 밝기    => 속성(Attribute), 필드(Field) : 변수
# - 클래스 기능 : 반짝임, 생성과 소멸 => 함수(func), 메서드(Method) : 함수
# --------------------------------------------------------
class Star: 

    # ================== [ 변수/속성/필드 ] =====================
    # -> 해당 클래스로 생선된 객체, 즉 인스턴스가 공유하는 속성
    timezone = 'Night'   # 변경하지 않는 값은 변수로 따로 지정하자
    __privateValue = '비밀 인스턴스(객체) 변수'

    # ===================== [ 메서드 ] ==========================
    # 최상위 부모 클래스 object 로부터 상속 받은 함수, 메서드
        # 태어나보니 생겨있다!
    # 형태 : def __XXX__()
    # 나의 클래스에 맞도록 수정: 리모델링해 사용 -> Override
    
    # ------- override -------------
    def __init__(self, size, color, brightness, name ='Unknown'):
        print('__init__() :', size, color, brightness, name)
        # ------- 힙 메모리 영역에 저장 -------------
        # : 속성 데이터의 주소 저장
        self.name = name
        self.color = color
        self.brightness = brightness
        self.__size =size               # 비공개 변수, 변경 불가
        # .self = .myStar : 일단 myStar라는 객체에 접근해야 속성이 든 주소를 알 수 있음
        # 얘네들 다 속성

    # 별 클래스의 기능 (-> 메서드)
    def drop(self):
        print(self.name, '별이 떨어집니다.')  # 클래스 내 저장된 name을 가져옴


    # --------------- [ 비공개 메서드 ] --------------------
    # 비공개 인스턴스 속성에 접근하기 위한 메서드 -> getter/setter 메서드
    # 비공개 인스턴스 속성 읽어 오는 메서드 : get속성명() => 속성값 
    # 비공개 인스턴스 속성에 값 설정 하는 메서드 : set속성명(새로운값)


    def getSize(self):        # 비공개 속성 읽어오기
        return self.__size


    def setSize(self, size):  # 비공개 속성값 변경
        self.__size = size


    def __inner(self):        # 인스턴스 자체에 __ 사용; 클래스 내부에서만 사용
        print("나는 비공개 인스턴스 메서드")

    
    # --------- 비공개 메서드 접근법: @ --------------
    # Decorate  (ex. @property => 비공개 속성을 다룸)
        # decorate마다 정해진 의미가 있어 맞춰 쓰면 됨!

    @property              # -> getter 함수를 뜻함
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value
    @delattr
    def x(self):           # 위와 똑같이 생겨도 쓰임이 달라 상관 없음
        del self.__x


# --------- 클래스도 비공개 가능 -------------
    
# --------- self 없는 메서드 : @ 필수 ---------------
    # 인스턴스 생성 없이 사용하는 메서드 만들 때:
    @staticmethod       # 정적메서드
    def add():          # self가 붙지 않음!
        pass
    # 사용 :
    #  - 변수가 없을 때, 저장할 필요 없을 때 사용
    # 예 :
    #  - DF.size        # 변수 없이 함수 동작
    #  - <-> DF.mean() : 괄호 사용 여부가 다름름

    
    @classmethod        # 힙 영역 내 클래스 정보를 가져옴
    def cc(cls):
        pass



# --------------------------------------------------------
# 객체 생성 -> 클래스에 정의된 속성, 즉 변수와 함수들이 메모리 힙 영역에서 생성
# 생성 방법 -> 클래스명( ) 생성자 함수/매서드
#             클래스명(매개변수1) 생성자 함수/매서드
#             클래스명(매개변수1, 매개변수2, ... ) 생성자 함수/메서드
# --------------------------------------------------------
myStar = Star(5, 'dark_yellow', 10, 'Star1')
myStar2 = Star(2, 'yellow', 20, 'Star2')


# --- 객체의 메서드 실행 => 객체변수명.메서드명() ---------
myStar.drop()


# --- 객체의 속성 정보 읽기 -------------------------------
# 인스턴스 속성에 접근: 비공개는 안됨 (myStar.__size)
print(myStar.color, myStar.brightness)

# 
a = Star(5, 'dark', 10)
b = Star(10, 'yellow', 30, 'YellowStar')


# 특정 변수를 변경 불가하도록 하는 법 : self.__para = para


# 인스턴스 속성에 간접 접근 -> 메서드 제공함수 getter/setter
print('현재 비공개 속성값 읽기 :', myStar.getSize())   # 5
myStar.setSize(100)  # 현재 비공개 속성값 변경
print(
    '''현재 비공개 속성값 변경하기 : myStar.setSize(100)
현재 속성값 :''', myStar.getSize())   # 100

# -------------------------------------------------
# 객체의 속성 정보 변경 -> 객체변수.속성 = value (DF와 유사)
myStar2.brightness = 7
print(myStar.brightness)


# 속성 이름과 값 딕셔너리 출력
print('클래스명.__dict__:\n', Star.__dict__)
print('인스턴스명.__dict__:\n', myStar.__dict__)
# print('인스턴스명.__dict__:\n', yourStar.__dict__)

