# 교재 2장
from urllib.request import urlopen
from bs4 import BeautifulSoup

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

# ==================== < 2장 BeautifulSoup 활용 > ======================
# [ BeautifulSoup 라이브러리 ]
# - HTML과 XML 분석 위함
# - 객체 생성법 : soup =  BeautifulSoup(html_example, "html.parser")
# - html_example : 분석할 문서
# - html.parser(기본값) : 구문 분석기

# 예제
html = urlopen("https://www.daangn.com/hot_articles")
bs = BeautifulSoup(html.read(), "html.parser")

if 0 :
    print(bs.h1)                    # 공백 너무 많음: <h1 class="head-title" id="hot-articles-head-title">
    print(bs.h1.string.strip())
    # => 중고거래 인기매물


# [ .태그명 ]
if 0 :
    print(bs.title)
    # => <title>당근 중고거래 | 당신 근처의 당근</title>
    print(bs.title.string)
    # => 당근 중고거래 | 당신 근처의 당근
    print(bs.title.get_text()) # .string과 동일 기능
    # => 당근 중고거래 | 당신 근처의 당근

# [ .태그명.parent ]
# : 해당 태그를 포함하고 있는 부모
    print(bs.title.parent)
    # => <head> 부터 </head> 까지 나옴


# [ <a> 태그 접근 ]
# : '첫 번째' <a> 태그 요소 접근
# <a> 태그 :

if 0 :
    print(bs.a)
    # < a class ="_1knjz492" href="https://www.daangn.com" > 부터
    # </a> 까지
    # href= :
    print(bs.a.string)
    # => None
    print(bs.a['href'])         # href 속성의 url을 추출
    # => https://www.daangn.com
    print(bs.a.get('href'))     # 동일 기능
    # => https://www.daangn.com


# ---------------------- [ find( ) ] ---------------------------
# find( tag,

# [ find( tagName , attributes ) ]
# : 태그 중 특정 태그 찾기

# file = 'DATA/chap02.html'   # 얘는 왜 안되지
soup = BeautifulSoup(html_example,'html.parser')

if 0 :
    print(soup.find('div', {'id': 'text_id2'}))

    div_text = soup.find('div', {'id': 'text_id2'})
    print(div_text.text)

    print(div_text.string)


# [ find( a ) ]
# - <a> 중 class 속성값이 "intenal_link" 인 정보 추출
if 0 :
    # 아래 둘 다 같은 의미 : 딕셔너리 or class_
    href_link = soup.find('a', {'class': 'internal_link'})
    href_link = soup.find('a', class_='internal_link')
    # class는 예약어라 class_ 사용
    # class_ : list 타입

    print(href_link)
    print(href_link['href'])
    print(href_link.get('href'))
    print(href_link.text)


# [ .attrs ]
# : 모든 속성 가져오기
if 0 :
    print('href_link.attrs:	', href_link.attrs)
    print('class 속성값: ', href_link['class'])
    print


# [ find( ) 활용하기 ]
# 1. 속성 검색
#   : href 속성의 값이 'www.google.com'인 항목 검색
if 0 :
    href_value = soup.find(attrs={'href' : 'www.google.com'})
    # 'a' 태그 지정 없이도 작동 ('a'에만 href 있음)
    href_value = soup.find('a', attrs={'href': 'www.google.com'})

    print('href_value: ', href_value)
    # href_value: <a ,="" class="external_link" href="www.google.com">google</a>
    print(href_value['href'])
    # www.google.com
    print(href_value.string)
    # google


# 2. 속성 가져오기
#   : span 태그의 속성 가져오기
if 0 :
    span_tag = soup.find('span')

    print('span	tag:',	span_tag)
    # <span class="red">BeautifulSoup Library Examples!</span>
    print('attrs:',	span_tag.attrs)
    #  {'class': ['red']}
    print('value:',	span_tag.attrs['class'])
    #  ['red']
    print('text:',	span_tag.string)
    #   BeautifulSoup Library Examples!

# 3. class 속성
#   : class 속성은 여러 개의 값을 가질 수 있음 (multi values)

if 0 :  # 선언한 클래스의 속성값 반환
    href_link = soup.find('a', class_='internal_link')
    print('class 속성값: ', href_link['class'])
    # => ['internal_link']
    # find()에서 class_= 해도 href_link['class'] 에선 _ 없이 검색

tr = '''
<table>
    <tr class="passed a b c" id="row1 example"><td>t1</td></tr>
    <tr class="failed" id="row2"><td>t2</td></tr>
</table>'''

if 0 :  #
    table =  BeautifulSoup(tr, 'html.parser')
    for row in  table.find_all('tr'):
        print(row.attrs)
    # {'class': ['passed', 'a', 'b', 'c'], 'id': 'row1 example'}
    # {'class': ['failed'], 'id': 'row2'}


# --------------------- [ find_all( ) ] -------------------------
# find_all( tag, attrs, recursive, text, limit, keywords )

# [ 태그 검색 ]
# 1. 모든 div 태그 검색
if 0 :
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

# 2. 모든 a 태그 검색
if 0 :
    links = soup.find_all('a')
    for	alink in links:
        print(alink)
        print(f"url:{alink['href']}, text: {alink.string}")
        print('-'*50)
    # 3가지 출력 : <a class="external_link" href="www.google.com">google</a>
    # 의미하는 것 :

# [ 특정 태그 중 여러 속성값 검색 ]
# : 리스트 형태로 추가
if 0 :
    link_tags = soup.find_all(name='a', attrs={'class':['external_link', 'internal_link']})
    print(link_tags)
    # google, Page1 이 포함된 a 태그문 출력
    # naver는 왜 없지? -> 파일 오류,, 복붙 잘못

    p_tags = soup.find_all('p', {'id': ['first', 'third']})
    for p in p_tags:
        print(p)
    # <p id="first">class1's first paragraph</p>
    # <p id="third">class1's third paragraph</p>


# -------------------------- [ select ] -----------------------------
# [ select( ) ]
#  :

# [ select 사용법 ]
# : select( selector, namespaces=None, limit=None, **kwargs )

# select(tag)
# select(tag#id)
# select(tag.class) or (.class)
# select( ' 상위태그 > 하위태그1 > 하위태그2' )
# select(tag[ attr1 = value1 ])

print('~~~~~~~~~~~~~~~~~~~ [ select_one( ) ] ~~~~~~~~~~~~~~~~~~~~')
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

print('[find와 비교]')
# : 얘는 찾은 변수에서 찾아야한다
link_find =  soup.find('div', {'id': 'link'})
external_link = link_find.find('a', {'class': 'external_link'})
# => link_find에 soup이 오면 안됨
print('find external_link: ', external_link)
# <a class="external_link" href="www.google.com">google</a>

print('[ 계층적 하위 태그 접근 2 : 공백으로 접근 ]')
# (상위태그 하위태그)
link2 = soup.select_one('div#class1 p#second')
print(link2)            # <p id="second">class1's   second   paragraph</p>
print(link2.string)     # class1's   second   paragraph

print('\n------------------------ [ select( ) ] ------------------------------')
# 다시 select ?
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


print('\n-------------------- [ 애국가로 연습하기] ----------------------')
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

# 수업 끝


# select와 find 비교 -> 과제하고 풀기
