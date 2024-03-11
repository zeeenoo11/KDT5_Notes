from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


print('=============== <3장 HTML 분석 및 정규식 > ==================')
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

# [ HTML 분석 개념 ]
# - 필요한 정보를 가져오기 위함


print('[ CSS 속성을 이용한 검색 ] ====속성 검색 태그 검색========================')
# 복습 바이브
# - 속성(attrs) 사용
# - span: 속성을 지정할 때 사용
# - 클래스에 스타일(글자색 등)을 정의하면 일괄 적용/수정이 쉽다.
html_text = '<span class="red">Heavens!</span>'
soup = BeautifulSoup(html_text, 'html.parser')

print('\n[속성 검색]')
object_tag = soup.find('span')
print('object_tag:',object_tag)
# object_tag: <span class="red">Heavens!</span>
print('object_tag.attrs:',object_tag.attrs)
# object_tag.attrs: {'class': ['red']}
print('object_tag.value:',object_tag['class'])
# object_tag.value: ['red']
print('object_tag.text:',object_tag.text)
# object_tag.text: Heavens!
# 맨 처음 결과만 출력 : ['red']

soup = BeautifulSoup(html, 'html.parser')   # soup 계속 변경

print('[태그 검색]: 등장인물 검색하기')
nameList = soup.find_all('span', {'class':'green'})
for name in nameList:
    print(name.text)
# Anna ~
# 줄바꿈이 포함됨

print('\n[태그 검색]: find_all')
princeList = soup.find_all(string='the prince')
print(princeList)
print('the	prince	count: ', len(princeList))
# ['the prince', 'the prince', 'the prince', 'the prince', 'the prince', 'the prince', 'the prince']
# the	prince	count:  7

print('\n[ 트리 이동 ] =======.children .descendants .next_siblings ========')
#   - 특정 위치를 기준으로 태그를 찾을 때
#   - 특정 행 위아래 이동
html2 = urlopen('https://www.pythonscraping.com/pages/page3.html')
soup =  BeautifulSoup(html2, 'html.parser')

print('\n[ .children ]')
table_tag =	soup.find('table', {'id': 'giftList'})
print('children 개수: ', len(list(table_tag.children)))
# giftList 의 하위항목(자식)은 13개 (공백 포함)
# children 검색 시: 화면에 보이지 않는 공백으로 내용에 공백이 포함될 수 있음
for	child in table_tag.children:
    print(child)
    print('-' * 30)

print('\n[ .descendants ]')
# 모든 태그마다 분리하여 표현
desc = soup.find('table', {'id': 'giftList'}).descendants
list_desc =  list(desc)
print('descendants 개수: ', len(list_desc))
# descendants: 태그 기준 분리, 자식 많음: 86개
for tag in list_desc:
    print(tag, '#')

print('\n[ .next_sibling ]')
# 지정된 테이블의 다음 행들을 모두 선택
sibling_tags = soup.find('table', {'id': 'giftList'}).tr.next_siblings
# : giftList의 첫 .tr 선택 -> 이후 모든 형제 선택
for sibling in sibling_tags:
    print(sibling, '$')
    # 공백 포함, <tr> ~ </tr> 이 줄줄이 나온다

print('\n[ .previous_sibling ]')
# 선택된 행 이전의 항목들을 선택
for	sibling	in	soup.find('tr', {'id': 'gift2'}).previous_siblings:
    print(sibling)

print('[ whitespace: 태그 하나만 반환 ]')
# 문자열 마지막에 whitespace(\n, \t)가 있는 경우1
# 실제론 \n 은 html에서 안씀: 예제용
sibling1 = soup.find('tr', {'id': 'gift3'}).next_sibling
print('sibling1:', sibling1)    # 미출력 : \n 이라서
print(ord(sibling1))

print('\n[ 해결: .next_sibling.next_sibling ]')
sibling2 =  soup.find('table', {'id': 'giftList'}).tr.next_sibling.next_sibling
print(sibling2)
# 이러면 값이 잘 출력됨


print('\n[ .parent ] =================================================')
# 부모 태그를 검색; 자신을 포함해서 나온다
style_tag = soup.style
print(style_tag.parent)
#  <head> <style> ~  </style> </head>

print('\n[ .parent 사용 ]')
# 이미지 검색 > 부모 태그 검색 > 이전 형제 태그 검색 > 가격 확인
img1 = soup.find('img', {'src': '../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)
# => $15.00


print('\n[ 정규 표현식 ] ===========================================')
# : 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어
# [사용]
#   - (regex)
#   - 문자열의 유효성 검사:
#     이메일, 전화번호, 웹사이트 주소 등
#   - 문자열 치환, 검색, 추출 등
# [장점]
#   - 다양한 입력 문자열 처리가 간결
#   - 범용성: 다양한 언어에서 지원
# [단점]
#   - 어려움ㅜㅜㅜ


# [ 정규 표현식 기호: 문자 집합 ] ^ . \d 자주 쓰임 ---------------
# 표현식               설명
#   ^           문자열 시작
#   $           문자열 종료
#   .           임의의 한 문자
#   \b          단어의 경계(공백) 검색
#   \s          공백 문자
#   \S          공백이 아닌 문자
#   \w          알파벳, 숫자, _ 검색
#   \W          알파벳, 숫자, _ 이외의 문자
#   \d          숫자 =[0-9]
#   \D          숫자를 제외한 모든 문자 =[^0-9]
#   \           확장 문자 (그 문자 자체를 의미)
#   r'패턴'     순수 문자열이라는 뜻

# [ 정규 표현식 기호: 그룹과 범위 ] [ ], ( ), [^] 자주 쓰임
#  표현식              설명
#   [ ]         문자의 집합이나 범위를 뜻함
#   [^]         [ ] 내의 ^ : not을 뜻함
#   ()          그룹: 하나의 문자로 인식
#   |           OR 연산
#   (?i)        대소문자 구분하지 않음
#   (?:)        뒤에 따라 나오는 문자를 하나의 그룹으로 합침
#   ?=(regex)   전방 긍정(=) 탐색 : 일치한다 -> (regex) 앞의 값 반환
#   ?!(regex)   전방 부정(!) 탐색
#   ?<=(regex)  후방(<) 긍정 탐색 : -> (regex) 뒤의 값을 반환
#   ?<!(regex)  후방(<) 부정 탐색

# [ 정규 표현식 기호: 수량 표시 ]
# 글자 뒤에 오는 표현 ( X*  X+)
#  표현식              설명
#   *           없거나 많거나
#   +           하나 이상
#   ?           없거나 하나
#  {n}         정확히 n개
#  {n,}        최소 n개 : n개 이상
#  {n,m}       최소 n개, 최대 m개
#   *?        가장 적게 일치하는 패턴 검색

# [ 빈출 정규 표현식 ]
#   설명            정규 표현식
#   숫자             ^[0-9]*$
#   영문자           ^[a-zA-Z]*$
#   한글             ^[가-힣]*$
#   영문자, 숫자     ^[a-zA-Z0-9]*$
#   이메일           ^[a-zA-Z0-9]+@[a-zA-Z0-9]+$
#   휴대전화         ^010-([0-9]{3,4})-([0-9]{4})$
#   주민등록번호     ^([0-9]{6})-([0-9]{7})$
#   ip 주소          ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$
#   패스워드         ^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]{8,15}$

# [ 정규 표현식 : re 모듈 함수 ]
#       함수명                            설명
#   compile(pattern, string)        정규식 객체 반환
#   search(pattern, string)         처음 매칭되는 문자열 리턴
#   match(pattern, string)
#   split(pattern, string)
#   findall(pattern, string)
#   finditer(pattern, string)
#   sub(pattern, repl, string)

# 주피터에서 사용

# [ compile(pattern) ]


# [ match( ) ]


# 과제 짱 많아...
