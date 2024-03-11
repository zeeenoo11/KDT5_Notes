# ------------------------------------------
# 입력 받은 내용을 파일에 저장하는 프로그램
# - 조건 : 대문자 'X', 'x' 입력 시 입력 받기 중단
# - 내용 : 무관
# -------------------------------------------
from datetime import date, datetime
import time

file = 'test.txt'
with open(file, mode='a',encoding='utf-8') as f:
    while True:
        data = input("메시지 입력(종료:X or x): ")
        time.sleep(1)

        # 종료 검사
        if data in ('X','x'):
            print("종료합니다.",); break # while 탈출

        # 파일 쓰기 (저장) : with open은 밖에 있는 게 좋다.
        f.write(data+'\n')

    f.write('종료 시간 : '+time.ctime(time.time())+'\n')


today = date.today()
print(today.year, today.month, today.day)

today2 = datetime.today()
print(today2.year, today2.month, today2.day)

print(today.strftime("%y/%m/%d"))
