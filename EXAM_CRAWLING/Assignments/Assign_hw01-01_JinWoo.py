# < 데이터 크롤링과 정제 >

# 과제 : 일주일간의 일기 예보 내용을 화면에 출력
#       - 총 9일 간의 일기 예보 내용을 스크래핑
#       - 출력 항목:
#           <p	class=“period-name”>'Tonight'</p>
#           <img src=“…”	title=“Tonight:	Patchy	fog	between	4am	and	5am.	…”	>
#           <p	class=“short-desc”	. . .> Partly Cloudy <br>then Patch <br>Fog </p>
#           <p	class=“temp	temp-low”>Low	46	℉	</P>
from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    # url link
    html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
    soup = BeautifulSoup(html, 'html.parser')

    print('National Weather Service Forecasts for San Francisco')
    print('-'*60)
    scraping_use_find(soup)
    print('='*60)
    scraping_use_select(soup)


def scraping_use_find(soup):  # find, find_all 사용
    print('[ find 함수 사용 ]')
    total = soup.find_all('li', class_='forecast-tombstone')
    print('총 tombstone-container 검색 개수:', len(total))
    print('='*60)

    # find_all 사용
    period_name = soup.find_all('p', class_='period-name')
    short_desc = soup.find_all('p', class_='short-desc')
    temp = soup.find_all('p', class_='temp')
    image_desc = soup.find_all('img', class_='forecast-icon')

    # 결과 출력
    print_result(period_name, short_desc, temp, image_desc)


def scraping_use_select(soup):  # select, select_one 사용
    print('[ select 함수 사용 ]')

    total = soup.select('li.forecast-tombstone')
    print('총 tombstone-container 검색 개수:', len(total))

    # select 사용
    period_name = soup.select('p.period-name')
    short_desc = soup.select('p.short-desc')
    temp = soup.select('p.temp')
    image_desc = soup.select('img.forecast-icon')

    # 출력하기
    print_result(period_name, short_desc, temp, image_desc)


def print_result(period_name, short_desc, temp, image_desc):
    for i in range(len(period_name)-1):
        print('[Period]:', period_name[i+1].text)
        print('[Short desc]:', short_desc[i+1].text)
        print('[Temperature]:', temp[i].text)
        print('[Image desc]:', image_desc[i+1]['title'])
        print('-'*60)


main()
