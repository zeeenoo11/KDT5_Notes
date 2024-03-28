# -------------------------------------------------
# 주의! 꼭 전역 변수가 아니더라도 iterables의 경우
# 함수의 매개변수로 전달 후 원소값 변경 시 모두 적용됨
# => 해결법 : 깊은 복사 deepcopy로 복사본 전달 필요
# -------------------------------------------------
def one(number):
    # number : local var.
    print(number)

def datas(nums, value):
    # num : 리스트
    # value : 정수
    nums[-1] = 1004
    print(nums, value, sep=' - ')

# 전역 변수 선언
value = 'Good'
datasList = [11, 22, 33]
num = 7

# 함수 호출
print(f'value : {value}, dataList : {datasList}, num : {num}') # value : Good, dataList : [11, 22, 33], num : 7

one(num) # 7
datas(datasList, value) # [11, 22, 1004] - Good

print(f'value : {value}, dataList : {datasList}, num : {num}') # value : Good, dataList : [11, 22, 1004], num : 7

# [정리] 함수 내에서 리스트를 변경하면 전역 리스트는 그대로, 내부 원소는 변경