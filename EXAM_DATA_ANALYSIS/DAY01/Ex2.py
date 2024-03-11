import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import platform

# ----------- 5. Save Data into List -----------------
"""
f = open('DATA/daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f)

header = next(data)
result = []

for row in data:
    if row[4] != '':                  # max temp
        result.append(float(row[4]))  # .append()

print(len(result))
f.close()
plt.figure(figsize=(10,2))
plt.plot(result, 'r')  # color : red
plt.show()
"""
# ---------------- 6. .hist() : Make histogram --------------------------
# plt.hist( ) : 히스토그램 생성
# - bins :

# - 예시) 주사위 랜덤 생성하고 그 값을 히스토그램 그리기
"""
f = open('DATA/daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f)

header = next(data)
result = []

for row in data:
    if row[-1] != '':                  # max_temp
        result.append(float(row[-1]))  # .append()

print(len(result))
f.close()
plt.figure(figsize=(10,2))
plt.hist(result, bins=500, color='blue')
plt.rc('font', family='Malgun Gothic')

plt.rcParams['axes.unicode_minus'] = False  # 음수 기호가 깨지는 오류 해결
plt.title('1907년 부터 2023년까지 대구 기온 히스토그램')
plt.show()
"""
# ---------------- 7. str2 =  str.split() -------------------
# [ .split() ] : 문자열 분리
#   - 기본 공백 / 여기선 날짜 분리 위해 사용 .split('-')
"""
date_string1 = '2024   01   01'
#   공백을 기준으로 분리
print(date_string1.split())
#   구분자:'-'   기준으로 분리
date_string2 = '2023-12-31'
split_date_string = date_string2.split('-')
print(split_date_string)
year = split_date_string[0]
month = split_date_string[1]
day = split_date_string[2]
print(f'연도:{year}, 월:{month}, 일:{day}')
"""
# --------- 8. Temp Histogram of Specific Month -------------
# 8월 > 최고 기온 값 > 실수형으로 append
"""
f = open('DATA/daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)
aug = []

for row in data:
    month = row[0].split('-')[1]
    if row[-1] != '':
        if month =='08':
            aug.append(float(row[-1]))
f.close()
plt.hist(aug, bins=100, color='tomato')
plt.title('대구 8월의 최고 기온 히스토그램')
plt.xlabel('Temp')
plt.ylabel('Counts')
plt.show()
"""
# ---------------- 9. Histograms of Aug and Jan ----------------
"""
f = open('DATA/daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data:
    month = row[0].split('-')[1]
    if row[-1] != '':
        if month =='08':
            aug.append(float(row[-1]))
        if month =='01':
            jan.append(float(row[-1]))
f.close()
plt.hist(aug, bins=100, color='tomato', label='Aug')  # label : legend 
plt.hist(jan, bins=100, color='b', label='Jan')
plt.title('대구 8월의 최고 기온 히스토그램')
plt.xlabel('Temperature')
plt.rc('axes', unicode_minus=False)

plt.legend()
plt.show()
"""
# ---------- 10. Find max_temp of specific Day ----------------
'''
def draw_graph_on_date(month, day):
    f = open('DATA/daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)
    result = []
    for row in data:
        if row[-1] != '':
            date_string = row[0].split('-')
            if date_string[1] == month and date_string[2] ==day:
                result.append(float(row[-1]))
    f.close()
    plt.figure(figsize=(15,2))
    plt.plot(result, 'royalblue')
    plt.rc('axes', unicode_minus=False)  # - 문자 오류 방지
    plt.rc('font', family='Malgun Gothic')
    plt.title(f'매년 {month}월 {day}일 최고 기온 변화')
    plt.show()

month, date = input('Enter Month and Day: ').split()
draw_graph_on_date(month, date)
'''
# -------- 11. 2000년 이후 특정일의 최고,최저 기온 변화량 ----------

# next(data) 꼭 해줘야한다
# 비교문에선 형변환 필수 : int(date_string[0])
"""
def draw_lowhigh_graph(start_year, month, day):
    f = open('DATA/daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)
    high_temp = []
    low_temp = []
    x_year = []
    for row in data:
        if row[-1] != '':
            date_string = row[0].split('-')
            if int(date_string[0]) >= start_year:
                if int(date_string[1]) == month and int(date_string[2])==day:
                    high_temp.append(float(row[-1]))
                    low_temp.append(float(row[-2]))
                    x_year.append(date_string[0]) # 연도 저장;
    f.close()

    plt.figure(figsize=(20,4))
    plt.plot(x_year, high_temp, label='최고 기온')
    plt.plot(x_year, low_temp, label='최저 기온')

    plt.rcParams['axes.unicode_minus'] = False
    plt.title(f'{start_year}년 이후 {month}월 {day}일의 온도 변화 그래프', size=16)

    plt.legend(loc=2)
    plt.xlabel('year')
    plt.ylabel('temperature')
    plt.show()

draw_lowhigh_graph(2000, 12, 24)l
"""
