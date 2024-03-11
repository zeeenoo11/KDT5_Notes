# ---------------------------------------
# 자동차 관리 프로그램 만들기
# - 특성 : 엔진, 연료, 브랜드, 색상, 번호
# - 기능 : 전진, 후진, 좌우회전, 정지
# ---------------------------------------
# engine = 'V3'
# food = 'gasoline'
# maker = 'Hyendai'
# color = 'White'
# number = '111가 1234'
#
# engine1 = 'V3'
# food1 = 'gasoline'
# maker1 = 'Hyondai'
# color1 = 'Black'
# number1 = '111가 5678'
#
# def go(): print('전진')
# def back(): print('후진')
# def stop(): print('정지')
#
# carDict = {}
# # 자동차 관리하기 ------------------
# for k, v in carDict.items():
#     print('1st sold car :',number)
#     print('- engine :',engine)
#     print('- food :',food)
#     print('- maker :',maker)
#     print('- color :',color)





# ---------------------------------------
# 자동차 클래스
# - 역할 : 자동차 관련 데이터, 기능을 모두 저장 관리
# - 문법:
#       class 클래스명:
#       <---> 코드
# ---------------------------------------
class car:

    # 클래스 생성 시 필수로 사용되는 매서드
    # 힙 메모리에 속성들의 값을 저장해주는 역할
    # 정보
    def __init__(self, engine_, food_, color_, number_, maker_='Hyendai'):  # 힙에 변수 저장
        print('__init__')
        # 1. 매개변수 자리에 필요한 변수를 넣기
        # 2. 아래 self. 자리에 넣기
            # 끝에 _ 하는 이유 :
        # 자동차 클래스가 가지는 속성을 메모리 힙에 저장
        self.engine=engine_  # engine_에 들어온 값을 engine에 저장
        self.maker=maker_
        self.food=food_
        self.color=color_
        self.number=number_

    # 기능
    # 함수 형식
    def go(self):
        print(f'{self.number}, go')  # self.number로 해당 클래스의 정보 추출
    def back(self):
        print(f'{self.number}, back')
    def stop(self):
        print(f'{self.number}, stop')


# 클래스로 자동차 객체 생성
myCar1 = car('V3',  'gasoline','white','111가 1234')
myCar2 = car('V3', 'gasoline','black','111가 5678')
print(myCar1)
