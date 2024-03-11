import os
import sys
import urllib.request
import urllib.parse

print('\n=============== <6장? Naver Open API를 활용한 크롤링 > ==================')
# 네이버 개발자 센터 > 서비스 API > 검색 > 신청
# - 일일 API호출 허용량   : 25,000
# - API 1회 호출(검색 수) : 100개
#   총 검색 수            : 최대 1000개

if 0 :
    print('\n[ Python 샘플 코드 ] ===========================================================')
    # 네이버 검색 API 예제 - 블로그 검색
    # import os
    # import sys
    # import urllib.request
    client_id = "ayE9TJgr2fOV93HmewOg"  # 발급한 아이디
    client_secret = "vzK9j6gBnE"
    encText = urllib.parse.quote("빅데이터")
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    # 실행 결과: items: 로 출력, 1000개까지 가능
    # ----------------------------------------------------------------------------------

# [ OpenAPI 가이드 ]
# - 요청 URL

# - 파라미터

# - 응답 변수

print('\n[ 네이버 검색 API 예제 : 뉴스 검색 ] =======================================')
# node : 'news' ; 크롤링 대상
# base : https//openapi.naver.com/v1/search/"
# get_naver_search() : base + node 로 검색함
# ---------------------------------------------
import urllib.request
import datetime
import json

def get_request_url(url):
    client_id = "ayE9TJgr2fOV93HmewOg"
    client_secret = "vzK9j6gBnE"

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",client_id)
    req.add_header("X-Naver-Client-Secret",client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f'Error for URL: {url}')


def get_naver_search(node, search_text, start, display):
    base = "https://openapi.naver.com/v1/search/"
    node = f"/{node}.json"
    query_string = f"{urllib.parse.quote(search_text)}"

    parameters = ("?query={}&start={}&display={}".format(query_string, start, display))

    url = base + node + parameters
    response = get_request_url(url)

    if response is None:
        return None
    else:
        return json.loads(response)
        # json.loads 로 하나씩 객체로 만듦 -> main()에서 딕셔너리 형태로 활용 가능


def main1():
    node = 'news'
    search_text = '코로나'
    cnt = 0

    json_response = get_naver_search(node, search_text, 1, 100)
    if (json_response is not None) and (json_response['display'] != 0):
        for post in json_response['items']:
            cnt += 1
            print(f"[{cnt}]", end=" ")
            print(post['title'])
            print(post['description'])
            print(post['originallink'])
            print(post['link'])
            print(post['pubDate'])
            # 100개의 뉴스를 검색


print('\n[ 네이버 뉴스 검색 2단계: 날짜 정보 변경 및 1000개까지 검색 ] ===============================')
# 1. 날짜 형식 변경
# 2.
import pandas as pd


def get_post_data(post, json_result_list, cnt):
    # 2단계용 함수
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    '''
    srtptime()
    - %a: abbreviated weekday name
    - #b: abbreviated month name
    '''
    # 한국 시간에 맞게 +0900
    pdate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pdate = pdate.strftime('%Y-%m-%d %H:%M:%S')

    print(f'[{cnt}]', end=' ')
    print(title, end=": ")
    print(pdate, end=' ')
    print(link)

    json_result_list.append([cnt, pdate, title, description, org_link, link])


def main2():
    node = 'news'
    search_text = '인공지능'
    cnt = 0
    json_result_list = []

    json_response = get_naver_search(node, search_text, 1, 100)
    # 1회 호출 한도가 100회이므로 while 사용
    while (json_response is not None) and (json_response['display'] != 0):
        for post in json_response['items']:
            cnt += 1
            get_post_data(post, json_result_list, cnt)

        start = json_response['start'] + json_response['display']
        json_response = get_naver_search(node, search_text, start, 100)
        # 1000개를 돌리는 구문
        # : 1회 호출 한도 100개
        # : start 101~ 1000개까지

    print('전체 검색 수:', cnt)

    columns = ['cnt', 'pdate', 'title', 'description', 'org_link', 'link']
    result_df = pd.DataFrame(json_result_list, columns=columns)
    result_df.to_csv(f'{search_text}_naver_{node}.csv', index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    # stage 1: main1()
    # stage 2: main2()
    # main1()
    main2()
