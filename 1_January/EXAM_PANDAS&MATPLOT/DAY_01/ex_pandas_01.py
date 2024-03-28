# ----------------------------------------
# 판다스 설치 확인 및 버전 체크
# ----------------------------------------
import pandas as pd

print(pd.__version__) # 버전 확인; 2.0.3

# 데이터 파일 읽기: '../ 로 시작하면 폴더가 뜬다
# 상대 경로 : 현재 파일을 기준으로 경로를 설정
filename = '../DATA/used_cars.csv'

data = pd.read_csv(filename)
print(type(data))  # <class 'pandas.core.frame.DataFrame'>
print(data) 