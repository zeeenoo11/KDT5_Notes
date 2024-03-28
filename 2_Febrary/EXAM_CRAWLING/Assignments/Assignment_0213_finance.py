from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# < 과제3 : 네이버 증시 정보 크롤링 >
# 1. 시가 총액 10위까지의 기업 정보를 리스트에 저장
#   - 종목명, 종목코드, 현재가, 전일가, 시가, 고가, 저가
#   - 한글 깨짐 예방을 위해 requests 사용
# 2. 메뉴에서 선택한 기업의 세부 주식 정보를 출력
# 3. -1 을 입력할 때까지 반복


def search_corp():  # 순위에 따른 회사명과 URL 추출
    # 1) 회사 정보 크롤링
    url = 'https://finance.naver.com/sise/sise_market_sum.naver'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    # 2) 기업 시가총액 순위 검색
    corp_list = []
    corps_url = []
    corp_list_driver = driver.find_elements(By.CLASS_NAME, 'tltle')
    for corp in corp_list_driver:
        corp_list.append(corp.text)
        corps_url.append(corp.get_attribute('href'))
        if len(corp_list) >= 10:
            break
    driver.close()
    driver.quit()

    return corp_list, corps_url


def print_table(corp_list, corps_url):  # 출력문
    # 1) 초기 출력문
    print('-'*50)
    print('[ 네이버 코스피 상위 10대 기업 목록 ]')
    print('-'*50)

    # 2) 10대 기업 목록
    for num, corp in enumerate(corp_list):
        print(f'[{num+1:2d}]', corp)

    # 3) 기업 선택
    while True:
        try:
            corp = input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료): ')
            if corp == '-1':
                break

            # 3-1) int(corp)에 맞는 회사 정보 출력
            # print(int(corp))
            print(corps_url[int(corp)-1])

            # 3-2) 접근 하기
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(corps_url[int(corp)-1])  # 입력된 번호에 맞는 url 접근
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            rows = soup.select('dl.blind > dd')

            # 3-3) 결과 출력
            for row in rows[1:8]:
                if row.string.split()[0] != '상한가':
                    print(row.string.split()[0], ':', row.string.split()[1])
        # 예외절
        except Exception as e:
            print(e)
            print('1~10 사이의 숫자만 입력해주세요.')


def main():
    corp_list, corps_url = search_corp()
    print_table(corp_list, corps_url)


if __name__ == '__main__':
    main()
