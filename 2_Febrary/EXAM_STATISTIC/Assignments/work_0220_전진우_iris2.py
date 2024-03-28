import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
from scipy import integrate

# < 과제3 - 붓꽃 데이터셋 활용 2 >
# [ 문제 1 ] 데이터셋 불러오기 및 기본 정보 확인
# 1) 붓꽃 데이터셋을 불러오고 데이터프레임으로 변환, 첫 5행 출력
# 2) 데이터 프레임의 기본 정보를 확인하고 각 열의 데이터 타입을 제시
# 3) 품종에 대한 클래스 분포를 확인하고, 각 클래스별 데이터 개수를 제시
#
# [ 문제 2 ] 데이터 시각화 및 탐색
# 1) 붓꽃 데이터셋에서 각 특성 간의 산점도를 그리되, 각 클래스별 다른 색상을 사용하여 시각화
# 2) 꽃받침의 길이와 너비의 관계를 시각화하고 각 클래스별로 구분하여 출력
#
# [ 문제 3 ] 연속확률변수 및 연속확률분포 계산
# 1) 꽃잎의 길이를 연속확률변수로 가정할 때, 이 확률 변수의 평균과 분산을 계산
# 2) 꽃잎의 너비를 연속확률변수로 가정할 때, 이 확률 변수의 확률 밀도 함수를 계산하고 그래프로 시각화
# 3) 꽃잎의 길이가 4cm 이상 5cm 미만을 확률을 계산
# ------------------------------------------------------------------------------------------
print('[문제1]')
print("1) 붓꽃 데이터셋 불러오기 및 기본 정보 확인")
file = pd.read_csv('DATA/iris.csv', encoding='utf-8')
print(file.head())

print("2) 데이터 프레임의 기본 정보를 확인하고 각 열의 데이터 타입을 제시")
print(file.info())
print(file.dtypes)

print("3) 품종에 대한 클래스 분포를 확인하고, 각 클래스별 데이터 개수를 제시")
print("품종의 종류:", file.species.unique())
print("품종별 데이터 개수: "
      "Setosa", file[file.species == 'setosa'].shape[0], '개,',
       "Versicolor", file[file.species == 'versicolor'].shape[0], '개,',
       "Virginica", file[file.species == 'virginica'].shape[0], '개,')

print('[문제2]')
print("1) 붓꽃 데이터셋에서 각 특성 간의 산점도를 그리되, 각 클래스별로 다른 색상을 사용하여 시각화")
# 특성 간 데이터프레임 구분
Setosa = file[file.species == 'setosa'].iloc[:, :-1]
Versicolor = file[file.species == 'versicolor'].iloc[:, :-1]
Virginica = file[file.species == 'virginica'].iloc[:, :-1]
species = [Setosa, Versicolor, Virginica]
names = ['Setosa', 'Versicolor', 'Virginica']
colors = ['red', 'blue', 'green']
# print(Setosa)
# 산점도 그리기: 총 6칸
fig = plt.figure(figsize=(15, 10))
f_properties = file.columns[:-1]
cnt = 0
for i in range(len(f_properties)):
    for j in range(i+1, i+len(file.columns[i:-1])):
        cnt += 1
        ax = fig.add_subplot(2, 3, cnt)
        ax.set_title(f'{file.columns[i]} vs {file.columns[j]}')
        for k in range(len(species)):   # 품종별 산점도 그리기
            ax.scatter(species[k].iloc[:, i], species[k].iloc[:, j], color=colors[k], marker='o')
        # Design
        ax.set_xlabel(file.columns[i])
        ax.set_ylabel(file.columns[j])
        ax.legend(file.species.unique())

fig.suptitle('Scatterplots by Properties comparing of Species', fontsize=20)
fig.subplots_adjust(wspace=0.5, hspace=0.5)
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
print('[Figure1]\n')

print("2) 꽃받침의 길이와 너비의 관계를 시각화하고 각 클래스별로 구분하여 출력")
# 히트맵 그리기
fig = plt.figure(figsize=(10, 3))
cnt = 0
for sp in species:
    cnt += 1
    ax = fig.add_subplot(1, 3, cnt)
    ax.set_title(names[cnt-1])
    x_val = sp.iloc[:, 0]
    y_val = sp.iloc[:, 1]
    c = ax.hist2d(x_val, y_val, bins=[10, 10], cmap='Blues',
                  range=[(x_val.min(), x_val.max()), (y_val.min(), y_val.max())])
    ax.set_xlabel('sepal length')
    ax.set_ylabel('sepal width')
    ax.set_xticks(c[1])
    ax.set_yticks(c[2])
    fig.colorbar(c[3], ax=ax)
plt.tight_layout()
plt.show()
print("[Figure2]\n")


def cont_prob(data):
    """
    확률 계산 함수
    :param data: elements; data array
    :return: element, count/len(data)
    """
    element, count = np.unique(data, return_counts=True)    # count 반환
    return element, count*count/len(data)     # 전체로 나눔: 확률

# print(cont_prob(file['sepal_length']))


print("[ 문제 3 ]")
print("1) 꽃받침의 길이를 연속확률변수로 가정할 때, 이 확률 변수의 평균과 분산을 계산")
print('전체 꽃받침 길이 값: np.array(file["sepal_length"])')
print('평균:', np.mean(file['sepal_length']))
print('분산:', np.var(file['sepal_length']))
print('\n')


print("2) 꽃잎의 너비를 연속확률변수로 가정할 때, 이 확률 변수의 확률 밀도 함수를 계산하고 그래프로 시각화")
# 확률 밀도 함수 그리기
plt.figure(figsize=(10, 5))
plt.title('Probability Density Function')
plt.xlabel('petal length')
plt.ylabel('Probability')
x1 = np.array(cont_prob(file['petal_width'])[0])
y1 = np.array(cont_prob(file['petal_width'])[1])
print(len(y1))
print(x1, y1)
f = np.poly1d(np.polyfit(x1, y1, 5))
plt.plot(x1, y1)
plt.plot(x1, f(x1), 'r')
plt.show()





print("3) 꽃잎의 길이가 4cm 이상 5cm 미만일 확률을 계산")
x2 = np.array(cont_prob(file['petal_length'])[0])
y2 = np.array(cont_prob(file['petal_length'])[1])
f2 = np.poly1d(np.polyfit(x2, y2, 5))
print(integrate.quad(f2, 4, 5)[0])
print(len(file['petal_length']))
# 결과는 0.13, 하지만 150개 중 48개로 0.28에 가까워야함