from urllib.request import urlopen
from bs4 import BeautifulSoup

# <과제2 : 네이버 날씨>
# : 네이버에서 대구 날씨 정보 가져오기
#   1. <div class=“weather_info”>
#   2. <div class=“temperature_text”>
#   3. <span class="weather before_slash">맑음</span>
#   4. <ul class="today_chart_list">
#   5. <div class=“graph_inner _hourly_weather”>

# 교수님 자료
# - 지역명 검색 기능 :
#   city=input; quote(f'{city}+날씨')
#   html = 'https:// ~~~ ' +  quote


def main():
    html = urlopen("https://search.naver.com/search.naver?query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8")
    soup = BeautifulSoup(html, "html.parser")
    print_weather(soup)


def print_weather(soup):
    print('현재 위치:', soup.select_one('h2.title').text)
    print('현재 온도:', soup.select_one('div.temperature_text').text.strip())
    print('날씨 상태:', soup.select_one('span.weather').text)

    print('공기 상태:')
    airList = soup.select_one('ul.today_chart_list').text.split()
    for i in range(len(airList)//2):
        print(airList[i*2], airList[i*2+1])
    print('-'*30)

    print('시간대별 날씨 및 온도')
    print('-'*30)
    hourly_weather = soup.select_one('div.graph_inner._hourly_weather').text.split()
    for i in range(len(hourly_weather) // 3):
        print(hourly_weather[i * 3], hourly_weather[i * 3 + 1], hourly_weather[i * 3 + 2])


if __name__ == "__main__":
    main()
