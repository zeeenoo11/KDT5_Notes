from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
# <5장 동적 웹페이지 크롤링 > ========================================
# [1. Selenium 라이브러리 설치]
# : 관리자 권한 실행 > conda install selenium
# ------------------------------------------------------------
if 0 :
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.naver.com/')
    print(driver.current_url)

    sleep(2)
    driver.close()
    driver.quit()

if 0 :
    print('\n[ selenium 사용 ] --------------------------------------------')
    # chromedriver가 설치된 파일에서 .exe 를 가져오기
    # path(C:\ProgramData\anaconda3\envs\My_38)에 붙여넣기
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')

    print(driver.current_url)
    print(driver.title)
    print(driver.page_source)

    driver.implicitly_wait(time_to_wait=5)  #
    driver.close()
    driver.quit()
# ----------------------------------------------------------------------

if 0:
    print('\n[ Selenium API ] ===========================================')
    # [ selenium API : element 접근 ]
    # - bs 와 유사하다
    # - 하나의 요소에 접근하는 함수
    #   1)
    #   2)
    #
    # - 여러 요소에 접근하는 함수
    #   1)
    #   2)
    # -------------------------------------------------------------------
    #
    driver = webdriver.Chrome()
    driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
    driver.implicitly_wait(5)

    print('-'*20)

    # bs처럼 데이터를 수집할 수 있다
    # : find_elements(by.class_name, '클래스 이름')
    nameList = driver.find_elements(By.CLASS_NAME, value='green')
    for name in nameList:
        print(name.text)

    driver.quit()

if 0 :
    print('\n[ Selenium API: 텍스트 입력 ] ==================================')

    # .send_keys( )
    # - <input> 태그처럼 입력 가능한 요소엔 .send_keys()

    # User Agent 정보 추가
    agent_option = webdriver.ChromeOptions()
    user_agent_string = 'Mozilla/5.0'
    agent_option.add_argument('user-agent=' + user_agent_string)


    driver = webdriver.Chrome(options=agent_option)
    driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/')
    # 이상한 오류로 페이지를 찾지 못함
    # line 242, in check_response
    #     raise exception_class(message, screen, stacktrace)
    # selenium.common.exceptions.NoSuchWindowException: Message: no such window: target window already closed
    # from unknown error: web view not found
    #   (Session info: chrome=121.0.6167.161)

    driver.implicitly_wait(5)

    # <input>의 이름이 id를 검색
    driver.find_element(By.NAME, value='id').send_keys('wjs3165')
    driver.find_element(By.NAME, value='pw').send_keys('1234')

    # //*[@id='log.login']
    # driver.find_element(By.XPATH, value='//*[@id="log.login"]').click()
    driver.find_element(By.ID, 'log.login').click()

    driver.quit()

if 0 :
    print('\n[Selenium API: 구글 검색어 입력 및 검색 결과 ] =================')

    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')

    driver.implicitly_wait(5)

    search_box =  driver.find_element(By.NAME, value='q')
    search_box.send_keys('Python')
    search_box.submit()     # 검색 버튼 클릭

    time.sleep(3)
    # 전체 길이 추출을 위한 search_results
    # - find_element 's'!! element하면 len 못 뽑음
    search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
    print(len(search_results))

    # Extract and print the title and URL of each search result
    for result in search_results:
        # 한 요소씩 뽑기
        title_element = result.find_element(By.CSS_SELECTOR, 'h3')
        title = title_element.text.strip()
        print(f'{title}')

    driver.quit()

if 0 :
    print('\n[Selenium API: 프레임 이동 ] ===========================')
    # [ iframe (inline frame) 접근]
    # : 현재 페이지에 다른 웹페이지를 불러와서 삽입
    #   - <iframe src='삽입할 페이지 주소'></iframe>
    #
    # 검색하는 데 분명 있어 보이지만 결과가 안 나올때: frame 확인
    #
    # frame 내부 요소 검색은 find_element()로는 안됨
    # : .switch_to.frame('프레임 이름')
    #   .switch_to.window('윈도우 이름')
    # ---------------------------------------------------------------
    driver = webdriver.Chrome()
    driver.get('https://blog.naver.com/swf1004/221631056531')
    # .switch_to.frame 사용
    driver.switch_to.frame('mainFrame')
    # driver의 주소를 html로 선언
    html = driver.page_source
    # selenium 써도 무관
    soup =  BeautifulSoup(html, 'html.parser')
    #
    whole_border = soup.find('div', {'id': 'whole-border'})
    results = whole_border.find_all('div', {'class': 'se-module'})

    result1 = []
    for result in results:
        print(result.text.replace('\n', ''))
        result1.append(result.text)

if 0 :
    print('\n[동적 웹크롤링 : Coffee Bean 매장 찾기 ] ===========================')
    print('\n[매장 검색 테스트]')
    # 홈페이지 실행
    driver = webdriver.Chrome()
    driver.get('https://www.coffeebeankorea.com/store/store.asp')
    # storePop2(1) : 팝업 창 호출하기
    #              : 매장 안내에 뜨는 팝업창을 여는 함수
    driver.execute_script('storePop2(1)')

    # 함수호출 결과페이지를 별돌 저장 후 bs 연동
    # .page_source : requests.get() 의 text와 동일
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # html을 보기 좋게 출력
    print(soup.prettify())  # 이제 여기서 추출하기

if 0 :
    print('\n[ 예제 코드1 ] ===========================')
    driver = webdriver.Chrome()
    driver.get('https://www.coffeebeankorea.com/store/store.asp')

    # 팝업창 생성
    driver.execute_script('storePop2(1)')
    # 현재의 html 소스를 저장
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # 매장 이름 추출
    store_names = soup.select('div.store_txt > p.name > span')
    store_name_list = []
    for name in store_names:
        store_name_list.append(name.text)
    # 전체 매장 개수 및 매장 이름 리스트 출력
    print('매장 개수:', len(store_name_list))
    print(store_name_list)
    # 주소만 모으기
    store_addresses =  soup.select('p.address > span')
    store_address_list = []
    for address in store_addresses:
        print(address.get_text())
        store_address_list.append(address.text)

    driver.quit()   # webdriver 종료

if 1 :
    print('\n[ 예제 코드2 ] ===========================')
    def coffeebean_store(store_list):
        coffeebean_url = 'https://www.coffeebeankorea.com/store/store.asp'
        driver = webdriver.Chrome()

        for i in range(1,388):  # 388:
            driver.get(coffeebean_url)
            time.sleep(1)

            driver.execute_script('storePop2(%d)' % i)  #
            time.sleep(1)
            try:
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')

                store_name = soup.select_one('div.store_txt > h2').text
                store_info = soup.select('div.store_txt > table.store_table > tbody > tr > td')
                store_address_list = list(store_info[2])
                store_addr = store_address_list[0]
                store_tel = store_info[3].text
                print("{} {} {}" .format(i+1, store_name, store_addr, store_tel))
                store_list.append([store_name, store_addr, store_tel])
            except:
                continue

    def main():
        store_info = []
        coffeebean_store(store_info)
        # DataFrame으로 변경
        coffeebean_table = pd.DataFrame(store_info, columns=['store_name', 'store_addr', 'store_tel'])
        print(coffeebean_table.head())

        coffeebean_table.to_csv('coffeebean_branches.csv', mode='w', index=True, encoding='utf-8-sig')

    main()

# Fin.
