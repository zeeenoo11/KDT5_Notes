# [과제]
# 딕셔너리 생성
dict_capital = {
    'Seoul': ['South Korea', 'Asia', '9,655,000'],
    'Tokyo' :['Japan', 'Asia', '14,110,000'],
    'Beijing' : ['China', 'Asia', '21,540,000'],
    'London' : ['United Kingdom', 'Europe', '14,800,000'],
    'Berlin' : ['Germany', 'Europe', '3,426,000'],
    'Mexico City' : ['Mexico', 'America', '21,200,000']}

# 프로그램 제작
def menu_screen():
    print('-'*50)
    print("""1. 전체 데이터 출력
2. 수도 이름 오름차순 출력
3. 모든 도시의 인구수 내림차순 출력
4. 특정 도시의 정보 출력
5. 대륙별 인구수 계산 및 출력
6. 프로그램 종료""")
    print('-'*50)
    while True:
        menu = input('메뉴를 입력하세요: ')
        if menu.isdecimal():
            if 1<= int(menu) <= 6: break
        print('1과 6사이의 정수를 입력하세요.')

    def menu_choose(menu):
        i = 1
        if int(menu)==1: # 전체 메뉴 출력
            for key, value in dict_capital.items():
                print(f'[{i}] {key:<12}: {value}')
                i += 1

        elif int(menu)==2: # 수도 이름 오름차순 정렬
            for key in sorted(dict_capital.keys()):
                print(f'[{i}] {key:<12}: {dict_capital[key]}')
                i += 1

        elif int(menu)==3: # 모든 도시의 인구수 내림차순 정렬
            for key, value in sorted(dict_capital.items(), key=lambda x:int(x[1][2].replace(',', '')), reverse=True):
                print(f'[{i}] {key:<12}: {value[2]:>10}')
                i += 1

        elif int(menu)==4: # 특정 도시의 정보 출력
            city_in = input('출력할 도시 이름을 입력하세요: ')
            if city_in in dict_capital.keys():
                print('도시:', city_in)
                print(f'국가: {dict_capital[city_in][0]}, 대륙: {dict_capital[city_in][1]}, 인구 수: {dict_capital[city_in][2]}')
            else: print(f'도시 이름: {city_in}은 key에 없습니다.')

        elif int(menu)==5: # 대륙병 인구수 계산 및 출력
            continent_in = input('대륙 이름을 입력하세요(Asia, Europe, America): ')
            sum_pop = 0
            for key in dict_capital.keys():
                if dict_capital[key][1] == continent_in:
                    print(f'{key}: {dict_capital[key][2]}')
                    sum_pop += int(dict_capital[key][2].replace(',',''))
            print(f'{continent_in} 전체 인구수 : {sum_pop:,}')

        elif int(menu)==6:
            print('프로그램을 종료합니다.')
            return True

    return menu_choose(menu)

flag = 0
while not flag:
    flag = menu_screen()


# -------- 교수님 자료 ----------------------
# - 범용 dict sort 함수 (dict, key=False, index=0, desc=False)
# - 입력문과 if 단락이 반대로 정리: while 쓰기 더 쉬울 것