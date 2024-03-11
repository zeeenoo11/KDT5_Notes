# ----------------------------------------------
# 2 dimensions dot class
# name : Point2D
# Attr. : x, y, color, shape, size
# func. : draw, erase, show
# ----------------------------------------------
class Point2D:
    # No class Attr.

    # instance initialize
    def __init__(self, x, y, color, shape, size):
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.size = size
    
    # istance Method
    def draw(self):
        print(f'{self.shape} on [{self.x}, {self.y}]')

    def printInfo(self):
        print(f'location : ({self.x}, {self.y})')
        print(f'color : {self.color}')
        print(f'shape : {self.shape}')
# =================================================


# [ How to COPY Class ] : 상속 inheritance
# - Point2D : super class -> Point3D : sub class
# ----------------------------------------------
# 3 dimensions dot class
# name : Point3D
# Attr. : x, y, z, color, shape, size
# func. : draw, erase, show
# ----------------------------------------------
class Point3D(Point2D):         # *
    # class Attr. -> None

    # instance init
    def __init__(self, x, y, z, color, shape, size):
        # 부모 객체 생성: super().__init__()
        super().__init__(x, y, color, shape, size)  #* Point2D init을 실행
        self.z = z          #* 없는 변수만 따로 저장
        print('Point3D')

    # [ Overriding ] : 부모의 메서드를 가져와 새로 만드는 것
    def printInfo(self):  #* 이걸 또 만드는 이유 : 원하는 결과와 달라서
        print('3D')
        print(f'location : ({self.x}, {self.y}, {self.z})')
        print(f'color : {self.color}')
        print(f'shape : {self.shape}')
    

p2 = Point2D(10, 10, 'red', 'circle', (10, 10))
print(p2.color)

p3 = Point3D(5, 5, 5, 'yellow', 'rectangle', (3,3,3))
print(p3.color)
# -> def color 없이도 super class에서 가져옴
# ====================================================


# [ Multiple Inheritance ] : Not Recommended
# -------------------------------------------------------
import ex_class_02 as e2

class Point3D(Point2D, e2.Car):         # **
    # class Attr. -> None

    # instance init
    def __init__(self, x, y, z, color, shape, size):
        print('Point3D')
        self.z = z          # 없는 변수만 따로 저장

p3.maker    # 다중상속: Car의 메서드도 사용 가능해진다
# =======================================================

# Fin.