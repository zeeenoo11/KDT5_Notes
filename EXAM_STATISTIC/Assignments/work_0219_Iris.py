import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# <과제2 Iris >
# 1. 공분산 구하기
# 2. 상관계수 계산하기
# 3. 특성별 히스토그램 그리기
# 4. 품종별 특성(네 가지)에 대한 상자그림 그리기
# 5. 품종별 꽃받침 길이와 너비의 관계를 산점도로 표현,
#    색상으로 품종을 구분하기
# ------------------------------------------------
# 0. Data Prepare
file = pd.read_csv('DATA/iris.csv', header=0, encoding='utf-8')
# print(file)

# 1. 공분산 구하기
cols = file.columns
print('[ 1. Find Covariances ]')
for i in range(len(file.columns)-1):
    for j in file.columns[i+1:-1]:
        cov_mat = np.cov(file.iloc[:, i], file.loc[:, j])
        print(f'{cols[i]}  <->  {j}:')
        print(cov_mat, '\n')
print('-'*50)

# 2. 상관계수 계산하기
print('[ 2. Find Correlations ]')
file_values = file.iloc[:, :-1]
corr_mat = pd.DataFrame(file_values)
# print(corr_mat)
print(corr_mat.corr())
print('-'*50)

# 3. 특성별 히스토그램 그리기
print('[ 3. Make Histogram ]')
try:
    plt.figure(figsize=(8,8))
    file_values.hist(bins=30)
    plt.show()
    print('Draw Successfully.')
except:
    print('Draw Failed.')
print('-'*50)

# 4. 품종별 특성(네 가지)에 대한 상자그림 그리기
# 4-1. 품종 구분
setosa_values = file[file['species'] == 'setosa'].iloc[:, :-1]
versicolor_values = file[file['species'] == 'versicolor'].iloc[:, :-1]
# print(setosa_values, versicolor_values)
# 4-2. 상자그림 그리기
print('[ 4. Make Boxplot ]')
try:
    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    plt.title('Boxplots of Iris: Setosa')
    plt.boxplot(setosa_values, vert=False)
    plt.yticks(range(1, 5), file_values.columns)
    plt.xlabel('Values')

    plt.subplot(1,2,2)
    plt.title('Boxplots of Iris: Versicolor')
    plt.boxplot(versicolor_values, vert=False)
    plt.yticks(range(1, 5), file_values.columns)
    plt.xlabel('Values')

    plt.tight_layout()
    plt.show()
    print('Draw Successfully.')

except:
    print('Draw Failed.')

# 5. 산점도 그리기
print('[ 5. Make Scatterplot ]')


def make_polyfit(values):
    x_values = np.array(values.iloc[:, 0])
    y_values = np.array(values.iloc[:, 1])
    # 1. .polyfit : B0, B1 (계수) 구하기
    poly_fit = np.polyfit(x_values, y_values, 1)
    # 2. .poly1d : 회귀직선 반환 함수
    poly_1d = np.poly1d(poly_fit)
    # 3. .linspace : 직선의 x좌표
    xs = np.linspace(x_values.min(), x_values.max())
    # 4. y좌표
    ys = poly_1d(xs)
    return xs, ys, poly_fit


try:
    # 품종별 sepal_length, sepal_width 산점도 그리기
    plt.figure(figsize=(6,6))
    plt.title('Scatterplots of Iris')
    # Draw Scatterplot
    plt.scatter(setosa_values.iloc[:, 0], setosa_values.iloc[:, 1], color='red')
    plt.scatter(versicolor_values.iloc[:, 0], versicolor_values.iloc[:, 1], color='blue')
    # Draw Linear Regression
    plt.plot(*make_polyfit(setosa_values)[:2], color='gray')
    plt.plot(*make_polyfit(versicolor_values)[:2], color='gray')
    # Design
    plt.xlabel('Sepal_Length')
    plt.ylabel('Sepal_Width')
    plt.legend(['Setosa', 'Versicolor',
                f'{make_polyfit(setosa_values)[2][1]:.2f}+{make_polyfit(setosa_values)[2][0]:.2f}x',
                f'{make_polyfit(versicolor_values)[2][1]:.2f}+{make_polyfit(versicolor_values)[2][0]:.2f}x'])
    plt.tight_layout()
    plt.show()
    print('Draw Successfully.')
except Exception as e:
    print(e)
    print('Draw Failed.')