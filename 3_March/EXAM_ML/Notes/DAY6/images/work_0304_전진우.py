import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2 as img
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.datasets import fetch_openml

# [ 과제 0304 ]
# - 이미지 이진분류 / 다중 분류
# - data : 144p - mnist
# - 조건1 : 모델 성능지표 분석
# - 조건2 : 이미지 생성 후 predict까지 진행
# - logistic, SGD
# - score로 과대적합/과소적합
# - 분류 성능 리포트
# --------------------------------------
# T0 ~ T9: track textbook
# T0. Prepare Data
mnist = fetch_openml("mnist_784", as_frame=False, parser="auto")
# print(mnist)
# T1. Set data and target
X, y = mnist["data"], mnist["target"]
# print(X.shape, y.shape)

# get each number's counts
# yDF = pd.DataFrame(y)
# print(yDF.value_counts()) # 1 is the most


def plot_digit(image_data):  # T2 : digit plotting func.
    """make plot from data to image
    Args:
        image_data (_type_): mnist data
    """
    image = image_data.reshape(28, 28)
    plt.imshow(image, cmap="binary")
    plt.axis("off")
    plt.show()


# Test the function
some_digit = X[0]
TEST = 0
if TEST:
    plot_digit(some_digit)

# T3. Split Set (Already splited)
X_train, X_test, y_train, y_test = X[:6000], X[6000:], y[:6000], y[6000:]


# T4. Make y values as binary : 1 is the most number
y_train_1 = y_train == "1"
y_test_1 = y_test == "1"
# print(y_train_1, y_test_1)

# T5. Load SGDClassifier Module
sgd_clf = SGDClassifier(random_state=11)
sgd_clf.fit(X_train, y_train_1)

# T6. Test
# print(sgd_clf.score(X_test, y_test_1))  # 0.9698
# print(sgd_clf.predict([some_digit]))    # True
# ----------------------------------------------


print("---------- [조건1] 모델 성능지표 분석 ------------")
# 1. SGD Classifier : 이진 분류
# - 이진 분류 : sgd_clf 그대로 사용
print("< 1 기준 이진 분류 학습 >")
print("[SGD train score] :", sgd_clf.score(X_train, y_train_1))  # 0.997
print("[SGD test score] :", sgd_clf.score(X_test, y_test_1))  # 0.986
# => 최적 적합

# 2. 분류 성능 테스트 : 정확도, 정밀도, 재현율, F1
print("\n< SGD Classifier의 분류 성능 테스트 >")
y_pred = sgd_clf.predict(X_test)

# 0) 혼잡 행렬 확인 - confusion_Matrix
#   : X_train 기반으로 학습한 sgd_clf에서 X_test로 예측한 y_pred를 정답인 y_test_1과 비교
ret = confusion_matrix(y_test_1, y_pred)
print("[혼잡 행렬 결과 값]\n", ret)

# 0-2) 시각화
conplot = ConfusionMatrixDisplay(ret, display_labels=["Not 1", "1"])
PLOT1 = 0
if PLOT1:
    conplot.plot(cmap="Blues")
    plt.show()  # TP : 6775

# 1) 정확도 : (TP+TN) / (TP+TN+FP+FN)
print(f"[정확도] : {accuracy_score(y_test_1, y_pred):.5f}")  # 0.9864

# 2) 정밀도 : TP / (TP+NP)
print(f"[정밀도] : {precision_score(y_test_1, y_pred):.5f}")  # 0.9395

# 3) 재현율 : TP / (TP+FP)
print(f"[재현율] : {recall_score(y_test_1, y_pred):.5f}")  # 0.9401

# 4) f1_score
f1_scores = f1_score(y_test_1, y_pred)
print(f"[f1_score] : {f1_scores:.5f}")  # 0.93986


# 2. SGD 다중 분류
# 1) y_train, y_test 그대로 사용
sgd_multi = SGDClassifier(random_state=11)
sgd_multi.fit(X_train, y_train)
print("\n< SGD Classifier의 다중 분류 성능 테스트 >")
print("[multi test score] :", sgd_multi.score(X_test, y_test))

# 2) 분류 성능 테스트
y_pred_m = sgd_multi.predict(X_test)
print("[multi confusion matrix] :\n", confusion_matrix(y_test, y_pred_m))
print(f"[정확도] : {accuracy_score(y_test, y_pred_m):.5f}")
print(f'[정밀도] : {precision_score(y_test, y_pred_m, average="weighted"):.5f}')
print(f'[재현율] : {recall_score(y_test, y_pred_m, average="weighted"):.5f}')
print(f'[f1_score] : {f1_score(y_test, y_pred_m, average="weighted"):.5f}')
# 0.86059   0.86232     0.86059     0.85946


"""
# . partial_fit으로 1 Epoch씩 학습
train_score, test_score = [], []
for _ in range(100):
    sgd_multi.partial_fit(X_train, y_train, classes=np.unique(y_train))
    train_score.append(sgd_multi.score(X_train, y_train))
    test_score.append(sgd_multi.score(X_test, y_test))
    if train_score[-1] > 0.95 and test_score[-1] > 0.95:
        break   # 이건 실패

# -2. 시각화
PLOT_EPOCH = 1
if PLOT_EPOCH:
    plt.plot(train_score, label='train score')
    plt.plot(test_score, label='test score')
    plt.xlabel('Epoch')
    plt.ylabel('score')
    plt.legend()
    plt.show()  # 시각화는 과적합, 0.97 0.86
"""


# 3. Logistic Regression
print("\n< Logistic Regression 학습 >")
# TODO 다중 분류에서 Logistic Regression을 쓰는 게 맞나? 이건 회귀인가? 우선 이진화 대입됨
model_log = LogisticRegression(max_iter=2000, random_state=11)
model_log.fit(X_train, y_train_1)
log_train_score = model_log.score(X_train, y_train_1)
log_test_score = model_log.score(X_test, y_test_1)
print("[logi_Reg train score] :", log_train_score)  # 1.0
print("[logi_Reg test score] :", log_test_score)  # 0.949
# TODO 과대적합/과소적합 판별 위함 : train이 1.0, 원래 이런건가, 의미 없는 건가? 내가 잘못 구한건가


print(" ----- [조건2] 그림판 이미지 생성 후 predict -----")
# [이진 분류 예측]
# 1. 이미지 입력
image_list = [
    "image0.png",
    "image1_01.png",
    "image2.png",
    "image3_01.png",
    "image4.png",
    "image5.png",
    "image6.png",
    "image7.png",
    "image8.png",
    "image9.png",
]

# 2. image => data : cv2 module 사용


def predict_image(image, num, PLOT=False):
    print(f"[predict_image] No.{num}")
    image_data = img.imread(image, img.IMREAD_GRAYSCALE)
    img.imshow("image_data", image_data)
    img.waitKey(0)
    img.destroyAllWindows()
    image_data = img.resize(image_data, (28, 28))
    image_data = np.invert(image_data)
    # print('[image_array] :', image_data)
    if PLOT:
        plot_digit(image_data)

    # 3. predict
    # 1) SGD 이용
    # print(image_data.reshape(1, -1))
    sgd_pred = sgd_clf.predict(image_data.reshape(1, -1))  # 하나의 행으로 변환
    print("[sgd_pred] :", sgd_pred)  # True


# 4. 확인
print("[ 이미지가 1인지 아닌지 확인하기 ]")
for i in range(len(image_list)):
    predict_image(image_list[i], i)
    print()  # 1에서만 True


# [다중 분류 예측]
# 시간이 없어 복붙
def predict_image(image, num, PLOT=False):
    print(f"[predict_image] No.{num}")
    image_data = img.imread(image, img.IMREAD_GRAYSCALE)
    img.imshow("image_data", image_data)
    img.waitKey(0)
    img.destroyAllWindows()
    image_data = img.resize(image_data, (28, 28))
    image_data = np.invert(image_data)
    # print('[image_array] :', image_data)
    if PLOT:
        plot_digit(image_data)

    # 3. predict
    # 1) SGD 이용
    # print(image_data.reshape(1, -1))
    sgd_pred = sgd_multi.predict(image_data.reshape(1, -1))  # 하나의 행으로 변환
    print("[sgd_multi] :", sgd_pred)  # True


# 4. 확인
print("[ 이미지가 1인지 아닌지 확인하기 ]")
for i in range(len(image_list)):
    predict_image(image_list[i], i)
    print()  # 0 1 2 3 3 5 6 3 3 7

# 6/10

# 임의 confusion Matrix
# 0 : 1 0 0 0 0 0 0 0 0 0
# 1 : 0 1 0 0 0 0 0 0 0 0
# 2 : 0 0 1 0 0 0 0 0 0 0
# 3 : 0 0 0 1 1 0 0 1 1 0
# 4 : 0 0 0 1 0 0 0 0 0 0
# 5 : 0 0 0 0 0 1 0 0 0 0
# 6 : 0 0 0 0 0 0 1 0 0 0
# 7 : 0 0 0 0 0 0 0 0 0 1
# 8 : 0 0 0 1 0 0 0 0 0 0
# 9 : 0 0 0 0 0 0 0 1 0 0


# 부족한 것
# 1. parameter 설정 : n_iter 값 변경해보기 (for문에서 사용하긴 함)
# 2. loss 사용
# 3. 미니배치 개념


# 고생한 것
# 1. cv2 설치
# 1) 가상환경 옮기기 : conda activate EXAM_MML
# 2) pip install opencv-python
