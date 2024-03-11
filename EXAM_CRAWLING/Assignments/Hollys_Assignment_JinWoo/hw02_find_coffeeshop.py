import pandas as pd

# <과제 파일2>
# : 저장된 csv 파일을 읽어 사용자가 입력한 지역에 있는 매장 정보 출력
#   주소, 전화번호 출력
#   quit 입력 시 종료
# --------------------------------------------------------
# 파일 불러오기
csvDf = pd.read_csv('hollys_branches.csv', header=0, encoding ='utf-8-sig')
# print(csvDf)

while True:
    city = input("검색할 매장의 도시를 입력하세요: ")
    if city == 'quit':     # 1) 'quit' 입력 시 종료
        break
    else:   # 2) 입력 값으로 매장 검색
        # 2-1) 매장 검색
        result = csvDf[csvDf['위치(시,구)'].str.contains(city)]
        # print(result)
        result_lists = []
        for i in range(len(result)):    # 리스트화하여 입력
            result_list = []
            result_list.append(result.iloc[i][2])   # 주소
            result_list.append(result.iloc[i][3])   # 전화번호
            result_lists.append(result_list)
        # print(result_lists)

        # 2-2) 출력
        print('-'*30)
        print('검색된 매장 수: ', len(result))
        print('-'*30)
        for i in range(len(result)):
            print(f'[{i+1:3d}]: ', result_lists[i])
        print('-'*70)
print('종료합니다.')
