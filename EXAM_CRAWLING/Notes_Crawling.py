print('============== < 1장 크롤링 개념 > ====================')
# (준비)
# - 'beautifulsoup' 설치 확인
# - anaconda > conda list beautifulsoup

# [ Crawling vs Scraping ] -------------------------------
# 1. Crawling
#   - 웹 페이지에서 필요한 데이터를 추출
#   - 데이터 수집한다는 뜻에 치중
#   - 크롤러 : 자동 정보 수집 프로그램
#
# 2. Scraping
#   - 수집한 정보를 분석해 필요한 정보를 추출
#   - 웹 크롤러로 다운 받음
# --------------------------------------------------------

print('\n\n[ .urlopen(url) ] : 웹 페이지 가져오기 -------')
# - urllib.request.urlopen(url)
# - 주소를 입력하면 해당 페이지의 HTML 코드를 반환

# [ .read() ] : HTML 콘텐츠를 읽음
# - HTTPResponse.read()
from urllib.request import urlopen

html = urlopen("https://www.naver.com")  #
print(type(html))  # <class 'http.client.HTTPResponse'>
print(html.read())
# --------------------------------------------------------

print('\n\n[ BeautifulSoup 객체 구조 ] -------------------')
# - html은 짝으로 이루어진 태그 내에 내용이 있음
#   <body> <title> aaaa </title> <b1> oooo </b1> </body>
# - 내가 필요한 건 태그 내부의 텍스트 값

from bs4 import BeautifulSoup   # 라이브러리 호출

html = urlopen("https://www.naver.com")
bs = BeautifulSoup(html.read(), "html.parser")
# html.read() : 전체 HTML 코드를 가짐
# html.parser : 분석 툴

                                    # 결과:
print('bs: ', bs)                   # <!DOCTYPE html> ... 모든 내용
# .h1 : <h1> 태그만 반환
print('bs.h1: ', bs.h1)             # <h1 class="search_logo" id="special-input-logo"></h1>
# .string : 태그 내부의 문자열만 가져오기
print('bs.string: ', bs.h1.string)  # None
print(bs.title)                     # <title>NAVER</title>
print('title: ', bs.title.string)   # NAVER
# --------------------------------------------------------

print('[ 예외 처리 ] -------------------------------------')
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://www.pythonscraping.com/pages/error.html')
except HTTPError as e:
    print(e)  # 이 오류가 반환
except URLError as e:
    print('The	server could not be found!')
else:
    print('It worked!')
# --------------------------------------------------------


print('[ 존재하지 않는 태그 접근 ] -----------------------')
# - None 반환, AttributeError 발생
def get_Title(url, tag):
    try:    # urlopen 오류 확인
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:    # 검색하는 tag 유무 에러 확인
        bsObj = BeautifulSoup(html.read(), "html.parser")
        value = bsObj.body.find(tag)
        # 입력된 tag 찾기 (최종 반환값)
    except AttributeError as e:
        return None
    # AttributeError -> return None
    return value


tag = 'h2'  # 검색할 태그
value = get_Title('http://www.pythonscraping.com/pages/page1.html', tag)
if value is None:
    print(f'{tag} could not be found')   # h2 could not be found
else:
    print(value)
# ------------------------------------------------------------

print('[ urllib.request와 requests의 차이 ] ------------------')
# [ .request ] urllib.request
# - 기본 파이썬 패키지
# - 바이너리로 저장, 없으면 에러

# [requests]
# - 추가 설치 필요 (conda install requests)
# - 없어도 에러 없이 동작
import requests

url = 'http://www.pythonscraping.com/pages/page1.html'
# url =	'http://finance.naver.com'
# url =	'http://www.naver.com’

html = requests.get(url)
print('html.encoding:', html.encoding)
print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
print()
print('h1.string:', soup.h1.string)
# ------------------------------------------------------------
# [ HTML 기본 구조 ]

# <!DOCTYPE	html>                   # 문서 형식 선언
# <html>                            # 짝을 이룬 태그
#     <head>
#         <meta charset='utf-8>
#         <title>A	Useful	Page</title>
#     </head>
#     <body>
#         <h1> 글자 제목1 </h1>     # 제목 크기 설정 1~6
# <div>

# [ 태그 구성 ]
#   : <태그 속성="속성값"> 내용  </태그>
# Ex) <span class="red"> 빨간색 글자 </span>

# [ 고급 HTML 분석 : CSS 스타일 ]
# class와 id 속성 사용
# id    : #id{ 속성1:속성값; 속성2:속성값; }
# class : .className{ 속성1:속성값; 속성2:속성값; }

file = 'DATA/h1~6_test.html'
# --------- 자세한 내용 관련은 html 파일에 필기 --------------

# [ urllib.request.Request 클래스 ]
# class urllib.request.Request(url, data=None, headers={},
# origin_req_host=None, unverifiable=False, method=None)

print('[ 멜론 웹사이트 접근 ] ------------------------------')

melon_url =	'https://www.melon.com/chart/index.htm'

"""
# melon 접근: 유저 정보 없이는 어렵다.

html = urlopen(melon_url)
soup = BeautifulSoup(html.read(), 'html.parser')
print(soup)
"""

# Error 406 Not Acceptable : 사람이 아닌 프로그램이라 인식해 크롤링 막음
# User Agent 정보 필요

from urllib.request import Request

# [ Request로 유저 정보 추가 ]
urlrequest = Request(melon_url, headers={'User-Agent':'Mozilla/5.0'})

html = urlopen(urlrequest)
soup = BeautifulSoup(html.read().decode('utf-8'), 'html.parser')
print(soup)
# ----------------------------------------------------------
html_example = '''
 <!DOCTYPE   html>
 <html   lang="en">
 <head>
     <meta   charset="UTF-8">
     <meta   name="viewport"   content="width=device-width,   initial-scale=1.0">
     <title>BeautifulSoup   활용</title>
 </head>
 <body>
     <h1   id="heading">Heading   1</h1>
     <p>Paragraph</p>
     <span   class="red">BeautifulSoup   Library   Examples!</span>
     <div   id="link">
         <a   class="external_link"   href="www.google.com">google</a>
         <div   id="class1">
             <p   id="first">class1's   first   paragraph</p>
             <a   class="external_link"   href="www.naver.com">naver</a>
             <p   id="second">class1's   second   paragraph</p>
             <a   class="internal_link"   href="/pages/page1.html">Page1</a>
             <p   id="third">class1's   third   paragraph</p>
         </div>
     </div>
     <div   id="text_id2">
     Example   page
     <p>g</p>
     </div>
     <h1   id="footer">Footer</h1>
 </body>
 </html>
 '''





print('\n\n============ < 2장 BeautifulSoup 활용 > ==============')
# [ BeautifulSoup 라이브러리 ]
# - HTML과 XML 분석 위함
# - 객체 생성법 : soup =  BeautifulSoup(html_example, "html.parser")
# - html_example : 분석할 문서
# - html.parser(기본값) : 구문 분석기
# -----------------------------------------------------------

print('[ 예제 ] ---------------------------------------------')
html = urlopen("https://www.daangn.com/hot_articles")
bs = BeautifulSoup(html.read(), "html.parser")

print(bs.h1)
# => 공백 너무 많음: <h1 class="head-title" id="hot-articles-head-title">
print(bs.h1.string.strip())
# => 중고거래 인기매물

# [ .태그명 ]
print(bs.title)
# => <title>당근 중고거래 | 당신 근처의 당근</title>
print(bs.title.string)
# => 당근 중고거래 | 당신 근처의 당근
print(bs.title.get_text())  # .string과 동일 기능
# => 당근 중고거래 | 당신 근처의 당근

# [ .태그명.parent ]
# : 해당 태그를 포함하고 있는 부모
print(bs.title.parent)
# => <head> 부터 </head> 까지 나옴
# ---------------------------------------------------------

# [ <a> 태그 접근 ]
# : '첫 번째' <a> 태그 요소 접근
# <a> 태그 :

print(bs.a)
# < a class ="_1knjz492" href="https://www.daangn.com" > 부터
# </a> 까지
# href= :
print(bs.a.string)
# => None
print(bs.a['href'])  # href 속성의 url을 추출
# => https://www.daangn.com
print(bs.a.get('href'))  # 동일 기능
# => https://www.daangn.com

print('\n[ find( ) ] ---------------------------------------')
# find( tag,

# [ find( tagName , attributes ) ]
# : 태그 중 특정 태그 찾기

# file = 'DATA/chap02.html'   # 얘는 왜 안되지
soup = BeautifulSoup(html_example,'html.parser')

print(soup.find('div', {'id': 'text_id2'}))

div_text = soup.find('div', {'id': 'text_id2'})
print(div_text.text)

print(div_text.string)


print('\n[ find( a ) ] --------------------------------------')
# - <a> 중 class 속성값이 "intenal_link" 인 정보 추출

# 아래 둘 다 같은 의미 : 딕셔너리 or class_
href_link_dict = soup.find('a', {'class': 'internal_link'})
href_link = soup.find('a', class_='internal_link')
# class는 예약어라 class_ 사용
# class_ : list 타입

print(href_link)
print(href_link['href'])
print(href_link.get('href'))
print(href_link.text)

print('\n[ .attrs ] -----------------------------------------')
# : 모든 속성 가져오기
print('href_link.attrs:	', href_link.attrs)
print('class 속성값: ', href_link['class'])
# print

print('\n[ find( ) 활용하기 ] --------------------------------')
print('\n[ 1. 속성 검색 ]')
#   : href 속성의 값이 'www.google.com'인 항목 검색

href_value_no_a = soup.find(attrs={'href': 'www.google.com'})
# 'a' 태그 지정 없이도 작동 ('a'에만 href 있음)
href_value = soup.find('a', attrs={'href': 'www.google.com'})

print('href_value: ', href_value)
# href_value: <a ="" class="external_link" href="www.google.com">google</a>
print(href_value['href'])
# www.google.com
print(href_value.string)
# google

print('\n[ 2. 속성 가져오기 ]')
# span 태그의 속성 가져오기
span_tag = soup.find('span')

print('span	tag:', span_tag)
# => <span class="red">BeautifulSoup Library Examples!</span>
print('attrs:', span_tag.attrs)
# => {'class': ['red']}
print('value:', span_tag.attrs['class'])
# => ['red']
print('text:', span_tag.string)
# => BeautifulSoup Library Examples!

print('\n[ 3. class 속성 ]')
#   : class 속성은 여러 개의 값을 가질 수 있음 (multi values)
href_link = soup.find('a', class_='internal_link')
print('class 속성값: ', href_link['class'])
# => ['internal_link']
# find()에서 class_= 해도 href_link['class'] 에선 _ 없이 검색

tr = '''
<table>
    <tr class="passed a b c" id="row1 example"><td>t1</td></tr>
    <tr class="failed" id="row2"><td>t2</td></tr>
</table>'''

table = BeautifulSoup(tr, 'html.parser')
for row in table.find_all('tr'):
    print(row.attrs)
# {'class': ['passed', 'a', 'b', 'c'], 'id': 'row1 example'}
# {'class': ['failed'], 'id': 'row2'}
# ---------------------------------------------------------

print('\n\n[ find_all( ) ] --------------------------------')
# find_all( tag, attrs, recursive, text, limit, keywords )

print('\n[ 태그 검색 ]')
print('1. 모든 div 태그 검색')

div_tags = soup.find_all('div')
print('div_tags length: ', len(div_tags))
#  div_tags length:  3

for div in div_tags:
    print('-'*50)
    print(div)
# div 태그가 하나씩 출력
# <div id="link"> ~ </div>
# <div id="class1"> ~  </div>
# <div id="text_id2"> ~ </div>

print('\n2. 모든 a 태그 검색')
links = soup.find_all('a')
for	alink in links:
    print(alink)
    print(f"url:{alink['href']}, text: {alink.string}")
    print('-'*50)
# 3가지 출력 : <a class="external_link" href="www.google.com">google</a>
# 의미하는 것 :

print('\n[ 특정 태그 중 여러 속성값 검색 ] ----------------')
# : 리스트 형태로 추가
link_tags = soup.find_all(name='a', attrs={'class': ['external_link', 'internal_link']})
print(link_tags)
# google, Page1 이 포함된 a 태그문 출력
# naver는 왜 없지? -> 파일 오류,, 복붙 잘못

p_tags = soup.find_all('p', {'id': ['first', 'third']})
for p in p_tags:
    print(p)
# <p id="first">class1's first paragraph</p>
# <p id="third">class1's third paragraph</p>

print('\n\n================ [ select ] ====================')
print('[ select( ) ]')
#  :

# [ select 사용법 ]
# : select( selector, namespaces=None, limit=None, **kwargs )

# select(tag)
# select(tag#id)
# select(tag.class) or (.class)
# select( '상위태그 > 하위태그1 > 하위태그2' )
# select(tag[ attr1 = value1 ])

print('\n[ select_one( ) ----------------------------------')
# : 첫 번째 일치하는 태그만 반환

print('[ <head> 태그 검색 ]')
head = soup.select_one('head')
print(head)
#  <head> ~ </head>
print('head.text: ', head.text.strip())
# BeautifulSoup   활용

print('\n[ 첫 번째 h1 태그 검색 ]')
h1 = soup.select_one('h1')
print(h1)
# <h1 id="heading">Heading   1</h1>

print('\n[ <h1> 태그의 id 검색 ]')
footer = soup.select_one('h1#footer')
print(footer)
# <h1 id="footer">Footer</h1>

print('\n[ 계층적 하위 태그 접근 ]')
# .select_one( '  >  ' ) : 쉼표 내 계층 표현
link1 = soup.select_one('div#link > a.external_link')
print(link1)
# <a class="external_link" href="www.google.com">google</a>

print('\n[find와 비교]')
# : 얘는 찾은 변수에서 찾아야한다
link_find = soup.find('div', {'id': 'link'})
external_link = link_find.find('a', {'class': 'external_link'})
# => link_find에 soup이 오면 안됨
print('find external_link: ', external_link)
# <a class="external_link" href="www.google.com">google</a>

print('\n[ 계층적 하위 태그 접근 2 : 공백으로 접근 ]')
# (상위태그 하위태그)
link2 = soup.select_one('div#class1 p#second')
print(link2)            # <p id="second">class1's   second   paragraph</p>
print(link2.string)     # class1's   second   paragraph


print('\n [ select( ) ] ------------------------------')
print('[ <h1> 태그 검색 ]')
h1_all =  soup.select('h1')
print('h1_all: ', h1_all)
# h1_all:  [<h1 id="heading">Heading   1</h1>, <h1 id="footer">Footer</h1>]

print('\n[ url 링크 검색 ]')
url_links =  soup.select('a')
for link in  url_links:
    print(link['href'])
# www.google.com
# www.naver.com
# /pages/page1.html


print('\n[ <div id="class1"> 내부 url 검색 ]')
div_urls = soup.select('div#class1 > a')
# 부등호 사용
print(div_urls)
# [<a class="external_link" href="www.naver.com">naver</a>, <a class="internal_link" href="/pages/page1.html">Page1</a>]
print(div_urls[0]['href'])
# www.naver.com

# 공백으로 구분하는 법
div_urls2 = soup.select('div#class1 a')
print(div_urls2)  # 똑같이 나온다


print('\n[ 여러 항목 검색 ( , ) ]')
# h1에서 id=heading과 id=footer를 검색
# -> 쉼표로 나열
h1 = soup.select('#heading, #footer')
print(h1)
# [<h1 id="heading">Heading   1</h1>, <h1 id="footer">Footer</h1>]

# <a> 태그에서 class=external_link 와 class=internal_link 를 검색
url_links =  soup.select('a.external_link, a.internal_link')
print(url_links)
# [<a class="external_link" href="www.google.com">google</a>, <a class="external_link" href="www.naver.com">naver</a>, <a class="internal_link" href="/pages/page1.html">Page1</a>]


print('\n [ 애국가로 연습하기] ---------------------------')
# 애국가
national_anthem = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>애국가</title>
</head>
<body>
    <div>
        <p id="title">애국가</p>
        <p class="content">
            동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            남산 위에 저 소나무 철갑을 두른 듯 바람서리 불변함은 우리 기상일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>                
    </div>
</body>
</html>
"""
soup = BeautifulSoup(national_anthem, 'html.parser')

print('\n[ 제목과 가사 내용 추출 ]')
print(soup.select_one('p#title').string)    # 애국가

contents = soup.select('p.content')
for content in contents:
    print(content.text)





print('============= <3장 HTML 분석 및 정규식 > ================')
html_warNpeace = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# [ HTML 분석 개념 ]
# - 필요한 정보를 가져오기 위함
#
# [ 목차 ]
# 1. CSS 속성을 이용한 검색
# 2. 특정 단어 찾기
# 3. 트리 이동
# 4. 정규 표현식
#
print('[ 1. CSS 속성을 이용한 검색 ] ==============================')
# 복습 바이브
# - 속성(attrs) 사용
# - span: 속성을 지정할 때 사용
# - 클래스에 스타일(글자색 등)을 정의하면 일괄 적용/수정이 쉽다.
html_text = '<span class="red">Heavens!</span>'
soup = BeautifulSoup(html_text, 'html.parser')
# --------------------------------------------------------------
print('\n[ 1-1. 속성 검색 ]')
object_tag = soup.find('span')  # find()
print('object_tag:',object_tag)
# object_tag: <span class="red">Heavens!</span>
print('object_tag.attrs:',object_tag.attrs)
# object_tag.attrs: {'class': ['red']}
print('object_tag.value:',object_tag['class'])
# object_tag.value: ['red']
print('object_tag.text:',object_tag.text)
# object_tag.text: Heavens!
# 맨 처음 결과만 출력 : ['red']

soup = BeautifulSoup(html_warNpeace, 'html.parser')   # soup 계속 변경

print('[ 1-2. 태그 검색 ]: 등장인물 검색하기')
nameList = soup.find_all('span', {'class':'green'})
for name in nameList:
    print(name.text)
# Anna ~
# 줄바꿈이 포함됨

print('\n[ 1-3. 태그 검색 ]: find_all')
princeList = soup.find_all(string='the prince')
print(princeList)
print('the	prince	count: ', len(princeList))
# ['the prince', 'the prince', 'the prince', 'the prince', 'the prince', 'the prince', 'the prince']
# the	prince	count:  7

print('\n=================== [ 2. 트리 이동 ] ======================')
#   - 특정 위치를 기준으로 태그를 찾을 때
#   - 특정 행 위아래 이동
html2 = urlopen('https://www.pythonscraping.com/pages/page3.html')
soup =  BeautifulSoup(html2, 'html.parser')
# -------------------------------------------------------------------

print('\n[ 2-1. .children ]')
table_tag =	soup.find('table', {'id': 'giftList'})
print('children 개수: ', len(list(table_tag.children)))
# giftList 의 하위항목(자식)은 13개 (공백 포함)
# children 검색 시: 화면에 보이지 않는 공백으로 내용에 공백이 포함될 수 있음
for	child in table_tag.children:
    print(child)
    print('-' * 30)
# -------------------------------------------------------------------
print('\n[ 2-2. .descendants ]')
# 모든 태그마다 분리하여 표현
desc = soup.find('table', {'id': 'giftList'}).descendants
list_desc =  list(desc)
print('descendants 개수: ', len(list_desc))
# descendants: 태그 기준 분리, 자식 많음: 86개
for tag in list_desc:
    print(tag, '#')
# ------------------------------------------------------------------

print('\n[ 2-3. .next_sibling ]')
# 지정된 테이블의 다음 행들을 모두 선택
sibling_tags = soup.find('table', {'id': 'giftList'}).tr.next_siblings
# : giftList의 첫 .tr 선택 -> 이후 모든 형제 선택
for sibling in sibling_tags:
    print(sibling, '$')
    # 공백 포함, <tr> ~ </tr> 이 줄줄이 나온다
# ------------------------------------------------------------------

print('\n[ 2-4. .previous_sibling ]')
# 선택된 행 이전의 항목들을 선택
for	sibling	in	soup.find('tr', {'id': 'gift2'}).previous_siblings:
    print(sibling)