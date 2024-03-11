import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import platform
import pandas as pd
import numpy as np

WORK = 1    # run work : 1 or 2
# ----------------  [ 과제1 ]  -------------------------
# 과거 10년 동안의 대구 날씨 데이터에서 1년 중 일교차가 가장 큰 달은 각각 몇 월인지 그래프로 표시

# 기간: 최근 10년 (2014년 ~ 2023년)
#   - 각 달의 일교차(최고기온 – 최저기온)를 비교하여 각 년도별 일교차가 가장 큰 달을 bar 그래프로 표시
#   - Pandas 또는 Python 코딩
# ------------------------------------------------------
def main():
    # 1-1. 데이터 준비 : 결측치 보정한 데이터 사용
    temp_data = pd.read_csv('DATA/daegu-utf-8-df.csv', encoding='utf-8-sig')
    # 1-2. 날짜 -> datetime
    temp_data['날짜'] = pd.to_datetime(temp_data['날짜'], format='%Y-%m-%d')
    # 1-3. 함수 호출
    draw_graph(temp_gap_calc(temp_data))


def temp_gap_calc(temp_data):  # 일교차 계산 함수
    # 2-2. 해당 연도만으로 구성된 데이터프레임 생성
    from_2023_df = temp_data[
        (2014 <= temp_data['날짜'].dt.year) & (temp_data['날짜'].dt.year <= 2023)
                            ].reset_index(drop=True)  # 2014~2023년만, 인덱스 제거
    # 2-3. 일교차 계산 후 데이터프레임에 입력 -> 안하는 게 낫나?
    temp_gap = []
    for i in range(len(from_2023_df.index)):
        temp_gap.append(round(from_2023_df['최고기온'][i] - from_2023_df['최저기온'][i], 1))
    from_2023_df.insert(5, '일교차', temp_gap)

    # 현길님팁ㅠㅠ : from_2023_df['일교차'] = from_2023_df['최고기온'] - from_2023_df['최저기온']

    # 2-4. 연도별 최고 일교차 계산하기
    temp_gap_max_list = []
    for yr in range(2014, 2024):
        each_yr = from_2023_df[from_2023_df["날짜"].dt.year == yr]
        tgmax= 0; month = 0     # 최대 일교차 비교 기준치
        for idx in each_yr.index:
            if each_yr['일교차'][idx] > tgmax:
                tgmax = each_yr.loc[idx, '일교차']
                month = each_yr['날짜'].dt.month[idx]
        temp_gap_max_list.append([yr, month, tgmax])
    print(temp_gap_max_list)
    return temp_gap_max_list


def draw_graph(temp_gap_max_list):  # 3. 그래프 제작 함수
    # 3-1. x, y축 선언
    barX = [f'{i[0]}.{i[1]}' for i in temp_gap_max_list]
    barY = [i[2] for i in temp_gap_max_list]

    # 3-2. 그래프 생성 함수
    plt.figure(figsize=(10,5))
    plt.bar(barX, barY)

    # 3-3. 디자인 : x,y축, 제목
    plt.title('지난 10년간 대구의 일교차가 가장 큰 달')
    plt.xlabel('Year/Month')
    plt.ylabel('Temp Gap')
    plt.show()  # 출력

if WORK == 1:
    main()  # main 함수 호출


"""
교수님 자료:
    - start_year, end~ 선언
    - for year -> for month in range(1,13)
    - str(year) +'.' + str(month)
    - max_month_index = ~~~['temp_gap'].idxmax()
    - max_month_df = pd.concat(원래 , max_month_index)
    - x_data (=axis) = .to_list()
"""
# ----------------  [ 과제2 ]  -------------------------
# 대구 기온 데이터에서 시작 연도, 마지막 연도를 입력하고 특정 월의 최고 기온 및 최저기온의 평균값을 구하고 그래프로 표현
# - 화면에서 측정할 달을 입력 받아서 진행
# -
#
# 입력 : 1) 시작연도 2) 마지막 연도 3) 측정 달
# 출력 : (해당월) 1) 최저기온 평균 2) 최고기온 평균
# ------------------------------------------------------
def main():
    # 1-1. 데이터 준비
    temp_data_2 = pd.read_csv('DATA/daegu-utf-8-df.csv', encoding='utf-8-sig')
    # 1-2. 날짜 형변환
    temp_data_2['날짜'] = pd.to_datetime(temp_data_2['날짜'], format='%Y-%m-%d')
    # 1-3. 함수 호출
    start, end, mth = year_in()
    y_in_list = [start, end, mth]
    draw_graph_2(y_in_list, year_out(temp_data_2, y_in_list))


def year_in():  # 2. 입력
    start_year = int(input('시작 연도를 입력하세요: '))
    end_year = int(input('마지막 연도를 입력하세요: '))
    month = int(input('기온 변화를 측정할 달을 입력하세요: '))
    return start_year, end_year, month


def year_out(data, y_in):  # 3. 출력
    # 3-1. data setting
    data_filtered = data[
        (y_in[0] <= data['날짜'].dt.year) & (data['날짜'].dt.year <= y_in[1])
        ].reset_index(drop=True)  # start ~ end year only
    
    # 3-2. 연도별 평균 계산
    # 희진쓰 따라 한 번에 for 돌리기
    min_mean_list = []
    max_mean_list = []
    for yr in range(y_in[0], y_in[1]+1):
        min_mean = data_filtered[data_filtered['날짜'].dt.year == yr]['최저기온'].mean()
        max_mean = data_filtered[data_filtered['날짜'].dt.year == yr]['최고기온'].mean()
        min_mean_list.append(round(min_mean,1))
        max_mean_list.append(round(max_mean,1))
    print(min_mean_list)
    print(max_mean_list)

    # 3-3. 출력
    print(f'{y_in[0]}년부터 {y_in[1]}년까지 {y_in[2]}월의 기온 변화')
    print(f'{y_in[2]}월 최저기온 평균:')
    for i in min_mean_list:
        print(i, end=' ')
    print(f'\n{y_in[2]}월 최고기온 평균:')
    for i in max_mean_list:
        print(i, end=' ')
    return min_mean_list, max_mean_list

def draw_graph_2(y_in, y_out):  # 4. 그래프 생성
    # 4-1. 그래프 준비
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10, 5))
    xlabels = [yr for yr in range(y_in[0], y_in[1]+1)]

    # 4-2. 그래프 생성 함수
    plt.plot(xlabels, y_out[0], 'bs-', xlabels, y_out[1], 'rs-')

    # 4-3. 디자인 : x,y축, 제목
    plt.title(f'{y_in[0]}년부터 {y_in[1]}년까지 {y_in[2]}월의 기온 변화')
    plt.legend()
    plt.show()  # 출력

if WORK == 2:
    main()

"""
수업과 같은 방식:
    - for year in -> yearDF = weatherDF[weatherDF['날짜'].dt.year == year ]
    -                monthDF = ~
    -                min_month_list[year-start_year] = round(month_df['최저기온'].mean(), 1)
    - 출력은 쉼표로 출력한다! 바꿔야함
"""

# min_mean_list = []
    # for yr in range(y_in[0], y_in[1]+1):
    #     min_mean = data_filtered[data_filtered['날짜'].dt.year == yr]['최저기온'].mean()
    #     min_mean_list.append(round(min_mean,1))
    # print(min_mean_list)
    # max_mean_list = []
    # for yr in range(y_in[0], y_in[1]+1):
    #     max_mean = data_filtered[data_filtered['날짜'].dt.year == yr]['최고기온'].mean()
    #     max_mean_list.append(round(max_mean,1))
    # print(max_mean_list)
    