import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser  import parser_functions as parse
import pandas as pd
import pymysql
import random
import re

print('\n========================= <4장 데이터 저장> ============================')
# 데이터를 csv에 저장
# -> test.csv
# [ 사용 함수 ]
# csvfile = open(); 없으면 만들어줌 (꼭 .close())
# .writerow() : 한 라인씩 csv 파일에 저장
# .writerows() : 여러 라인 한번에 저장
# ------------------------------------------------------------------------
csvfile = open('DATA/test.csv', 'w', encoding='utf-8')
try:
    writer = csv.writer(csvfile)
    # .writerow : 한 라인씩 csv 파일에 저장
    writer.writerow(('number', 'number+2', '(number+2)^2'))

    for i in range(10):
        writer.writerow((i, i+2, (i+2)**2))
except Exception as e:
    print(e)
finally:
    csvfile.close()


print('\n------------ [ 웹의 테이블 데이터를 csv로 저장 ] ----------------')
# https://en.wikipedia.org/wiki/Comparison_of_text_editors
# table = ~~~.find_all('table', {'class': 'wikitable'})[0]
# rows = table.find_all('tr')
# --------------------------------------------------------

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')
# 두 개의 테이블 중 첫 번째 테이블 사용
table = bs.find_all('table', {'class': 'wikitable'})[0]
rows = table.find_all('tr')

csvfile = open('DATA/editor.csv', 'wt', encoding='utf-8') # t: text mode
writer = csv.writer(csvfile)

try:
    for row in rows:
        csvRow = []
        for cell in row.find_all(['th', 'td']):
            print(cell.text.split())
            csvRow.append(cell.text.strip())
        writer.writerow(csvRow)
finally:
    csvfile.close()

# 이러면 이중 컬럼이 반영되지 않는다.

print('\n[ html_table_parser 사용 ] ==========================================')
# 새로운 라이브러리: anaconda > pip install html_table_parser
# html > 2d list > pandas_DF > file.csv
# .make2d(table) 하면 끝

# [ 예제1 ]
# 위와 동일한 html 사용
table = bs.find('table', {'class': 'wikitable'})
# 또는 table = bs.find_all('table', {'class': 'wikitable'})[0]
# -> find_all 에선 [0] 필요
table_data = parse.make2d(table)    # 라이브러리 사용 구문

# 두 행만 출력
print('[0]:', table_data[0])
print('[1]:', table_data[1])

# [ 예제2 ] ---------------------------------------------------------
df = pd.DataFrame(table_data[2:], columns=table_data[1])
print(df.head())

# csv 파일로 저장
csvFile = open('DATA/editors1.csv', 'w', encoding='utf-8')
writer = csv.writer(csvFile)

for row in  table_data:
    writer.writerow(row)

csvFile.close()
# -------------------------------------------------------------------

print('\n[ 새로운 데이터 베이스 생성 ] ====================================')
# Database; SQL로 접근
print(""" SQL문 내
create database scraping;

use scraping; # 새 데이터 베이스 생성

create table pages (
    id BIGINT not null auto_increment,
    title VARCHAR(200),
    content VARCHAR(10000),
    created TIMESTAMP default CURRENT_TIMESTAMP, # 현재 시간 자동 입력
    primary key(id)
);

desc pages;
# Test1
insert into pages(title, content)
value(
    "Test page title",
     "This is some test page content. It can be up to 10,000 characters long.");

select * from pages;
# Test2
insert into pages(title, content)
values(
       "Second page title",
       "This is the second test page content"
      );
""")

# [ like 검색 조건 ]
# select * from table where 위치 like 조건2
# %test% :

print('\n [ 파이썬과 통합하기 ] =======================================================')
print('\n[데이터베이스 접근 테스트]')
conn = pymysql.connect(host='localhost', user='root', password='1234', db='scraping', charset='utf8')
cur = conn.cursor()

cur.execute('use scraping')
cur.execute('select * from pages where id=2')

print(cur.fetchone())
cur.close()
conn.close()

print('\n[ 데이터베이스와 접근하기 ]')
# def store( title, content ) : title과 content를 pages 에 저장하는 함수
# def getLinks( atrticleUrl ) : 입력된 주소에서 title과 content를 저장
#                               title : <h1>, content : <div> id='bodyContent'
#
conn = pymysql.connect(host='localhost', user='root', password='1234', db='scraping', charset='utf8')
cur = conn.cursor()
random.seed(None)

def store(title, content):
    # pages에 store()한 값을 입력
    cur.execute('Insert into pages (title, content) values("%s","%s"), (title, content)')
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org' + articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').text
    content =  bs.find('div', {'id':'mw-content-text'}).find('p').text
    store(title, content)
    return (bs.find('div', {'id':'bodyContent'})
            .findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')))

links = getLinks('/wiki/Kevin_Bacon')
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()


print(cur.fetchone())
cur.close()
conn.close()