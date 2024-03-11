import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ----------------------- 12.
weather_df = pd.read_csv('DATA/daegu-utf8.csv', encoding='utf-8-sig')
print(weather_df.columns)
print(weather_df['날짜'].dtype)  # 날짜 컬럼은 object

# column명 변경
weather_df.columns = ['날짜', '지점', '평균기온', '최저기온', '최고기온']
print(weather_df.columns)

# pd.to_datetime : '날짜':obj -> datetime 타입으로 변경
weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')
# %Y : 혼자 대문자!
print(weather_df['날짜'].dtype)

# ------------- 13. 누락 개수 구하기 -------------------

print(weather_df.head())
print(weather_df.shape)
num_rows = weather_df.shape[0]

# ------------- 14. 누락값 처리하기 --------------------
# [ dropna(axis) ] : 누락값 제거
#   - database에서의 용어를 그대로 사용
#   - drop : 삭제
#
# [ fillna() ]
#   - fillna(0) : 모두 0으로 채움
#   - fillna(method= 'ffill') :
#   - fillna(method= 'bfill') :
# interpolate() :
weather_df = weather_df.dropna(axis=0)
print(weather_df.count())
print(weather_df.head())

# ------- 15. 누락값 제거한 데이터를 파일로 저장 -------
weather_df.to_csv('DATA/daegu-utf-8-df.csv', index=False, mode='w', encoding='utf-8-sig')

# --------- 16. 특정 연도와 달의 최고, 최저 기온 평균값 계산 ---------
# 1. 해당 연도와 달의 DF 가져오기
year_df = weather_df[weather_df['날짜'].dt.year == 2023]  # year == 2023
month_df = year_df[year_df['날짜'].dt.month == 8]  # year_df 에서 month_df 추출
print(month_df.head())

# 2. 선별된 DF에서 연산하기
max_temp_mean = round(month_df['최고기온'].mean(), 1)
min_temp_mean = round(month_df['최저기온'].mean(), 1)
print('2023년 8월:','최저기온 평균:',min_temp_mean, ' 최고기온 평균:', max_temp_mean)


# ========================================================
# ---- 17. 1990년대와 2010년대 최고 기온 비교 ---------
# func. 1 : draw graph
def draw_two_plots(title, x_data, max_temp_list1, label_y1, max_temp_list2, label_y2):

    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10,4))
    plt.plot(x_data, max_temp_list1, label = label_y1)
    plt.plot(x_data, max_temp_list2, label = label_y2)

    # plt.ylim(10,40)
    plt.title(title)
    plt.legend()
    plt.show()

# func. 2 : main
# - pd.to_datetime( ) -> 이후 .dt.year 로 호출
def main():
    search_month = int(input('Enter Month: '))

    weather_df = pd.read_csv('DATA/daegu-utf-8-df.csv', encoding='utf-8-sig')
    weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')

    first_decade_max_temp_list = [0] * 10
    second_decade_max_temp_list = [0] * 10

    first_decade = 1990
    second_decade = 2010

    for year in range(10):
        first_decade_df = weather_df[(weather_df['날짜'].dt.year == first_decade + year) &
                                     (weather_df['날짜'].dt.month == search_month)]
        first_decade_max_temp_list[year] = round(first_decade_df['최고기온'].mean(), 1)

        second_decade_df = weather_df[(weather_df['날짜'].dt.year == second_decade + year) &
                                     (weather_df['날짜'].dt.month == search_month)]
        second_decade_max_temp_list[year] = round(second_decade_df['최고기온'].mean(), 1)

    print(f'{first_decade}, {search_month} mean max temp list : {first_decade_max_temp_list}')
    print(f'{second_decade}, {search_month} mean max temp lsit : {second_decade_max_temp_list}')

    first_decade_high_temp_mean = round(np.array(first_decade_max_temp_list).mean(), 1) # np.array 쓰면 가능
    second_decade_high_temp_mean = round(sum(second_decade_max_temp_list)/len(second_decade_max_temp_list), 1)

    print(f'{first_decade}, {search_month} mean max temp : {first_decade_high_temp_mean}')
    print(f'{second_decade}, {search_month} mean max temp : {second_decade_high_temp_mean}')

    x_data = [i for i in range(10)]
    draw_two_plots(f'{search_month} max temp compare', x_data,
                   first_decade_max_temp_list, str(first_decade),
                   second_decade_max_temp_list, str(second_decade))

main()