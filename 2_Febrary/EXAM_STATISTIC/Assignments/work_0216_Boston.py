import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib


# [ 과제2 ] -------------------------------------
# : 'Boston House Prices' 데이터셋 활용하기
# 1. 주택 가격의 평균
# 2. 주택 가격의 중앙값
# 3. 주택 가격의 표준 편차
# 4. 주택 가격의 최댓값
# 5. 주택 가격의 최소값
# 6. 주택 가격의 최빈값
# 7. 주택 가격의 분포를 시각화
# ----------------------------------------------------
# [ 컬럼명 및 설명 ]
# CRIM : per capita crime rate by town
# ZN : proportion of residential land zoned for lots over 25,000 sq.ft.
# INDUS : proportion of non-retail business acres per town
# CHAS : Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
# NOX : nitric oxides concentration (parts per 10 million)
# RM : average number of rooms per dwelling
# AGE : proportion of owner-occupied units built prior to 1940
# DIS : weighted distances to five Boston employment centres
# RAD : index of accessibility to radial highways
# TAX : full-value property-tax rate per $10,000
# PTRATIO : pupil-teacher ratio by town
# B : 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
# LSTAT : % lower status of the population
# MEDV : Median value of owner-occupied homes in $1000's
# ----------------------------------------------------
# 0. 데이터 준비
data = pd.read_csv('DATA/housing.csv', header=None)
# print(data[0])

columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
data_list = []
for row in data[0]:
    data_list.append(row.split())
# print(data_list)
data = pd.DataFrame(data_list, columns=columns)
# print(np.array(data.MEDV))

# - MEDV 값을 주택 가격으로 판단
price_array = np.array(data.MEDV).astype(float)


print('1. 주택 가격의 평균 : {:.1f}'.format(np.mean(price_array)))
print('2. 주택 가격의 중앙값 : {:.1f}'.format(np.median(price_array)))
print('3. 주택 가격의 표준 편차 : {:.1f}'.format(np.std(price_array)))
print('4. 주택 가격의 최댓값 : {:.1f}'.format(np.max(price_array)))
print('5. 주택 가격의 최소값 : {:.1f}'.format(np.min(price_array)))
price_mode = float(data.MEDV.mode().values[0])
print('6. 주택 가격의 최빈값 : {:.1f}'.format(price_mode))

print('\n7. 주택 가격의 분포를 시각화')
# .hist로 주택 가격 분포를 알 수 있음.
plt.figure(figsize=(5, 4))
freq, _, _ = plt.hist(price_array, bins=50, range=(np.min(price_array), np.max(price_array)))
# Design
plt.grid(axis='y', alpha=0.5)
plt.ylim(0, freq.max()*1.1)
plt.title('Boston 주택 가격의 분포', fontsize=15)
plt.xlabel('단위 : 1,000$')
plt.ylabel('개수')
plt.show()