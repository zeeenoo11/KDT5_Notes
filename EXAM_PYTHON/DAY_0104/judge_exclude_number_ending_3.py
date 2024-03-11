# 18장 -----------------------------------------------------
# 문제 : 1~200, 10~200인 정수1, 정수2 입력 (정수1 < 정수2)
#        두 정수 사이의 3으로 끝나지 않는 정수를 출력하는 프로그램
# ----------------------------------------------------------
start, stop = map(int,input().split())

i = start

    # for i in range(start, stop+1):
    #     print(i) if i%10 == 3 else None

while True:
    if i > stop: break       # stop보다 커지면 종료
    if i % 10 == 3:
        i +=1; continue      # 일의 자리가 3으로 끝나면 미출력
    print(i, end=' ')        # 3으로 끝나지 않는 수만 출력
    i += 1                   # i + 1