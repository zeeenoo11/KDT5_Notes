# 7th Feb.

# ================ < 1장 크롤링 개념 > ====================
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

print('\n\n[ BeautifulSoup 객체 구조 ]')
# - html은 짝으로 이루어진 태그 내에 내용이 있음
#   <body> <title> aaaa </title> <b1> oooo </b1> </body>
# - 내가 필요한 건 태그 내부의 텍스트 값
from bs4 import BeautifulSoup

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




# [ 예외 처리 ]
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

if 0 :
    try:
        html = urlopen('http://www.pythonscraping.com/pages/error.html')
    except HTTPError as e:
        print(e)  # 이 오류가 반환
    except URLError as e:
        print('The	server could not be found!')
    else:
        print('It worked!')


# [ 존재하지 않는 태그 접근 ]
# - None 반환, AttributeError 발생
if 0 :
    def get_Title(url, tag):
        try:
            html = urlopen(url)
        except HTTPError as e:
            return None

        try:
            bsObj = BeautifulSoup(html.read(), "html.parser")
            value =  bsObj.body.find(tag)
            # 입력된 tag 찾기 (최종 반환값)
        except AttributeError as e:
            return None
        # AttributeError -> return None
        return value

    tag = 'h2'
    value = get_Title('http://www.pythonscraping.com/pages/page1.html', tag)
    if value == None:
        print(f'{tag} could not be found')   # h2 could not be found
    else:
        print(value)


# [ urllib.request와 requests의 차이 ]
# [urllib.request]
# - 기본 파이썬 패키지
# - 바이너리로 저장, 없으면 에러

# [requests]
# - 추가 설치 필요 (conda install requests)
# -
import requests

if 0 :
    url = 'http://www.pythonscraping.com/pages/page1.html'
    # url =	'http://finance.naver.com'
    # url =	'http://www.naver.com’
    html = requests.get(url)
    print('html.encoding:', html.encoding)
    print(html.text)
    soup = BeautifulSoup(html.text, 'html.parser')
    print()
    print('h1.string:', soup.h1.string)


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
# id : #id{ 속성1:속성값; 속성2:속성값; }
# class : .className{ 속성1:속성값; 속성2:속성값; }

file = 'DATA/h1~6_test.html'
# --------- 자세한 내용 관련은 html 파일에 필기 -------------------

# [ urllib.request.Request 클래스 ]
# class urllib.request.Request(url, data=None, headers={},
# origin_req_host=None, unverifiable=False, method=None)


# [ 멜론 웹사이트 접근 ]
melon_url =	'https://www.melon.com/chart/index.htm'
# html = urlopen(melon_url)
# soup = BeautifulSoup(html.read(), 'html.parser')
# print(soup)
# Error 406 Not Acceptable : 사람이 아닌 프로그램이라 인식해 크롤링 막음
# User Agent 정보 필요

from urllib.request import Request

# [ Request로 유저 정보 추가 ]
urlrequest = Request(melon_url, headers={'User-Agent':'Mozilla/5.0'})

html = urlopen(urlrequest)
soup = BeautifulSoup(html.read().decode('utf-8'), 'html.parser')
print(soup)
