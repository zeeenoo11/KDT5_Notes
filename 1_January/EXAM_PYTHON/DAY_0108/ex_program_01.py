# ------------------------------------
# 나의 프로그램 : 계산기
# [계산기]
# 1. 입력
# 2~5. 사칙연산
# 6. 종료
# ------------------------------------
import functools


def dataCheck():
    data = input('계산할 숫자를 입력하세요: ')
    for word in data:
        if not word.isdecimal():
            print('숫자가 아닙니다.'); return dataCheck()
        else: return list(map(int, data.split()))

def Calculator():
    while True:
        print("""[Calculator]
        1. 입력
        2. 덧셈
        3. 뺼셈
        4. 곱셈
        5. 나눗셈(0 생략)
        6. 종료""")
        menu_input = input('입력 : ')
        if menu_input.isdecimal():
            while True:
                if int(menu_input) == 2:
                    dataCheck()
                    menu2 = '덧셈:' + str(functools.reduce(lambda a, b: a + b, dataCheck()))
                    print(menu2); break
                elif int(menu_input) == 3:
                    dataCheck()
                    menu2 = '뺼셈:' + str(functools.reduce(lambda a, b: a + b, dataCheck()))
                    print(menu2); break
                elif int(menu_input) == 4:
                    dataCheck()
                    menu2 = '덧셈:' + str(functools.reduce(lambda a, b: a + b, dataCheck()))
                    print(menu2); break
                elif int(menu_input) == 5:
                    dataCheck()
                    print('나눗셈:',functools.reduce(lambda a,b:a/b,dataCheck() if dataCheck()!=0 else None)); break
                elif int(menu_input) == 6:
                    pass
                elif int(menu_input) == 9: print('프로그램 종료'); break
                else: print('잘못된 입력입니다.')
        else: print('잘못된 메뉴입력입니다.')

# ============= 기록보기 & 탐색 & 기록 삭제 추가 ====================

calcHistory = []

def searchResult(search):
    for calc in calcHistory:
        if search in calc: print(calc)