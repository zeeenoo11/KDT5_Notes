# 20장 -------------------------------------
# 문제 : 정수 2개 입력, 첫 정수부터 마지막 정수까지
#        5의 배수면 Fizz, 7의 배수면 Buzz, 공배수면 FizzBuzz 출력
# -------------------------------------------
start, stop = map(int,input().split())

for i in range(start, stop+1):
    if not i%5 and not i%7: print('FizzBuzz') # 공배수
    elif not i%5: print('Fizz')               # 5만 나눠질때
    elif not i%7: print('Buzz')               # 7만 나눠질때
    else: print(i)