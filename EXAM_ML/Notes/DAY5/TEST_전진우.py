# ML-TEST 1차 
# 1. 기계학습 프로세스에 대해 간략하게 설명하세요
#   - 목표 설정 -> 데이터 확인 -> 모델 학습 -> 모델 평가 -> 활용

# 2. 기계학습에 사용되는 데이터셋에 대해 설명하세요
#   - feature와 target으로 나누며, target은 Series형태고 feature의 갯수는 다양함.
#   - feature에 맞는 target을 찾도록 학습시킴

# 3. 지도학습의 특징을 설명하세요
#   - 문제와 정답을 함께 제시하여 훈련시키고, 평가에선 문제만 제시하여 일치하는 정도를 판단
#   - 중간 검증 과정도 필요시 거침

# 4. 데이터 전처리 중 처음 데이터 수집 후 데이터 정제하는 과정에 진행되는 작업을 설명하세요
#   - 1. 데이터 타입 확인 / 변환
#   - 2. 결측치, 중복값, 이상치 확인 / 제거

# 5. 모델 개념을 설명해 주세요
#   - 기계학습을 시킬 때 바탕이 되는 공식으로, 클래스 선언 후 피처 및 타겟 데이터셋을 입력해
#   - 메서드 함수(.fit, .score, .predict)를 실행하며 데이터를 저장, 생성, 변환함
 
# 6. 모델의 결과 값이 수치를 예측해주는 기계학습은 무엇인가요?
#   - 회귀

# 7. 모델 파라미터는 무엇인가요?
#   - 모델 연산에 입력되는 매개변수로, 데이터 및 목표에 적합한 결과를 도출하기 위해
#   - 튜닝하는 데 사용됨

# 8. KNN 알고리즘에 대해 설명해 주세요
#   - KNeighborsNear... 의 약자로, 
#   - 매개변수인 n_neighbors 값으로 근처의 데이터 개수를 근접값으로 판단해 
#   - 분류(-Classifier)나 회귀(Regression)를 진행하는 알고리즘 

# 9. 하이퍼 파라미터는 무엇인가요?
#   - 튜닝에 사용되는 매개변수, 결과 산출에 큰 영향을 줌

# 10. Regression의 성능평가 지표들을 설명하세요
#   - R2 : 오차의 정도를 평가; 오차 제곱의 합을 전체 개수로 나눔
#   - MAE : 평균절대값오차
#   - RMSE : 평균제곱오차의 제곱근

# 11. LinearRegression알고리즘에 대해 설명해 주세요
#   - 선형회귀 분석, 직선을 가정하여 각 데이터와의 거리가 가장 가까운 직선을 그리는 것

# 12. Classification의 성능평가 지표들을 설명하세요
#   - f1 : 정밀도와 재현율을 반영한 지표

# 13. 피쳐공학에 대해 설명하세요
#   - feature를 선별, 생성, 그룹화 등으로 최적의 결과를 도출하는 것

# 14. LogisticRegression알고리즘에 대해 설명해 주세요

# 15. 과대적합 과소적합에 대해 설명해 주세요
#   - 훈련 및 테스트 평가를 진행했을 때,
#   - 과대적합은 훈련 자료에 너무 맞춰져 훈련 평가보다 테스트 평가가 현저히 낮은 것이고
#   - 과소적합은 훈련 평가 자체가 현저히 낮은 것이다.


# 16. 아래 데이터셋을 기반으로 분류 회귀 모델을 완성 후 성능평가까지 구현하세요
# - : iris.csv 데이터셋
# - 조건
#   * 분류 : 3개 품종 중 2개 선택하여 이진 분류 진행
#   * 회귀 : 3개 품종 중 1개 선택, 4개 피쳐 중 꽃잎의 길이값 예측 회귀
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier

# -------------------------------------------------------------------
# 0. 데이터 불러오기
irisDF = pd.read_csv('iris.csv')
print(irisDF.info())    # float, species만 obj

# 1. 데이터 전처리
# 결측치 없음
print('중복값 :', irisDF.duplicated().sum())   # 3
# 중복값 제거
irisDF = irisDF.drop_duplicates()
# print(irisDF.info())
# 이상치 확인 전 분류 먼저 진행

# 2. 데이터 분리 : setosa, versicolor 중 피처 타겟 분리
irisDF_seve = irisDF[irisDF['species'] != 'virginica']

feature = irisDF_seve.drop(['species'], axis=1)
target = irisDF_seve['species']
xtr, xte, ytr, yte = train_test_split(feature, target, test_size=0.2, random_state=11, stratify=target)
# print(xtr.shape, xte.shape, ytr.shape, yte.shape)

# 3. 이진 분류 : SDGClassifier()
model = SGDClassifier(loss='log_loss', random_state=11)
model.fit(xtr, ytr)
print('Loss=log', model.score(xte, yte))

# 3-2. Loss 변경
model = SGDClassifier(loss='hinge', random_state=11)
model.fit(xtr, ytr)
print('Loss=hinge', model.score(xte, yte))
# 둘 다 1.0 ?

# 4. 예측 (loss=hinge)
new_data = [[5.1, 3.5, 1.4, 0.2]]
pred = model.predict(new_data)
print(pred) # 'setosa'



# [ 회귀 ]
iris_se = irisDF[irisDF['species'] != 'setosa']





