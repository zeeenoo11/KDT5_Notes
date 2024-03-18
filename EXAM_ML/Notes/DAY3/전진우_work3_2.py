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
# 3. 회귀 모델 결정
#   1) 선형 또는 다항 중에 선택
# -------------------------------------------------------

# 1. 데이터 확인
# 1-1. 데이터 불러오기
df = pd.read_csv(r'DATA\auto-mpg.csv')
# print(df.info())  # => 결측치 없음, horsepower가 object, 398 x 9

# 1-2. '?' 값을 nan으로 변환
df.horsepower = df.horsepower.replace('?', np.nan)

# 1-3. horsepower열의 타입 변경
df.horsepower = df.horsepower.astype(float).copy()

# 1-4. nan 값 변환
# 1) 시각화하여 분포 확인
PLOT = 1
if PLOT:
    plt.hist(df['horsepower'])
    plt.vlines(df['horsepower'].mean(), 0, 100, colors='r', linestyles='dashed', label='Mean')
    plt.vlines(df['horsepower'].median(), 0, 100, colors='y', linestyles='dashed', label='Median')
    plt.title('Horsepower Distribution : Compare mean and median')
    plt.legend()
    # 그래프를 3초 후 내리는 명령어
    plt.show(block=False)
    plt.pause(5)
    plt.close()
# => 좌편향된 분포를 보임, 중앙값보다 평균이 더 크다.
#    이상치를 제거한다 가정할 때 중앙값을 결측치에 넣는 게 합리적이라 판단

# 2) 중앙값을 nan에 대입
df['horsepower'].fillna(value=df['horsepower'].median(), inplace=True)

# 1-5. 상관계수 확인 : feauture 결정
total_feature = ['horsepower', 'mpg', 'cylinders', 'displacement', 'weight', 'acceleration', 'model year', 'origin']
print(df[total_feature].corr().horsepower.abs().sort_values(ascending=False))
# displacement    0.895778
# weight          0.862442
# cylinders       0.841284
# mpg             0.773453
# acceleration    0.686590
# origin          0.452096
# model year      0.413733

# 1-6. feature와 target 분리
# : 가장 높은 상관계수를 보이는 세 피처를 선택
feature = df[['displacement', 'weight', 'cylinders']]
target = df['horsepower']

plt.figure(figsize=(12, 4))
for i, col in enumerate(feature):
    plt.subplot(1, len(feature.columns), i+1)
    plt.scatter(feature.loc[:, col], target)
    plt.xticks([]); plt.yticks([])
    plt.xlabel(col); plt.ylabel('horsepower')
    plt.title(col)
plt.tight_layout()
plt.show(block=False)
plt.pause(5)
plt.close()


# 1-6. 이상치 확인




X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size=0.2, random_state=42)

# 1-7. 선형 회귀 모델 학습
linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)

# 1-8. 선형 회귀 모델 예측
y_linear_pred = linear_regression.predict(X_test)

# 1-9. 선형 회귀 모델 평가
linear_regression_mse = mean_squared_error(y_test, y_linear_pred)
linear_regression_rmse = np.sqrt(linear_regression_mse)
print(f'Linear Regression MSE: {linear_regression_mse:.4f}')
print(f'Linear Regression RMSE: {linear_regression_rmse:.4f}')

# 1-10. 다항 회귀 모델 학습
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

linear_regression_poly = LinearRegression()
linear_regression_poly.fit(X_train_poly, y_train)

# 1-11. 다항 회귀 모델 예측
y_poly_pred = linear_regression_poly.predict(X_test_poly)

# 1-12. 다항 회귀 모델 평가
poly_mse = mean_squared_error(y_test, y_poly_pred)
poly_rmse = np.sqrt(poly_mse)
print(f'Polynomial Regression MSE: {poly_mse:.4f}')
print(f'Polynomial Regression RMSE: {poly_rmse:.4f}')

# 1-13. 스케일러 비교
scaler_models = [StandardScaler(), MinMaxScaler(), RobustScaler()]
scaler_names = ['StandardScaler', 'MinMaxScaler', 'RobustScaler']

for scaler, scaler_name in zip(scaler_models, scaler_names):
    # 1-14. 스케일러 적용
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 1-15. 스케일러 적용 후 선형 회귀 모델 학습
    linear_regression_scaled = LinearRegression()
    linear_regression_scaled.fit(X_train_scaled, y_train)

    # 1-16. 스케일러 적용 후 선형 회귀 모델 예측
    y_linear_scaled_pred = linear_regression_scaled.predict(X_test_scaled)

    # 1-17. 스케일러 적용 후 선형 회귀 모델 평가
    linear_regression_scaled_mse = mean_squared_error(y_test, y_linear_scaled_pred)
    linear_regression_scaled_rmse = np.sqrt(linear_regression_scaled_mse)
    print(f'{scaler_name} Linear Regression MSE: {linear_regression_scaled_mse:.4f}')
    print(f'{scaler_name} Linear Regression RMSE: {linear_regression_scaled_rmse:.4f}')
    
    # R2 값 출력
    print(f'{scaler_name} R2: {linear_regression_scaled.score(X_test_scaled, y_test):.4f}')