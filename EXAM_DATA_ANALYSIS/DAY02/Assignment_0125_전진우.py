import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib
import pandas as pd

WORK = 2  # 과제 실행 변수: 1 or 2


def data_prepare(file, index_list):
    '''
    데이터 준비 함수; 두 과제가 공유
    :param file: data를 불러올 csv파일
    :param index_list:
    :return:
    '''
    data = pd.read_csv(file, encoding='utf-8-sig', header=[1])
    data_filtered = data.iloc[:, index_list].copy()  # 데이터 일부만 저장
    data_filtered['sum'] = data_filtered.iloc[:, 2] + data_filtered.iloc[:, 3]
    return data_filtered


# [과제1] : 각 노션별 최대하차인원 -------------------------
#   - 지하철 각 노션별 최대 하차 인원을 막대 그래프로 표시
#   - 하차 인원 출력
#   - 출근 시간대 : 07:00~08:59
# ----------------------------------------------------------
def get_off_calc(lane_list, data):
    """
    최고 인원 지하철 구하기
    :param lane_list: 1호선~7호선 목록
    :param data: 데이터: [0]호선명 [1]지하철역 [4]합계
    :return:
    """
    max_station_list = []
    max_num_list = []
    for line in lane_list:
        data_line_sorted = data[data['Unnamed: 1']==line].sort_values(by='sum')
        max_station = data_line_sorted.tail(1)['Unnamed: 3'].iloc[0]
        max_num = data_line_sorted.tail(1)['sum'].iloc[0]
        print(f'출근 시간대 {line} 최대 하차역: {max_station}역, 하차 인원: {max_num:,}명')
        max_station_list.append(f'{line} {max_station}'); max_num_list.append(max_num)

    plt.figure(figsize=(10,5))
    plt.bar(max_station_list, max_num_list)  # 그래프 그리기
    # 디자인
    plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하자역')
    plt.xticks(rotation=80)
    plt.show()


if WORK == 1:
    file = 'DATA/subwaytime.csv'
    index_list = [1, 3, 11, 13]
    data = data_prepare(file, index_list)
    lane_list = ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선']
    get_off_calc(lane_list, data)


# [과제2] : 퇴근 시간대 최대 하차 인원 ---------------------------
# 퇴근 시간대 : 19:00 ~ 20:59
# - 많이 내리는 순으로 지하철역 정렬
# - 5개의 지하철역 및 하차 인원수 출력
# - 호선은 다르지만 동일한 이름의 역은 모두 합하여 계산
# - 하차 인원은 1000 단위 쉼표 표기
# -----------------------------------------------------------------
# 호선이 겹치는 지하철역의 호선별 하차인원수 총합산
def highest_station_calc(data):
    # 각 역별로 합계 계산
    station_dict = {}
    print(data['Unnamed: 3'].unique)
    data.set_index('Unnamed: 3', inplace=True)
    for station in data.index.unique():
        print(station, data.loc[station]['sum'].max())
        highest_value = data.loc[station]['sum'].max()
        station_dict[station] = highest_value
    print(station_dict)


if WORK == 2:
    file = 'DATA/subwaytime.csv'
    index_list = [1, 3, 35, 37]
    data2_filtered = data_prepare(file, index_list)
    print(data2_filtered)
    highest_station_calc(data2_filtered)