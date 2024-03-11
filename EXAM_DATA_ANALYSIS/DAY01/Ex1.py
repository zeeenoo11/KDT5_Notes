# --------------- 1. Open csv :'r' ----------------------
# csv 파일 함수
import csv
"""
f = open('Daegu_utf8.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter=',')
print(data)
f.close()
"""

# -------- 2. print each csv line one by one ------------
"""
f = open('Daegu_utf8.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter=',')
count = 0
for	row	in data:
    if count > 5:
        break
    else: 
        print(row)
        count += 1
f.close()
"""
# ------------ 3. Save new file replaced '\t' --------------
"""
#
fin = open('DATA/daegu.csv', 'r', encoding='utf-8-sig')
data = csv.reader(fin, delimiter=',')
# delimiter= : 

fout = open('DATA/daegu-utf8.csv', 'w', newline='', encoding='utf-8-sig')
# newline= : 한 라인 씩 건너뛰는 것을 방지
wr = csv.writer(fout)

for row in data:
    for i in range(len(row)):
        row[i] = row[i].replace('\t', '')
    print(row)
    wr.writerow(row)

fin.close()
fout.close()
print('파일 저장 완료')
"""

# --------------- 4. 데이터 헤더 출력하기 ----------------
# 사실 필요한 건 데이터, 헤더를 따로 출력하기 위함
#   - next( ) : 첫 데이터행 반환; 탐색 위치를 다음 행으로
#   - header = next(data)
"""
f = open('DATA/daegu-utf8.csv', 'r', encoding='utf-8-sig')

data = csv.reader(f, delimiter=',')
header = next(data)
print(header)
f.close()
"""

# -------- 예제1 : 최고 최저 기온 구하기 -----------------
# def main() 사용: open() -> csv.reader

def get_minmax_temp(data):
    header = next(data)

    min_temp = 100
    min_date = ''

    max_temp = -999
    max_date = ''

    for row in data:
        if row[3] == '':
            row[3] = 100
        row[3] = float(row[3])

        if row[4] == '':
            row[4] = -999
        row[4] = float(row[4])

        if row[3] < min_temp:
            min_temp = row[3]
            min_date = row[0]

        if row[4] > max_temp:
            max_temp = row[4]
            max_date = row[0]

    print('-'*50)
    print(f'대구 최저 기온: {min_date} - {min_temp}\'C')
    print(f'대구 최고 기온: {max_date} - {max_temp}\'C')

def main():
    f = open('DATA/daegu-utf8.csv', 'r', encoding='utf-8-sig')
    data = csv.reader(f)
    get_minmax_temp(data)
    f.close()

main()