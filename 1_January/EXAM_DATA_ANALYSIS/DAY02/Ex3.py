import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib
import pandas as pd

# ------------ 13. [ Pandas ] --------------
#
#w 데이터 준비
df = pd.read_excel('DATA/subway.xls', sheet_name='지하철 시간대별 이용현황', header=[0,1])
print(df.head())  # 0~4 인덱스
print(df.columns) # 열들만 세로로

# 특정 컬럼 데이터 가져오기
print(df['호선명', 'Unnamed: 1_level_1' ]) # 멀티인덱스라 두 개
print()
# iloc로 접근
commute_time_df = df.iloc[:, [1,3,10,12,14]] # : 이면 전체라는 뜻
print(commute_time_df.head())   # only 5 columns

# 데이터 타입 확인
print(commute_time_df.dtypes) # 모두 object

# 데이터의 쉼표 없애기
# copy 오류 : .copy 를 선언해 모두 적용하면 사라짐
commute_time_df = commute_time_df.copy() # 한 방에 오류 삭제
commute_time_df[('07:00:00~07:59:59', '승차')] = commute_time_df[('07:00:00~07:59:59', '승차')].apply(lambda x: x.replace(',',''))
commute_time_df[('08:00:00~08:59:59', '승차')] = commute_time_df[('08:00:00~08:59:59', '승차')].apply(lambda x: x.replace(',',''))
commute_time_df[('09:00:00~09:59:59', '승차')] = commute_time_df[('09:00:00~09:59:59', '승차')].apply(lambda x: x.replace(',',''))
print(commute_time_df.head())

# 데이터 타입 변경 : 키:값 형태..? ------------------
commute_time_df = commute_time_df.astype({('07:00:00~07:59:59', '승차') : 'int64'})
commute_time_df = commute_time_df.astype({('08:00:00~08:59:59', '승차') : 'int64'})
commute_time_df = commute_time_df.astype({('09:00:00~09:59:59', '승차') : 'int64'})
print(commute_time_df.dtypes) # 변경 완료

# 각 행 승차 인원 수의 합 계산
row_sum_df = commute_time_df.sum(axis=1, numeric_only=True)
passenger_number_list = row_sum_df.to_list()
print(row_sum_df)

# 최대값
max_number = row_sum_df.max(axis=0)
print(max_number)

# [ .idxmax() ] : 최대값 인덱스
max_index = row_sum_df.idxmax()
max_line, max_station = df.iloc[max_index, [1,3]]
print('출근 시간대 최대 승차 인원역: {0} {1} {2:,}명'
      .format(max_line, max_station, max_number))

# --------- bar-chart 그리기 --------------
