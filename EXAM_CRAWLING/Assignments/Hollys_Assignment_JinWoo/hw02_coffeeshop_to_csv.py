from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import csv

# --------------------- < 커피 매장 찾기 > ----------------------
# 1. 매장 찾기에서 1~51 페이지까지 모든 매장의 정보를 스크레이핑
#   - 지역, 매장명, 매장 주소, 전화번호
#   - 수집된 정보는 csv 파일로 저장
#   - csv에 저장하는 파일: 현재 파일
#   - csv : hollys_branches.csv (utf-8)
# 2. 저장된 csv 파일을 읽어 사용자가 입력한 지역에 있는 매장 정보 출력
#   - 파일 : hw02_find_coffeeshop.py
# ---------------------------------------------------------------

# 1) url 확인
html_1 = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=1&sido=&gugun=&store='

# 2) 데이터 스크레이핑 문
store_data = []; count = 0
for i in range(1, 52):
    # 2-1) 페이지 1부터 51까지 url 따로 지정
    url = urlopen(f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store=")
    soup_ = BeautifulSoup(url, 'html.parser')
    # 2-2) 페이지 내 데이터 스크래핑
    store_info_list = soup_.select('table.tb_store > tbody > tr > td')
    for j in range(len(store_info_list)//6):
        # 각 매장의 정보 저장
        store_name = store_info_list[j*6+1].text
        store_location = store_info_list[j*6].text
        store_addr = store_info_list[j*6+3].text
        store_tel = store_info_list[j*6+5].text
        store_data.append([store_name, store_location, store_addr, store_tel])
        count += 1
        print(f'[{count:3d}]:', end=' ')
        print(f'매장이름: {store_name},', end=' ')
        print(f'지역: {store_location},', end=' ')
        print(f'주소: {store_addr},', end=' ')
        print(f'전화번호: {store_tel}')
print('전체 매장 수:', count)


# 3) 데이터 저장 (DataFrame > to_csv)
columns = ['매장 이름', '위치(시,구)', '주소', '전화번호']
df = pd.DataFrame(store_data, columns=columns).set_index('매장 이름')
# print(df)
print('hollys_branches.csv 파일 저장 완료')
# .to_csv
df.to_csv('hollys_branches.csv', encoding='utf-8-sig', mode='w', index=True)


# [ 테스트용 ]
# url 확인
# html_1 = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=1&sido=&gugun=&store='
# html_2 = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=2&sido=&gugun=&store='
# pageNo= 뒤 숫자 한 자리만 다름
# if 0 : # test
#     store_info_list = soup.select('table.tb_store > tbody > tr > td')
#     print(store_info_list)
#     store_data = []
#     for i in range(len(store_info_list)//6):
#         # print(store_info_list[i*6+1].text)
#         # print(store_info_list[i*6].text)
#         # print(store_info_list[i*6+3].text)
#         # print(store_info_list[i*6+5].text)
#         store_data.append([store_info_list[i*6+1].text, store_info_list[i*6].text,
#                           store_info_list[i*6+3].text, store_info_list[i*6+5].text])
#
#     for i in range(len(store_data)):
#         print(store_data[i])