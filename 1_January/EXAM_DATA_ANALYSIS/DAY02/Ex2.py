import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

# ------ 8. 시간대별 지하철 이용 인원 수 (map(int, data)) ---------------
# 승하차 인원을 기록
#   - 헤더가 두 줄 : next() 두 번 (겹칠 수 있나?)
#   - 열이 완전 길다 : [4:]

# [ map( func, iterables ) ] : map(int, data)
#   - 리스트 요소를 각각 함수로 처리
#   - map 객체를 리턴
"""""""""
result = []
total_number = 0
with open('DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    for row in data:
        row[4:] = map(int, row[4:])
        total_number += row[4]
        result.append(row[4])
print(f'총 지하철 역의 수: {len(result)}')
print(f'새벽 네시 승차인원: {total_number:,}')
"""""""""
# ---------- 9. 새벽 4시 지하철 승차 인원 수 / 최대 승차역 -----------------
#
"""
with open('DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)          # next 두 번; 중복 사용은 안된다
    result = []
    total_number = 0; max_num = -1; max_station = ''
    for row in data: #
        row[4:] = map(int, row[4:])  #형변환
        total_number += row[4]       # [4] -> 4시 승차
        result.append(row[4])
        if row[4] > max_num:         # 최대 승차역 구하기
            max_num = row[4]
            max_station = row[3]
print(f'새벽 네 시 승차인원 수: {total_number:,}')
print('최대 승차역 : {0}, 인원수: {1:,}'.format(max_station, max_num))
result.sort()  # 오름차순 정렬
# 그래프
plt.figure(dpi=100)
plt.bar(range(len(result),), result)   # x축 간단히 적기: range(len(y_data))
plt.title('새벽 4시 지하철 승차인원 현황')
plt.show()
"""
# -------------- 10. 출근 시간대 지하철 이용 현황 ------------------------
# 출퇴근 시간대가 제일 핫하지요
# 1) header를 for로 돌려서 모든 열을 인덱스와 함께 보기
# 2) 열이 길면 세기 어렵다,, .transpose도 나쁘지 않을지도?
# 3) row[10:15:2] vs (row[10] + row[12] + row[14])
#   - 둘 다 장단점이 있다, 오른쪽이 직관적
#   - 깔끔하고 자신에게 맞는 방법 찾기

# sorted() vs .sort(), 누가 inplace일까
# - sorted( ) : 원본 변경 X, 새로 반환 (False)
# - .sort( ) : 원본 변경               (True)

# subplot() => sharey : y축 라벨 공유
#   - 대신 앞선 plt.subplot() 에 변수 선언 -> 입력
#   - ax1 =

# suptitle(' '): super - 부모 타이틀
"""
with open('DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)          # next 두 번; 중복 사용은 안된다
    result = []
    total_number = 0; max_num = -1; max_station = ''
    for row in data: #
        row[4:] = map(int, row[4:])  #형변환
        row_sum = sum(row[10:15:2])
        result.append(row_sum)
        if row_sum > max_num:
            max_num = row_sum
            max_station = row[3] + '(' + row[1] + ')'

print(f'최대 승차 인원역: {max_station} {max_num:,}')
result.sort(reverse=True)
# graph
plt.figure(figsize=(10,4))
ax1 = plt.subplot(1,2,1)
plt.title('10개의 역의 승차 인원수', size=12)
plt.bar(range(10), result[0:10])
plt.ylabel('승차인원수')

ax2 = plt.subplot(1,2,2, sharey=ax1)
plt.title('전체 역의 승차 인원수', size=12)
plt.bar(range(len(result)), result)

plt.suptitle('출근 시간대 승차 인원 현황\n', size=20)
plt.tight_layout()
plt.show()
"""
# ----- 팁) 그래서 결론이 뭔데? -------
#  발표 시 결과를 도출해야 한다 엉엉
# -------------------------------------

# ------------- 11. 시간대별 가장 많이 승차하는 역 정보 분석 ------------
# 24시간제 표현하기: 오전4시 ~ 오전2시
#   - range(4, 27)
#   - i % 24  -> 24면 0시, 25 - 1시, 26 - 2시
# for row in data: 라인이 핵심
"""
with open('DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)          # next 두 번; 중복 사용은 안된다
    max = [0 for _ in range(23)]
    max_station = [' ' for _ in range(23)]
    xtick_list = []

    for i in range(4, 27):
        n = i % 24      # 24시간 단위, 넘으면 0~2시
        xtick_list.append(str(n))  # x축 표현

    for row in data:     # 중요 단락
        row[4:] = map(int, row[4:])  # 형변환
        for j in range(23):          # 2시 : 48열
            a = row[j*2 + 4]         # 시간 열은 4번부터 두 칸씩
            if a > max[j]:
                max[j] = a
                max_station[j] = xtick_list[j] + '시:' + row[3]

    for i in range(len(max)):
        print(f'[{max_station[i]}: {max[i]:,}')

# graph
plt.figure(figsize=(10,10))
plt.title('시간대별 최대 승차역 정보')
plt.bar(range(23), max)
plt.xticks(range(23), labels=max_station, rotation=80)
plt.tight_layout()
plt.show()
"""
# -------- 12. 모든 지하철역에서 시간대별 승하차 인원 (고양이) ------------
# 천 만명 단위,, 1e+7
"""
with open('DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    subway_in = [0 for _ in range(24)]
    subway_out = [0 for _ in range(24)]

    for row in data: #
        row[4:] = map(int, row[4:])
        for i in range(24):                 #
            subway_in[i] += row[4+i*2]      #
            subway_out[i] += row[5+i*2]

    xticks_list = []
    for i in range(4, 28):
        n = i % 24
        xticks_list.append(str(n))

plt.figure(dpi=100)
plt.title('지하철 시간대별 승하차 인원 추이', size=16)
plt.grid(linestyle=':')
plt.plot(subway_in, label='승차')
plt.plot(subway_out, label='하차')
plt.legend()

plt.xticks(range(24), labels=xticks_list)
plt.xlabel('시간')
plt.ylabel('인원 (천만명)')
plt.show()
"""
# ---- (어려움) [정렬하기] lambda vs operator -------------------------
# 조건 : dict -> key, value and ascending, descending
# [lambda] :
#   - sorted(names.items(), key=(lambda x:x[0]))
#                  (키, 값) -> (키,값)[0] = '키'  : items() 중 0번
#   - sorted(names.items(), key=(lambda x:x[1]))
#                  (키, 값) -> (키,값)[1] = '값'  : items() 중 1번
#   => .items를 key 기준으로 정렬
#               = key or value
#   => key에 x? : sorted()의 key= 는 iterable의 값을 받는 함수로 작용되도록 설계!

# Tip) x:-x[0] 하면 내림차순 정렬

# [Operator] :
#   - sorted(names.items(), key=operator.itemgetter(0))
#                                       0번 인덱스를 뽑는다

# ---------------- [ lambda ] : 람다 함수 ----------------------
# lambda x, y: x + y / 이젠 아마 잘할걸?

# ------------------ [key=] 매개변수 ----------------------------
# 1. key = func. : 무조건 함수!
#                  iterables를 변수로 정렬 기준을 선정
# 2. 기본= None
# 3. 예시 : 1) key= len  2) key=str.lower  3) lambda x:x[0]
#           3번(람다)을 제일 많이 쓴다
# class 예제 (구경)
