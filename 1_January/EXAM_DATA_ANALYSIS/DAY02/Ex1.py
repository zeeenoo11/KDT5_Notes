import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

# ----------- 1. 데이터 읽어오기 -------------------------
"""
f = open('DATA/subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
print(header)
i = 1
for row in data:  # 한 줄씩 출력해보기
    print(row)
    if i > 5:
        break
    i += 1
f.close()
"""
# ----------- 2. 유임승차 비율 최고 역 찾기 ----------------
# row - [4] 유임승차 [6] 무임승차
# rate - 무임승차인원을 나누는 이유: 0명이 있는지 확인을 위함
# int로 형변환
# max_rate 선언해 최대값 찾기
"""
f = open('DATA/subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate = 0; rate = 0

for row in data:
    for i in range(4,8):
        row[i] = int(row[i])  # 자료를 int로 형변환
    rate = row[4] / row[6]
    if rate > max_rate:
        max_rate = rate
print(max_rate)
f.close()
"""
# => ZeroDivisionError: division by zero  # row[6]=0 존재

# ------------- 3. 무임승차=0 찾기 ---------------------------
# 실제 유임승차비율 = 유임승차 / (유임 + 무임)
# print() 잘 넣는 것도 능력이다
"""
f = open('DATA/subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate = 0; rate = 0

for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    rate = row[4] / (row[4] + row[6])
    # 유임 / (유임 + 무임)
    if row[6] == 0:  # 무임이 0인 역 출력
        print(row)
f.close()
"""
# ----------- 4.최대 무임 승차 비율 확인 ------------------
# 무임 승차 비율의 최대값
# 최대값의 기준값: 가장 작은 이상치
# if 내에 print( )를 넣으면서 비율 최대값의 변화를 볼 수 있음
"""
f = open('DATA/subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate = 0
for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    if row[6]:  # row[6] != 0
        rate = row[6] / (row[4] + row[6]) * 100
        if rate > max_rate:  # 최대 비율 찾기
            max_rate = rate
            print(row, round(rate, 2), '%')
f.close()
"""
# -------------- 5. 최대 유임 승차 인원 -------------------
# 앞선 내용 + 출력문
# f'{ :,}' : 천단위 쉼표
"""
f = open('DATA/subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate = 0; max_row = []; max_total_sum = 0 

for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    total_count = row[4] + row[6]
    if row[6] and (total_count > 100000):  # row[6] != 0
        rate = row[4] / total_count        
        if rate > max_rate:  # 최대 비율 찾기
            max_rate = rate
            max_row = row
            max_total_sum = total_count  # 각 max값 저장
            print(f'호선명: {max_row[1]}, 역이름: {max_row[3]}, 전체 인원: {max_total_sum:,}명,'
            f'유임승차인원: {max_row[4]:,}명, 유임승차 비율: {round(max_rate*100,2):,}%')

print()
print(f'호선명: {max_row[1]}, 역이름: {max_row[3]}, 전체 인원: {max_total_sum:,}명,'
      f'유임승차인원: {max_row[4]:,}명, 유임승차 비율: {round(max_rate*100,2):,}%')
f.close()
"""
# ------- 6. [실습] 유임 승차 비율이 가장 낮은 역 -------------------
# 총 승차 인원이 10,000명 이상인 역 중에서
# 유임 승차 비율이 50% 이하
# plt.pie 그리기 : .pie(values= , labels= , autopct= )
#   - 값= , 부분명= , 표현 양식= ('%,1f%% '=소수점 첫째 자리까지 계산)
#   - 유임 승차 비율이 가장 낮은 역을 그래프로 출력
"""
f = open('DATA/subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
min_rate = 100; min_row = []; min_total_sum = 0

for row in data:
    for i in [4,6]:
        row[i] = int(row[i])
    total_count = row[4] + row[6]
    if row[6] and (total_count > 10000):  # row[6] != 0, 10,000명 이상
        rate = row[4] / total_count
        if rate <= 0.5:  # 50% 이하 중 최소값
            print(row, round(rate, 2))
            if rate < min_rate:
                min_rate = rate
                min_row = row
                min_total_sum = total_count  # 각 max값 저장
f.close()

print()
print(f'호선명: {min_row[1]}, 역이름: {min_row[3]}, 전체 인원: {min_total_sum:,}명,'
      f'유임승차인원: {min_row[4]:,}명, 유임승차 비율: {round(min_rate*100,1):,}%')
# 파이 차트 출력
plt.title(min_row[3] + '역 유무임 승차 비율')
label = ['유임승차', '무임승차']
values = [min_row[4], min_row[6]]
plt.pie(values, labels=label, autopct='%.1f%%')
plt.legend(loc=2)  # loc : 
plt.show()
"""
# ---------- 7. 각 항목별 인원이 가장 많은 역 --------------------------
# 모든 역의 유무임, 승하차 각각을 비교
# with open() 구문
# - 뒤에 as f:  =>  f를 변수로 사용하기 위함
# - 한 번에 4개의 최대값을 비교: [0, 0, 0, 0] 에 수를 입력
# - idx[i-4] : 파일에서 네 항목이 4번부터 시작 -> list에 0부터 입력
"""
max = [0 for _ in range(4)]
max_station = ['' for _ in range(4)]
label = ['유임승차', '유임하차', '무임승차', '무임하차']
# with
with open('DATA/subwayfee.csv', encoding='utf-8-sig') as f: # as f
    data = csv.reader(f)  # 여기서 f 사용
    next(data)
    for row in data:
        for i in range(4, 8):
            row[i] = int(row[i])
            if row[i] > max[i-4]:  # 원본은 네번째, max는 첫 번째
                max[i-4] = row[i]
                max_station[i-4] = row[3] + ' ' + row[1]  # 역이름 + 호선

for i in range(4):
    print(f'{label[i]}: {max_station[i]} {max[i]:,}명')
"""

# -------------- 8. 지하철역 승하차 인원 분석 및 '저장' --------------------
# 파일 저장 방법 : savefig(filename, dpi)
#   - dpi : 파일 크기(안 써도 됨)
# .pie( row[4:8] , ... )
#   - 네 항목의 값을 비교 -> for로 모든 역에서 반복
# .savefig( 'img/'  + row[3] + ' ' + row[1] + '.png' )
#   - 동묘앞 1호선.png
#   - 'img/' :
"""
label = ['유임승차', '유임하차', '무임승차', '무임하차']
color_list = ['#ff9999', '#ffc000',	'#8fd9b6',	'#d395d0']
pic_count = 0   # 저장 개수 설정
with open('DATA/subwayfee.csv', encoding='utf-8-sig') as f: # as f
    data = csv.reader(f)  # 여기서 f 사용
    next(data)

    for row in data:
        for i in range(4, 8):
            row[i] = int(row[i]) # 형변환
        print(row)
        plt.figure(dpi=100)    # 저장 dpi를 여기서 설정
        plt.title(row[3] + ' ' + row[1])
        plt.pie(row[4:8], labels=label, colors=color_list, autopct= '%.1f%%', shadow=True)
        plt.savefig('img/' + row[3] + ' ' + row[1] + '.png')  # 동묘앞 1호선.png
        plt.close()   # .savefig 의 close()

        pic_count += 1
        if pic_count >= 10: break  # 10개만 저장
"""

