import pandas as pd
import csv

# [ 과제1 ] ------------------------------------------
# : 서울시 지하철 역별 이용객수
# 1. 역별 평균 이용객 수
# 2. 역별 이용객 수의 표준편차
# 3. 가장 많은 이용객이 있는 역의 이용객 수
# 4. 가장 적은 이용객이 있는 역의 이용객 수
# 5. 가장 많은 이용객이 있는 역의 이름
# 6. 가장 적은 이용객이 있는 역의 이름
# 7. 이용객 수의 분포를 히스토그램으로 시각화
# ---------------------------------------------------

# 0. 파일 준비
pd.set_option('display.max_columns', None)  # 인덱스 전체 출력
pd.set_option('display.precision', 0)  # 인덱스 전체 출력
file = pd.read_csv('DATA/서울교통공사_역별 일별 시간대별 승하차인원 정보.csv', encoding='utf-8')

# 0-1. 자료 확인
# print(file.dtypes)  # int 자료형 확인
# print(file.sort_values(['수송일자','역명']))  # 일자별 호선별 2행씩 존재

# 0-2. 전처리: 합계 구하기
file['합계'] = file.iloc[:, 6:].sum(axis=1)    # 합산 후 새 컬럼에 추가
file_refine_1 = file.loc[:, ['수송일자', '역명', '합계']]
file_refine_final = file_refine_1.groupby(['수송일자', '역명'], as_index=False).sum()
print(file_refine_final[file_refine_final['역명'] == '신내'])

# 1. 평균 이용객 수 : 하루 이용객 기준으로 전체 기간의 평균 산정
#   - 기간 : 2023/01/01 ~ 2023/09/30
station_mean = file_refine_final.groupby('역명')['합계'].mean()
print('역별 평균 이용객수 : \n', station_mean.sort_values(ascending=False))
print('-'*50)

# # 2. 역별 이용객 수의 표준편차
station_std = file_refine_final.groupby('역명')['합계'].std().dropna()
print('역별 표준편차 : \n', station_std.sort_values(ascending=False))
print('-'*50)
