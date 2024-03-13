import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
from sklearn.utils import all_estimators
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.preprocessing import (
    PolynomialFeatures,
    StandardScaler,
    MinMaxScaler,
    RobustScaler,
    OneHotEncoder,
    LabelEncoder,
)
from sklearn.model_selection import (
    train_test_split,
    KFold,
    cross_val_score,
    GridSearchCV,
    RandomizedSearchCV,
    cross_validate,
)
from sklearn.metrics import (
    accuracy_score,
    r2_score,
    mean_squared_error,
    mean_absolute_error,
)

# from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
# from sklearn.pipeline import make_pipeline, Pipeline

# [ Tips ]
# 1. 폴더가 다른 class.py 가져오기
# import sys
# sys.path.append('../')


class Assign_class:
    # 설명 : 제일 처음 만든 클래스 / 매우 기본적
    # [목록]
    # 1. split_standard
    # 2. standard_scaler
    # 3. score_print
    # 4. predict_func

    def __init__(self, df):
        self.df = df

    @classmethod
    def split_standard(cls, df):
        """
        학습 데이터와 테스트 데이터로 나누고 정규화하는 함수
        :param df: 변환할 데이터프레임
        :return:
        """
        # 2-1. 학습 데이터 분리 : train_test_split
        feature = df.iloc[:, 1:]
        target = df.iloc[:, 0]
        X_train, X_test, y_train, y_test = train_test_split(
            feature, target, test_size=0.2, stratify=target
        )

        # 2-2. 정규화 모듈 사용
        def standard_scaler(df):
            scaler = StandardScaler()
            scaler.fit(df)
            ret = scaler.transform(df)
            return ret

        # 2-3. 정규화 수행
        X_train = standard_scaler(X_train)
        X_test = standard_scaler(X_test)
        # print(X_train, X_test)
        return X_train, X_test, y_train, y_test

    @classmethod
    def score_print(cls, model_name, model_func, df):
        xtr, xte, ytr, yte = cls.split_standard(df)
        model = model_func
        model.fit(xtr, ytr)

        print(f"{model_name} train:", round(model.score(xtr, ytr), 3))
        print(f"{model_name} test:", round(model.score(xte, yte), 3))

    @classmethod
    def predict_func(cls, model_func, df, new):
        xtr, xte, ytr, yte = cls.split_standard(df)
        model = model_func
        model.fit(xtr, ytr)
        pred = model.predict(new)
        return pred


class scaler_model:
    # 설명 :
    # [목록]
    # 1. find_outliers
    # 2. object_encoder : object->float/int by LabelEncoder\
    def __init__(self) -> None:
        pass

    @classmethod
    def find_outliers(cls, data, iqr_multiplier=1.5, PLOT=False):
        """Find outliers in the given data.

        Args:
            data (DataFrame): Input DataFrame.
            iqr_multiplier (float, optional): Multiplier for interquartile range. Defaults to 1.5.
            PLOT (bool, optional): Whether to plot outliers. Defaults to False.

        Returns:
            list: List of outliers for each column.
        """
        outliers = []
        for col in data.columns:
            q1 = np.percentile(data[col], 25)
            q3 = np.percentile(data[col], 75)
            iqr = q3 - q1
            lower_bound = q1 - iqr * iqr_multiplier
            upper_bound = q3 + iqr * iqr_multiplier
            mask = (data[col] < lower_bound) | (data[col] > upper_bound)
            outliers.append(data[col][mask].values.tolist())

        # if PLOT:
        #     plot_func.box_plot(data, outliers, filter)

        return outliers

    # new_hair = scaler_model.object_encoder(LukeDF)
    # 이렇게 호출해야한다 왜 그런진 아직 모르겠다 싫으면 __call__ 쓰래
    @classmethod
    def object_encoder(cls, DF):
        """Transform object type columns into float or int
        Args:
            DF : DataFrame
        Returns:
            new_DF, label
        ver.1.2
        """
        new_DF = DF.copy()
        label = LabelEncoder()
        object_cols = new_DF.select_dtypes(include=["object"]).columns
        for col in object_cols:
            new_DF[col] = label.fit_transform(new_DF[col])
        return new_DF, label


class plot_func:
    # 설명 : 미완

    @classmethod
    def box_plot(cls, data, outliers, filter, columns, PLOT=True):
        # box_plot을 출력
        # return값으로 outliers, filtered_data 등을 출력
        pass
    
    @classmethod
    def corr_dataframe(cls, dataDF, top5=False):
        data_corr = dataDF.corr().abs()
        df = pd.DataFrame()
        for i in range(len(data_corr.columns)):
            corr_i = data_corr.iloc[:, i].sort_values(ascending=False).reset_index(drop=True)
            df = pd.concat([df, corr_i], axis=1)
        
        if top5:
            mask = df.iloc[1, :].sort_values(ascending=False).head().index # 높은 상관계수를 보이는 col
            return dataDF.corr()[mask]
        else:    
            return df
        
    @classmethod
    def data_check(cls, dataDF):
        # 2) 이상치 확인 : histogram, scatter, boxplot
        # - 
        from matplotlib import pyplot as plt

        COLOR = '#6495ED'
        COLOR2 = '#F08080'
        # columns which value count is more than 2
        over2_cols = dataDF.loc[:, dataDF.nunique() > 2].columns
        binary_cols = dataDF.loc[:, dataDF.nunique() == 2].columns

        # 값이 2가지 일때
        for col in dataDF.columns:
            if col in binary_cols:
                plt.figure(figsize=(12, 4))
                plt.title(col)
                plt.xticks([])
                plt.yticks([])
                plt.subplot(1, 3, 1)
                plt.bar(dataDF[col].unique(), dataDF[col].value_counts(), color=COLOR)
                plt.xticks([0, 1])
                plt.ylabel('Count')
                plt.subplot(1, 3, 2)
                plt.hist(dataDF[dataDF[col] == 1].BMI, color=COLOR, alpha=0.5, label='1')
                plt.hist(dataDF[dataDF[col] == 0].BMI, color=COLOR2, alpha=0.5, label='0')
                plt.legend()
                plt.subplot(1, 3, 3)    # boxplot
                # dataDF[col] == 1 일때와 0 일때
                plt.boxplot(dataDF[dataDF[col] == 1].BMI, labels=[0], vert=False, positions=[1])
                plt.boxplot(dataDF[dataDF[col] == 0].BMI, labels=[1], vert=False, positions=[2])
                plt.xlabel('BMI')
                    
                plt.tight_layout()
            

            # 값이 2가지 이상
            if col in over2_cols:
                plt.figure(figsize=(12, 4))
                plt.title(col)
                plt.xticks([])
                plt.yticks([])
                plt.subplot(1, 3, 1)
                plt.hist(dataDF[col], color=COLOR)
                plt.ylabel('Count')
                plt.subplot(1, 3, 2)
                corr = dataDF['BMI'].corr(dataDF[col])
                plt.scatter(dataDF[col], dataDF['BMI'], color=COLOR, alpha=0.5, label = f'corr: {corr:.2f}')
                plt.legend()
                plt.xlabel(col)
                plt.ylabel('BMI')
                plt.subplot(1, 3, 3)
                plt.boxplot(dataDF[col], vert=False)
                plt.tight_layout()
        plt.show()


class hj_model:
    # 설명 : 박희진님의 코드를 훔쳐온 클래스입니다.
    # [목록]

    def __init__(self, DF):
        self.DF = DF

    def print_scatter(nrows, ncols, targetSR, featureDF):
        n = 1
        for col in featureDF.columns:
            plt.subplot(nrows, ncols, n)
            plt.scatter(
                targetSR,
                featureDF[col],
                label=f"corr = {targetSR.corr(featureDF[col]):.4f}",
            )
            plt.xlabel(targetSR.name)
            plt.title(f"{col}")
            plt.ylabel(col)
            plt.xticks([])
            plt.legend()
            n += 1
        plt.tight_layout()
        plt.show()

    def print_hist(nrows, ncols, featureDF):

        n = 1
        for col in featureDF.columns:
            plt.subplot(nrows, ncols, n)
            plt.hist(featureDF[col], edgecolor="k", color="yellow")
            plt.title(f"{col}")
            plt.ylabel(col)
            n += 1
        plt.tight_layout()
        plt.show()

    def print_box(nrows, ncols, targetSR, featureDF):
        n = 1
        for i in featureDF.columns:
            plt.subplot(nrows, ncols, n)
            plt.boxplot(featureDF[i])
            plt.xlabel(targetSR.name)
            plt.title(f"{i}")
            n += 1
        plt.tight_layout()
        plt.show()

    def find_outlier_zs(df, hold=1):
        for i in df.columns:
            mean = df[i].mean()
            std = df[i].std()
            z_score = (df[i] - mean) / std
            mask = z_score.abs() > hold
            print(f"z - {i}의 이상치 개수 : {z_score[mask].count()}")

    def fill_outliers_zs(sr, hold, fill_value):

        valid_value = ["mean", "median"]
        if fill_value not in valid_value:
            raise ValueError(f"score_standard must be one of {valid_value}")

        mean = sr.mean()
        std = sr.std()
        z_score = (sr - mean) / std
        mask = z_score.abs() <= hold

        sr_copy = sr.copy()

        if fill_value == "mean":
            sr_copy[mask] = sr_copy.mean()
        elif fill_value == "median":
            sr_copy[mask] = sr_copy.median()

        return sr_copy

    def find_outlier_iqr(df, threshold=1.5):
        for i in df.columns:
            q1 = df[i].quantile(0.25)
            q3 = df[i].quantile(0.75)
            iqr = q3 - q1

            lower = q1 - iqr * threshold
            upper = q3 + iqr * threshold

            print(
                f"iqr - {i}의 이상치 개수 : {df[(df[i] < lower)&(df[i] > upper)].count()}"
            )

    def fill_outliers_iqr(sr, threshold, fill_value):

        valid_value = ["mean", "median"]
        if fill_value not in valid_value:
            raise ValueError(f"score_standard must be one of {valid_value}")

        q1 = sr.quantile(0.25)
        q3 = sr.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - iqr
        upper = q3 + iqr

        sr_copy = sr.copy()

        if fill_value == "mean":
            sr_copy[(sr_copy < lower) & (sr_copy > upper)] = sr_copy.mean()
        elif fill_value == "median":
            sr_copy[(sr_copy < lower) & (sr_copy > upper)] = sr_copy.median()

        return sr_copy

    def find_random_state(featureDF, targetSR):
        # 최적 random_state 값
        random_state_list = []
        for i in range(1, 51):
            xtrain, xtest, ytrain, ytest = train_test_split(
                featureDF, targetSR, test_size=0.2, random_state=i
            )
            scaler = StandardScaler()  # scaler 종류에 따른 큰 차이 없음
            scaler.fit(xtrain)
            xtrain_scaled = scaler.transform(xtrain)
            xtest_scaled = scaler.transform(xtest)
            model = LinearRegression()  # model 종류에 따라 차이남
            model.fit(xtrain_scaled, ytrain)
            model.score(xtest_scaled, ytest)
            random_state_list.append(model.score(xtest_scaled, ytest))
        max_score = max(random_state_list)
        print(
            f"radom_state = {random_state_list.index(max_score)+1}\nscore : {max_score}"
        )

        max_random_state = random_state_list.index(max_score) + 1
        return max_random_state

    def find_maxK_re(xtrain, ytrain, xtest, ytest):
        max_k = xtrain.shape[0]
        test_scoreList = []
        train_scoreList = []

        for k in range(1, max_k + 1):
            knn_model = KNeighborsRegressor(n_neighbors=k)
            knn_model.fit(xtrain, ytrain)
            train_scoreList.append(knn_model.score(xtrain, ytrain))
            test_scoreList.append(knn_model.score(xtest, ytest))
        max_idx = test_scoreList.index(max(test_scoreList)) + 1
        K = max_idx
        return K

    def find_maxK_cl(xtrain, ytrain, xtest, ytest):
        max_k = xtrain.shape[0]
        test_scoreList = []
        train_scoreList = []

        for k in range(1, max_k + 1):
            knn_model = KNeighborsClassifier(n_neighbors=k)
            knn_model.fit(xtrain, ytrain)
            train_scoreList.append(knn_model.score(xtrain, ytrain))
            test_scoreList.append(knn_model.score(xtest, ytest))
        max_idx = test_scoreList.index(max(test_scoreList)) + 1
        K = max_idx
        return K

    def find_re_model(xtrain, ytrain, xtest, ytest, score_standard):

        valid_scores = ["r2", "mae", "mse", "rmse"]
        if score_standard not in valid_scores:
            raise ValueError(f"score_standard must be one of {valid_scores}")

        models = [KNeighborsRegressor(), LinearRegression(), Ridge(), Lasso()]
        scalers = [StandardScaler(), MinMaxScaler(), RobustScaler()]

        acDict = {}
        model_score = {
            "model": [],
            "scaler": [],
            "train_score": [],
            "test_score": [],
            "r2": [],
            "mae": [],
            "mse": [],
            "rmse": [],
        }

        for scaler in scalers:
            scaler.fit(xtrain)
            scaled_xtrain = scaler.transform(xtrain)
            scaled_xtest = scaler.transform(xtest)

            for model in models:
                if isinstance(model, KNeighborsRegressor):
                    print("----------------탐색중------------------")
                    max_k = xtrain.shape[0]
                    test_scoreList = []
                    train_scoreList = []

                    for k in range(1, max_k + 1):
                        knn_model = KNeighborsRegressor(n_neighbors=k)
                        knn_model.fit(xtrain, ytrain)
                        train_scoreList.append(knn_model.score(xtrain, ytrain))
                        test_scoreList.append(knn_model.score(xtest, ytest))
                    max_idx = test_scoreList.index(max(test_scoreList)) + 1
                    K = max_idx
                    model = KNeighborsRegressor(n_neighbors=K)
                elif isinstance(model, Ridge):
                    alphas = np.arange(0.1, 30.0, 0.1).tolist()
                    scorelist = [[], []]
                    for a in alphas:
                        model = Ridge(alpha=a, max_iter=30000)

                        model.fit(xtrain, ytrain)

                        scorelist[0].append(model.score(xtrain, ytrain))
                        scorelist[1].append(model.score(xtest, ytest))
                    best_alpha = alphas[scorelist[1].index(max(scorelist[1]))]
                    model = Ridge(alpha=best_alpha, max_iter=30000)
                elif isinstance(model, Lasso):
                    alphas = np.arange(0.1, 30.0, 0.1).tolist()
                    scorelist = [[], []]
                    for a in alphas:
                        model = Lasso(alpha=a, max_iter=30000)

                        model.fit(xtrain, ytrain)

                        scorelist[0].append(model.score(xtrain, ytrain))
                        scorelist[1].append(model.score(xtest, ytest))
                    best_alpha = alphas[scorelist[1].index(max(scorelist[1]))]
                    model = Lasso(alpha=best_alpha, max_iter=30000)

                # KNN,Ridge,Laaso 모델이 아닐 때, 바로 아래 코드 수행
                model.fit(scaled_xtrain, ytrain)
                print(f"model : {model}")

                train_score = model.score(scaled_xtrain, ytrain)
                test_score = model.score(scaled_xtest, ytest)
                print(
                    f"scaler : {scaler}\nTrain score : {train_score}\nTest score : {test_score}"
                )

                y_pre = model.predict(scaled_xtest)
                r2 = r2_score(ytest, y_pre)
                mse = mean_squared_error(ytest, y_pre)
                mae = mean_absolute_error(ytest, y_pre)
                rmse = mean_squared_error(ytest, y_pre, squared=False)
                print(
                    f"""
        [모델 설명도]\nR2 : {r2}\n[에러]\nMAE : {mae}\nMSE : {mse}\nRMSE : {rmse}\n--------------------------------------
        """
                )

                acDict[(model, scaler)] = [train_score, test_score, r2, mae, mse, rmse]

                model_score["model"].append(model)
                model_score["scaler"].append(scaler)
                model_score["train_score"].append(train_score)
                model_score["test_score"].append(test_score)
                model_score["r2"].append(r2)
                model_score["mae"].append(mae)
                model_score["mse"].append(mse)
                model_score["rmse"].append(rmse)

        if score_standard == "r2":
            max_ac = max(acDict, key=lambda k: acDict[k][2])
        elif score_standard == "mae":
            max_ac = min(acDict, key=lambda k: acDict[k][3])
        elif score_standard == "mse":
            max_ac = min(acDict, key=lambda k: acDict[k][4])
        elif score_standard == "rmse":
            max_ac = min(acDict, key=lambda k: acDict[k][5])
        else:
            pass

        print(
            f"[최적의 모델] :{max_ac}\nTrain score : {acDict[max_ac][0]}\nTest score : {acDict[max_ac][1]} \nR2 : {acDict[max_ac][2]}"
            f"\nMAE : {acDict[max_ac][3]}\nMSE : {acDict[max_ac][4]}\nRMSE : {acDict[max_ac][5]}"
        )
        return model_score

    def find_scaler(xtrain, ytrain, xtest, ytest, model):
        scalers = [StandardScaler(), MinMaxScaler(), RobustScaler()]

        train_scores = []
        test_scores = []
        for scaler in scalers:
            scaler.fit(xtrain)
            scaled_xtrain = scaler.transform(xtrain)
            scaled_xtest = scaler.transform(xtest)

            model.fit(scaled_xtrain, ytrain)
            print(f"model : {model}")

            train_score = model.score(scaled_xtrain, ytrain)
            test_score = model.score(scaled_xtest, ytest)
            train_scores.append(train_score)
            test_scores.append(test_score)
            print(
                f"scaler : {scaler}\nTrain score : {train_score}\nTest score : {test_score}"
            )

            y_pre = model.predict(scaled_xtest)
            r2 = r2_score(ytest, y_pre)
            mse = mean_squared_error(ytest, y_pre)
            mae = mean_absolute_error(ytest, y_pre)
            rmse = mean_squared_error(ytest, y_pre, squared=False)
            print(
                f"""
    [모델 설명도]\nR2 : {r2}\n[에러]\nMAE : {mae}\nMSE : {mse}\nRMSE : {rmse}\n\n--------------------------------------
    """
            )

    def find_poly_p(xtrain, ytrain, xtest, ytest):
        # poly 최적의 파라미터 값 찾기
        max_score = []
        for b in [True, False]:
            for d in range(1, 6):
                poly = PolynomialFeatures(interaction_only=b, degree=d)
                poly.fit(xtrain)
                xtrain_transformed = poly.transform(xtrain)
                xtest_transformed = poly.transform(xtest)

                model = LinearRegression()
                model.fit(xtrain_transformed, ytrain)
                score = model.score(xtest_transformed, ytest)
                print(b, d, score)
                max_score.append([b, d, score])

        max_element = max(max_score, key=lambda x: x[2])

        b_max, d_max, score_max = max_element[0], max_element[1], max_element[2]

        print(
            f"max score =>\ninteraction_only = {b_max}, degree = {d_max}, score = {score_max}"
        )
        return b_max, d_max

    def find_alpha(xtrain, ytrain, xtest, ytest):
        alphas = np.arange(0.1, 30.0, 0.1).tolist()
        scorelist = [[], []]
        for a in alphas:
            model = Ridge(alpha=a, max_iter=30000)

            model.fit(xtrain, ytrain)

            scorelist[0].append(model.score(xtrain, ytrain))
            scorelist[1].append(model.score(xtest, ytest))
        best_alpha = alphas[scorelist[1].index(max(scorelist[1]))]
        return best_alpha

    def print_alpha_plot(alphas, best_alpha, scorelist):
        plt.plot(alphas, scorelist[0], label="Train")
        plt.plot(alphas, scorelist[1], label="Test")
        plt.axvline(
            best_alpha, color="red", linestyle=":", label=f"alpha ={best_alpha}"
        )
        plt.text(best_alpha + 1, 0.984, f"Best_alpha ={best_alpha}")
        plt.legend()
        plt.title("[Train & Test]")


# 반장꺼 훔쳐오기 헤헤
# 1. 전처리 :
#                  1.1 이상값 제거(box-plot, or Z-score)
#                  1.2 중복값 제거
#                            import scipy.stats as stats
#                            from sklearn.preprocessing import LabelEncoder
#                  1.3 훈련/검증 데이터 셋 생성
#                            from sklearn.model_selection import train_test_split
#                  1.4 데이터 정규화
#                            from sklearn.preprocessing import StandardScaler
#                            from sklearn.preprocessing import MinMaxScaler
#                            from sklearn.preprocessing import RobustScaler
#                            from sklearn.preprocessing import SplineTransformer
#                            from sklearn.preprocessing import QuantileTransformer

# 1.5 feature 결정 :
#                  1.6 컬럼 추가 생성
#                            from sklearn.preprocessing import PolynomialFeatures
#                  1.7 ols 분석 + 상관계수 + 데이터 분포 시각화로 feature 결정
#                            import statsmodels.formula.api as smf

# 2. 모델링 :

#                  2.1 회귀분석 시행(Classifier)
#                            from sklearn.neighbors import KNeighborsClassifier
#                  2.1 회귀분석 시행(Regressor)
#                            from sklearn.ensemble import RandomForestRegressor
#                            from sklearn.svm import SVR
#                            from sklearn.linear_model import LogisticRegression
#                            from sklearn.neighbors import KNeighborsRegressor
#                            from sklearn.linear_model import LinearRegression
#                  2.2 우리는 울지 않는 부엉이오...OvO
#                            from sklearn.multiclass import OneVsRestClassifier
#                            from sklearn.multiclass import OneVsOneClassifier


# 3. 지표 평가 :
#                  3.1 오차 평가 지표
#                            from sklearn.metrics import mean_squared_error
#                            from sklearn.metrics import mean_absolute_error
#                            from sklearn.metrics import r2_score
#                  3.2 재현율, 정밀도 관련 지표
#                            from sklearn.metrics import accuracy_score
#                            from sklearn.metrics import precision_score
#                            from sklearn.metrics import recall_score
#                            from sklearn.metrics import f1_score
#                  3.3 전체 지표
#                            from sklearn.metrics import confusion_matrix
#                            from sklearn.metrics import classification_report

# # 4. 튜닝   : 제일 성능이 높게 나온 모델 2개에 한해서,
#                 param의 값을 바꿔가면서 지표 평가

# # 5. 결과 시각화 :
#                 성능을 대표할 만한 지표 3개를 뽑아 시각화(train score, test score, ?)
