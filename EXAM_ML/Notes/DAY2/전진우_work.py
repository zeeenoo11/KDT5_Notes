# [ 과제 1 ]
# : 와인 품질 선별 ML 모델 만들기
# -------------------------------------------------
# 1. 데이터 전처리(중복값 제거, feature 2개 정하기)
# 2. 데이터 정규화
# 3. KNN 모델 분석
# 4. 튜닝 후 => 최적의 파라미터 결과 분석
# -------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from ML_class import Day2_Assign_class as d2
# =================================================
# 1. 데이터 전처리
file = pd.read_csv('../DATA/winequality-white.csv', sep=';')
# print(file.info())  # Non-null, int인 quality 외 모두 float, 12 columns
# print(sum(file.duplicated())) # 937
file.drop_duplicates(inplace=True)
# print(ML_df.quality.unique())   # 6 5 7 8 4 3 9
# print(file.info())

# 1-2. feature 선정을 위한 corr 확인, 시각화
# print(file.corr())
# print(file.corr().quality.abs().sort_values(ascending=False))
# -> alcohol, density 선정
ML_df = file[['quality', 'alcohol', 'density']]
# print(ML_df.head())

PLOT = 0    # 상관계수 시각화 함수
if PLOT:
    plt.figure(figsize=(8,8))
    plt.pcolor(file.corr(), cmap='Blues')
    plt.xticks(range(len(file.columns)), file.columns, rotation=300)
    plt.yticks(range(len(file.columns)), file.columns)
    plt.colorbar()
    plt.show()

if PLOT:
    plt.scatter(ML_df['alcohol'], ML_df['density'], c=ML_df['quality'], cmap='viridis')
    plt.xlabel('alcohol')
    plt.ylabel('density')
    plt.colorbar()
    plt.title('alcohol vs density')
    plt.show()

# 1-3. density 이상치 확인
# print(ML_df.describe())
# print(ML_df[ML_df['density']>1.02])     # 2781        6     11.7  1.03898
# 1-3-2. 이상치 제거한 경우
IS_ELIMINATE = 0
if IS_ELIMINATE:
    ML_df = ML_df.drop(2781, axis=0)
    print(ML_df.describe())
# 표준편차에 큰 영향이 없으므로 제거하지 않음

# 1-4. 데이터 인덱스 정렬
ML_df = ML_df.reset_index(drop=True)
# print(ML_df)    # 3961 x 3

# 2. 데이터 정규화 : class 활용
standard_df = d2.split_standard(ML_df)
Scaled_X_train, Scaled_X_test, y_train, y_test = standard_df
# 시각화로 데이터 확인
PLOT2 = 0
if PLOT2:
    plt.scatter(Scaled_X_test[:, 0], Scaled_X_test[:, 1], c=y_test, cmap='viridis')
    plt.show()  # x,y축 모두 1값에 집중 : 정규화 확인

# 3. KNN 모델 분석
d2.score_print('KNN', KNeighborsClassifier(), ML_df)

# 3-2. n_neighbors = k 값을 조정

# max_k = Scaled_X_train.shape[0]
max_k = 100
train_scores, test_scores = [], []
for k in range(1, max_k+1):
    if k % 10 == 0:
        print(k, end=' ')
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(Scaled_X_train, y_train)
    train_scores.append(model.score(Scaled_X_train, y_train))
    test_scores.append(model.score(Scaled_X_test, y_test))
# 4. KNN에서 최적 파라미터 결과 분석
# : 가장 높은 score 값의 k 찾기
max_idx = test_scores.index(max(test_scores))
print(f'\nWhen n_neighbors : {max_idx+1}')
print(f'max_score : {max(test_scores):.3f}')
print(f'k value : {max_idx+1}\n')

# 5. 다른 분석 모듈 적용
# 5-1. SVC 모델 분석
from sklearn.svm import SVC
d2.score_print('SVC', SVC(), ML_df)

# 5-2. LogisticRegression 모델 분석
from sklearn.linear_model import LogisticRegression
d2.score_print('LogisticRegression', LogisticRegression(), ML_df)

# 6. 모델별 예측값 비교
while True:
    try:
        new_data = list(map(float, input('새로운 실수 두 개를 입력하세요(8.0~14.2, 0.99~1.03) : ').split()))
        df = pd.DataFrame([new_data], columns=['alcohol', 'density'])
        print(df)
        break
    except Exception as e:
        print(e)
        print('두 실수를 올바른 형식으로 입력해주세요.')

# 6-2.
knn_pred = d2.predict_func(KNeighborsClassifier(n_neighbors=max_idx+1), ML_df, df)
svc_pred = d2.predict_func(SVC(), ML_df, df)
lr_pred = d2.predict_func(LogisticRegression(), ML_df, df)
print(f'\nKNN 예측값 : {knn_pred}')
print(f'SVC 예측값 : {svc_pred}')
print(f'LogisticRegression 예측값 : {lr_pred}')
print(f'')


# 7. 최종결론
print(f"""
최종 분석 결과, 
KNN 모델의 경우 n_neighbors 값을 조정하여 최적의 파라미터를 찾아낼 수 있었다.
파라미터 미입력 값보다 값이 {max_idx+1} 일 때 더 정확하다.


""")

# 문제; split을 계속 반복함, 하나로 클래스 통일 -> standard_df
# 문제2; new_data가 9 1 일때


# <아침 리뷰>
# 이상치를 조절하면 결과값이 좋아진다
#   - 이상치 제거 후 상관계수를 보자
# 결과를 숫자가 아닌 평가(좋음 / 질감 / 맛 등)으로 표현할 수도 있다
# n_neighbors=5 ; 기본이 5로 맞춰져있다
