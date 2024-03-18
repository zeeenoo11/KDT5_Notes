import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ML_class import scaler_model as sm
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler, MinMaxScaler, RobustScaler
from sklearn.metrics import mean_squared_error

# < 과제3 : auto-mpg.csv 에서 마력 최대값을 구하기 >
# -------------------------------------------------------
# 1. 데이터 확인
#   1) 데이터 불러오기
#   2) 이상치, 결측치, 중복값 확인
# 2. 정규화 스케일러 결정
#   1) StandardScaler, MinMaxScaler, RobusrScaler 중 선택
#   2) 
# 3. 회귀 모델 결정
#   1) 선형 또는 다항 중에 선택
# -------------------------------------------------------

# 1. 데이터 불러오기
df = pd.read_csv(r'DATA\auto-mpg.csv')
# print(df.info())  # => 결측치 없음, horsepower가 object, 398 x 9

# 1-2. '?' 값을 nan으로 변환
df.horsepower = df.horsepower.replace('?', np.nan)

# 1-3. horsepower열의 타입 변경
df.horsepower = df.horsepower.astype(float).copy()

# 1-4. nan 값 변환
# 1) 시각화하여 분포 확인
PLOT = 0
if PLOT:
    plt.hist(df['horsepower'])
    plt.vlines(df['horsepower'].mean(), 0, 100, colors='r', linestyles='dashed', label='Mean')
    plt.vlines(df['horsepower'].median(), 0, 100, colors='y', linestyles='dashed', label='Median')
    plt.title('Horsepower Distribution : Compare mean and median')
    plt.legend()
    plt.show() 
# => 좌편향된 분포를 보임, 중앙값보다 평균이 더 크다.
#    이상치를 제거한다 가정할 때 중앙값을 결측치에 넣는 게 합리적이라 판단

# 2) 중앙값을 nan에 대입
df['horsepower'].fillna(value=df['horsepower'].median(), inplace=True)


# 2. 데이터 확인
# 2-1. 이상치 확인
PLOT2 = 0
if PLOT2:
    plt.figure(figsize=(10, 5))
    plt.boxplot(df.iloc[:, :-1])
    plt.xticks(range(1, len(df.columns)), df.columns[:-1])
    plt.show()
    plt.close()   # => weight가 너무 커 정규화 먼저 진행

# 2-2. 클래스에서 함수 호출하여 이상치 제거
outlier, filtered = sm.remove_outliers(df, df.columns[:-1], 2)
print(df.shape, len(outlier), filtered.shape)
# => 클래스 오류, todo


# 2-3. 상관계수

# 3. 정규화 스케일러 결정
scalers = [StandardScaler, MinMaxScaler, RobustScaler]


# 3-1. 학습 점수로 판별
scores = []
for scaler in scalers:
    scaler = scaler()
    scaler.fit(df.iloc[:, :-1])
    scaled_features = scaler.transform(df.iloc[:, :-1])
    scaled_df = pd.DataFrame(scaled_features, columns=df.columns[:-1])


    # 4. 회귀 분석 모델 결정
    # 4-1. 선형 회귀 vs 다항 회귀
    linear_regression = LinearRegression()
    linear_regression.fit(scaled_df, df['mpg'])
    linear_regression_score = linear_regression.score(scaled_df, df['mpg'])
    
    polynomial_features = PolynomialFeatures(degree=2)
    X_poly = polynomial_features.fit_transform(scaled_df)
    linear_regression_poly = LinearRegression()
    linear_regression_poly.fit(X_poly, df['mpg'])
    linear_regression_poly_score = linear_regression_poly.score(X_poly, df['mpg'])
    
    scores.append({
        'scaler': scaler.__class__.__name__,
        'linear_regression_score': linear_regression_score,
        'linear_regression_poly_score': linear_regression_poly_score
    })

# 3-2. 점수 비교
for i, score in enumerate(scores):
    print(f"{i+1}. Scaler: {score['scaler']}")
    print(f"Linear Regression Score: {score['linear_regression_score']:.4f}")
    print(f"Linear Regression with Polynomial Features Score: {score['linear_regression_poly_score']:.4f}")
    print()
    
