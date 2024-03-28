import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib
import pandas as pd
WORK = 1

data = pd.read_csv('DATA/subwaytime.csv', encoding='utf-8-sig', header=[0,1])  #
data_filtered = data.iloc[:, [1, 3, 11, 13]].copy()  # 데이터 일부만 저장
data_filtered['sum'] = data_filtered.iloc[:, 2] + data_filtered.iloc[:, 3]
data_filtered.set_index('호선명', inplace=True)
print(data_filtered)

lane_list = ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선']
