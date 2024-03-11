# [ 과제3 ] 구군별 남녀 비율을 파이 차트로 구현
# - subplots(3,3,n)
# - gender.csv
import csv
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


def draw_pie_chart(pop_rate, cities):
    """
    pie 차트를 그리는 함수
    :param pop_rate: [남성, 여성 총 인구수]의 집합
    :param cities: 출력하고 싶은 도시(구역) 명
    :return: None
    """
    plt.figure(figsize=(10,10))
    plt.suptitle('대구광역시 구별 남녀 인구 비율')
    color = ['cornflowerblue', 'tomato']

    for i in range(9):
        plt.subplot(3, 3, i+1)
        plt.pie(pop_rate[i], labels=['남성', '여성'], autopct='%.1f%%', colors=color, startangle=90)
        plt.title(cities[i])
    plt.show()


def calculate_population():
    # data load
    f = open('DATA/gender.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    # 변수 선언
    pop_rate = []
    cities = ['대구광역시 ', '대구광역시 중구', '대구광역시 동구',
            '대구광역시 서구', '대구광역시 남구', '대구광역시 북구',
            '대구광역시 수성구', '대구광역시 달서구', '대구광역시 달성군']
    # 구역별 [남, 여 총 인구수] 계산 및 리스트 입력
    for city in cities:
        for row in data:
            if city in row[0]:   # 구역에 해당된다면
                male_num = int(row[104].replace(',',''))
                female_num = int(row[207].replace(',',''))
                pop_rate.append([male_num, female_num])
                break
    print(pop_rate)
    f.close()
    draw_pie_chart(pop_rate, cities)

calculate_population()