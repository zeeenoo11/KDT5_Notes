# -------------------------------------------------------
# 전역변수(Global Variable)와 지역변수(Local Variable)
# - 함수 내에서 전역 변수 값을 변경하고자 할 땐 추가 코드 필요
# - global 전역 변수명
# -> 주의 : 전역 변수의 값이 함수가 변경; 프로그램 전체에 영향
# --------------------------------------------------------
def currentDate2_2(month, day):
    # year = year + 10     # year의 데이터 변경 시도 시: 오류 발생
    global year            # global : 함수 내 전역 변수 변경에 사용
    year = year + 10
    print(f"Today : {year}/{month:0>2}/{day:0>2}")

# 전역 변수
year, month, day = 2024, 1, 8

# 함수 호출
currentDate2_2(month, day)

# 변수 값 확인 출력
print(f'year : {year}, month : {month}, day : {day}')

# 전역 변수 year 값이 변함!