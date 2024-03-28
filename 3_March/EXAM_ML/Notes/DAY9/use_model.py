# Load Module
from joblib import load

# 전연 변수
model_file = "../models/iris_dt_best_model.pkl"

# 2) Load Model
model = load("../models/iris_dt_best_model.pkl")

# print(model.classes_)   # ['setosa' 'versicolor' 'virginica']

# Input info of Iris => 4 features
datas = input(
    "Please Enter information of iris (ex: 꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비) : "
)
if len(datas):
    datas_list = list(map(int, datas.split(",")))
    print(datas_list)

    # Show matched data with input' one : predict(2D)
    pred = model.predict([datas_list])
    pred_prob = model.predict_proba([datas_list])

    print("The species of iris is", pred[0], f"with {max(pred_prob[0])*100:.1f}% probability.")
else:
    print("No input data.")
