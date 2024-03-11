# --------------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수가 정해지지 않은 경우에 적합
# ---------------------------------------------------
# [요청] 사용자로부터 좋아하는 음식명을 입력 받아 주세요.
#       => input(), '끝' 이라는 음식명 입력 시 종료
#       단, Top 5로 가장 좋아하는 음식 5개만
# ---------------------------------------------------
# food_list = []
# for i in range(5):
#     food_list.append(input())

# food_list = []
# while len(food_list) < 5:
#     food_list.append(input())
# print(f"Top5 Lists: 1. {food_list[0]} 2. {food_list[1]} 3. {food_list[2]} 4. {food_list[3]} 5. {food_list[4]}")

# str로 표현하기; if문 사용 보여주기 위함
EX_IF = False

if EX_IF:
    strfood = ""
    for cnt in range(1,6):
        food = input(f'Enter your no.{cnt} food: ')
        strfood = strfood + food + (', ' if cnt != 5 else '')
    print('Food lists: ', strfood)
    # 추후 활용엔 split 쓰면 됨

# -------------------------------------
# 기본 while 문법
# --------------------------------------
# Down counting Program
"""
downcount = 10
while downcount > 0:   # downcount가 0이 될 때까지
# or downcount >= 1
    print(downcount,'!',sep='')
    downcount -= 1

upcount = 1
while upcount <= 10:
    print(upcount,'!',sep='')
    upcount += 1
"""
"""
# for 문으로 써보기
for downcount in range(1,11):
    print(downcount,'!', sep='')
for upcount in range(10,0,-1):
    print(upcount,'!', sep='')
"""

# 구구단 : 알고 싶은 단 입력 받기, while 사용
"""
num_input = int(input("구구단 몇 단이 궁금하세요: "))
print(f'-- {num_input}단 --')
# for i in range(1,10):
#     print(f'{num_input} * {i} = {num_input*i}')
# 구구단은 for가 나은데...
count = 1
while count < 10:
    print(f'{num_input} * {count} = {num_input*count:2d}')
    count += 1
"""
# 모든 단 출력
dan, unit = 2, '단'
while dan < 10:
    # print(f'---{dan}단---')
    print(f'{dan:->4}{unit:-<4}')
    count = 1
    while count < 10:
        print(f'{dan} * {count} = {dan*count:2d}')
        count += 1
    print()
    dan += 1