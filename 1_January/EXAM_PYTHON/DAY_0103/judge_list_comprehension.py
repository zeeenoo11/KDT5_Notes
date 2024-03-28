# 22장 ------------------------------------------
# 문제: 정수 두 개 입력 (num1: 1~20, num2: 10~30) (num1<num2)
# num1 ~ num2 를 지수로 하는 2의 배수 리스트 생성
# 리스트 두 번째 요소와 뒤에서 두 번째 요소는 삭제
# -----------------------------------------------

# 1. 정수 입력
num1, num2 = input().split()       # 공백 구분 입력
num1, num2 = int(num1), int(num2)  # 정수 변환

# 2. 리스트 생성
power_list = [2 ** a for a in range(num1,num2+1)]                    # 리스트 생성
# while num1 <= num2:                # num1 == num2 까지 반복
#     power_list.append(2**num1)     # 리스트에 입력
#     num1 += 1                      # num1 + 1
# for i in range(num1,num2+1):
#     power_list.append(2 ** num1)  # 리스트에 입력

# 3. 요소 제거
power_list.pop(1); power_list.pop(-2)  # 앞뒤 2번째 제거
print(power_list)                  # 최종 출력
