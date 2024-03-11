# -------------------------------------------------------
# 전역변수(Global Variable)와 지역변수(Local Variable)
# - 함수 내에서 전역 변수 값을 변경하고자 할 땐 추가 코드 필요
# - global 전역 변수명
# -> 주의 : 전역 변수의 값이 함수가 변경; 프로그램 전체에 영향
# --------------------------------------------------------
def currentDate_List(todays):
    # to
    todays[0] = todays[0] + 100
    x = 0
    print(f"Today : {todays[0]}/{todays[1]:0>2}/{todays[2]:0>2}")
    print(locals())

# 전역 변수
year, month, day = 2024, 1, 8
todayList = [year, month, day]

# 함수 호출
currentDate_List(todayList)

# 변수 값 확인 출력
print(f'year : {year}, month : {month}, day : {day}')

print(locals())

