import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

# ---------- 1. 시작: 데이터 확인하기 ----------------
# 대구 산격동 인구 현황
"""
f = open('DATA/age.csv', encoding='utf-8-sig')
data = csv.reader(f)

header = next(data)
print(header)

for row in data:
    if '산격3동' in row[0]:
        print(row)
f.close()
"""
# ----------- 2.
#
"""
f = open('DATA/age.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)

result = []
for row in data:
    if '산격3동' in row[0]:
        for data in row[3:]:
            result.append(result)
print(result)
f.close()
"""
# ------------ 3.
# 천 단위 콤마 제거
# 신암1동 출력 완료
"""
f = open('DATA/age.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
result = []
city = ''
for row in data:
    if '해운대구' in row[0]:
        city = row[0]
        for data in row[3:]:  # row[3:] : 0~100세
            if ',' in data:
                data = data.replace(',','')  # 쉼표 제거
            result.append(int(data))
print(result)
f.close()

plt.title(f'{city} 인구 현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()   # 엥 해운대구는 2000살까지 나옴
"""
# ---------- 4. 인구 구조 그래프 함수 구현 -------------------
#  - bar의 x는 표현할 모든 데이터 (range(101))
#  - xticks 는 그래프에 보일 데이터 (range(0, 101, 10))
#  --> 개수가 맞을 필요는 없다
"""""""""
def print_population(population):
    '''
    특정 지역의 인구 현황을 화면에 출력
    '''
    for i in range(len(population)):
        print(f'{i:3d}세: {population[i]:6d}명', end=' ')
        if (i+1) % 10 == 0:
            print()


def draw_population(district_name, population_list):
    '''
    특정 지역에 대한 인구 분포를 그래프로 나타냄(plot)
    :param district_name: 지역 이름
    :param population_list: 0~100세 인구 수 리스트
    :return: None
    '''

    plt.style.use('ggplot')  # 이건 뭐지
    plt.title('{0} 인구 현황'.format(district_name))
    plt.xlabel('나이')
    plt.ylabel('인구수')

    plt.bar(range(101), population_list)
    plt.xticks(range(0, 101, 10))  # 0세 ~	100세 이상

    plt.plot(population_list)
    plt.show()

def	get_population(city):
    f = open('DATA/age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)

    population_list = []
    district_name = ''
    for row in data:
        if city in row[0]:
            district_name = row[0]
            for data in row[3:]:
                if ',' in data:
                    data = data.replace(',','')
                population_list.append(int(data))
            break

    f.close()
    print_population(population_list)
    draw_population(district_name, population_list)

city = input('인구 구조를 알고 싶은 지역의 이름(읍면동 단위)을 입력하세요: ')
get_population(city)
"""""""""

# ------------ 5. 투표 가능 인구수 분석 ----------------
# 18세 이상: [21:]
# 고령화 비율을 볼 수 있음

# 파이차트 특징: x/(x+y) , y/(x+y)
#   - 각 부분은 총합 대비 비율을 나타낸다
#   - 예제: pie(population) 에 [투표 가능 , 투표 불가능] 을 전체를 기준으로 산정해 입력
"""
def draw_piechart(city_name, city_population, voting_population):
    '''
    전체 인구수 대비 투표 가능 인구의 파이 차트
    '''
    non_voting_population = city_population - voting_population
    population = [non_voting_population, voting_population]

    color = ['tomato', 'royalblue']
    plt.pie(population, labels=['18세 미만', '투표가능인구'],
            autopct='%.1f%%', colors=color, startangle=90)

    plt.legend(loc=1)
    plt.title(city_name + '투표 가능 인구 비율')
    plt.show()


def get_voting_population(city):
    '''
        투표가능 인구수 분석 row[21:]
    전체 인구수 : row[1]
    '''

    f = open('DATA/age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data)

    voting_number_list = []
    city_name = ''
    city_population = 0
    voting_population = 0
    for row in data:
        if city in row[0]:  # 도시 전체 인구수
            # 없으면 계속 지나간다
            city_population = row[1]
            if ',' in city_population:
                city_population = city_population.replace(',','')
            city_population = int(city_population)
            city_name = row[0]  # 서울특별시 오류 : 들여쓰기 덜 함
            for data in row[21:]:   # 18세 이상: for내에 있음
                if ',' in data:
                    data = data.replace(',','')
                voting_num = int(data)
                voting_number_list.append(voting_num)
                voting_population += voting_num
            break  # 처음 이름이 검색된 도시만 출력된다
    f.close()
    print(f'{city_name} 전체 인구수 : {city_population}명,'
          f'투표 가능 인구수 : {voting_population} 명')
    # 최종 함수 호출
    draw_piechart(city_name, city_population, voting_population)


city = input('투표 가능 인구수를 확인할 도시이름을 입력하시오: ')
get_voting_population(city)
"""
# ---------------- 6. 학령 인구 비율 --------------------
# 학령 인구는 초중고대 네 분류로 나뉜다
# 대학 18~21세...
"""
def draw_pie_chart(city, population_list, label_list):
    plt.pie(population_list, labels=label_list, autopct='%.1f%%', startangle=90)

    plt.legend(loc=1)
    plt.title(city + '학령인구 비율')
    plt.show()


def get_population(row, start, end):
    population = 0
    for num in row[start:end+1]:
        if ',' in num:
            num = num.replace(',', '')
        num = int(num)
        population += num
    return population


def school_age_popluation(city):
    city_population = 0
    non_school_pop = 0
    school_age_pop = 0
    label_list = ['초등학생', '중학생', '고등학생', '대학생', '비학령인구']
    population_list = []

    f = open('DATA/age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data)

    for row in data:
        if city in row[0]:
            city_population = row[1]
            if ',' in city_population:
                city_population = city_population.replace(',','')
            city_population = int(city_population)

            elementary_pop = get_population(row, 9, 14)
            population_list.append(elementary_pop)

            middleschool_pop = get_population(row, 15, 17)
            population_list.append(middleschool_pop)

            highschool_pop = get_population(row, 18, 20)
            population_list.append(highschool_pop)

            university_pop = get_population(row, 21, 24)
            population_list.append(university_pop)

            school_age_pop = (elementary_pop + middleschool_pop +
                              highschool_pop + university_pop)

            non_school_pop = city_population - school_age_pop
            population_list.append(non_school_pop)
            break

    print(f'전체인구수{city_population}'
          f'학령인구 비율:{round((school_age_pop*100)/city_population,	1)}%')
    draw_pie_chart(city,	population_list,	label_list)

# 실행문
city = input('학령인구를 분석할 도시 이름: ')
school_age_popluation(city)
"""
# -------------- 팁: if !func(): 하지마라 ------------------
# ret = function()
# if !
