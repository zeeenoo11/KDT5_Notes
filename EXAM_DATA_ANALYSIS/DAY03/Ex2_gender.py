import csv
import math

import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

# ---------- 1. gender.csv 헤더 ------------------
"""
f = open('DATA/gender.csv', encoding='utf-8-sig')
data = csv.reader(f)

header = next(data)
print(header)

for row in data:
    if '산격3동' in row[0]:
        print(row)
f.close()
"""
# ----------- 2. 연령별 성별 데이터 시각화 -----------------
# 인덱스: 남성 106~206, 여성 209~309
# 수평 막대 두 개
"""
def print_population(population):
    '''
    특정 지역의 인구 현황을 화면에 출력함
    :param population:
    :return:
    '''
    for i in range(len(population)):
        print(f'{i:3d}세: {population[i]:4d}명', end=' ')
        if (i+1) % 10 == 0:
            print()
    print()


def draw_gender_population(title, male_num_list, female_num_list):
    '''
    남녀 성별 인구 그래프 출력
    :param title:
    :param male_num_list:
    :param female_num_list:
    :return:
    '''
    plt.barh(range(len(male_num_list)), male_num_list, label='남성')
    plt.barh(range(len(female_num_list)), female_num_list, label='여성')
    plt.rcParams['axes.unicode_minus'] = False
    plt.title(title + ' 성별 인구 비율')
    plt.legend()
    plt.show()


def calculate_population():
    f =	open('DATA/gender.csv',	encoding='utf-8-sig')
    data = csv.reader(f)
    male_num_list = []
    female_num_list = []

    district = input('시군구 이름을 입력하세요: ')
    for row in data:
        if district in row[0]:
            for male in row[106:207]:
                if ',' in male:
                    male = male.replace(',','')
                male_num_list.append(int(male))
            for female in row[209:310]:
                if ',' in female:
                    female = female.replace(',','')
                female_num_list.append(int(female))
                # female_num_list.append(int(female)*(-1)) # 좌우대칭!
            break
    f.close()

    print(f'남성 총 인구수:{sum(male_num_list):,}	')
    print_population(male_num_list)
    print('-------------------------------')
    print(f'여성 총 인구수:{sum(female_num_list):,}	')
    print_population(female_num_list)
    draw_gender_population(district, male_num_list, female_num_list)

calculate_population()
"""
# -------- 3. 좌우대칭 만들기 --------------
# 아까 해봤지롱 근데 교수님은 남성 뒤집으심
# .append( -int(male) ) 도 가능하다 (이게 되네)
#   - code skip

# ------- 4. 특정 지역 성비 파이차트 -----------------
# 데이터 처음 보고 필요한 걸 찾는 게 중요하다
#   - 해당 파일에 합계를 제공함
"""
f = open('DATA/gender.csv',	encoding='utf-8-sig')
data = csv.reader(f)
population = []			# Pie chart에 넣을 데이터 (남, 여 인구수)
city = input('찾고 싶은 지역의 이름을 입력하세요:	')
male_count = 0
female_count = 0

for row in data:
    if city in row[0]:
        male_count = int(row[104].replace(',',''))
        female_count = int(row[207].replace(',',''))
        break

print(f'{city} 남자 인구수: {male_count:,} 명, 여자 인구수: {female_count:,} 명')

population = [male_count, female_count]
color = ['cornflowerblue', 'tomato']
plt.pie(population, labels=['남', '여'], autopct='%.1f%%', colors=color, startangle=90)
plt.title(city + '남녀 성별 비율')
plt.show()
"""
# ------ 5. 서울 포함 6개 광역시 연령대별 남녀 인구수 비교 -----
# 그래프 하나에 그리기
# 그래프 : 여러 지역의 인구 분포 -> 경향성 파악
#        - 남자가 더 빨리 죽는다...
# .savefig 사용 : 사진으로 저장
# csv 순으로 city_list를 설정해야한다
#   -
"""
f = open('DATA/gender.csv',	encoding='utf-8-sig')
data = csv.reader(f)
city_list =	['서울특별시',	'부산광역시','대구광역시',	'인천광역시',	'광주광역시',	'대전광역시'	]
for	city in city_list:
    male_list = []	#	리스트 데이터 초기화
    female_list = []	#	리스트 데이터 초기화
    for row in data:
        if city in row[0]:
            for i in range(106, 207):
                male_list.append(int(row[i].replace(',','')))
                female_list.append(int(row[i+103].replace(',','')))
            break

    color = ['cornflowerblue', 'tomato']
    plt.plot(male_list, label='남성', color=color[0])
    plt.plot(female_list, label='여성', color=color[1])
    plt.title(city + '남녀 인구수 비교')
    plt.xlabel('나이')
    plt.ylabel('인구수')
    plt.legend()
    plt.savefig('img/'+city+'.png', dpi=100)  # 'img/' = img 폴더에 저장
    plt.close()
"""
# ------------- 6. 산점도(scatter)로 표현하기 ------------------
# 1) [ plt.scatter() ]
#   - 회귀 기준선을 보고 나이대별 성별 치중도를 볼 수 있음
#   - 기준선 아래 : 남자가 많다 (<-> 위: 여자)
#   - 인구가 많을 수록 버블이 커짐 (우상향)
#   - 앞서 선그래프에서 차이를 비교하는 것과 동일
# 2) 산점도에 color bar 추가하기
#   - cmap : 컬러맵 속성
# 3) .scatter()
#   - c= : 구분 색상의 개수
#   - alpha= : 투명도
#   - cmap= : 색상표
#   - 버블 크기가 큼 : 교수님은 math.sqrt() 사용

def draw_scatter(city, male_list, female_list, bubble_size_list):

    plt.figure(figsize=(8,4), dpi=100)
    plt.scatter(male_list, female_list, s=bubble_size_list, c=range(101), alpha=0.5, cmap='jet')
    plt.colorbar()
    plt.plot(range(max(male_list)), range(max(male_list)), 'g--')

    plt.title(city + "	지역의 남녀 인구수 비교")
    plt.xlabel('남성 인구 수')
    plt.ylabel('여성 인구 수')
    plt.show()

def calculate_population():
    f = open('DATA/gender.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    male_list = []
    female_list = []
    bubble_size_list = []
    city = input('찾고 싶은 지역의 이름을 입력하세요: ')

    for row in data:
        if city in row[0]:
            for i in range(106, 207):
                male_num = int(row[i].replace(',',''))
                female_num = int(row[i+103].replace(',', ''))

                bubble_size_list.append(math.sqrt(male_num+female_num))

                male_list.append(male_num)
                female_list.append(female_num)
            break
    f.close()
    print(f'[여성 인구]: {female_list}')
    print(f'[남성 인구]: {male_list}')
    draw_scatter(city, male_list, female_list, bubble_size_list)

calculate_population()