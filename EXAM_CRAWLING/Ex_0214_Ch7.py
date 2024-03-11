

PASS = False
print('\n============================ < 7장 한국어 형태소 분석 > ================================')

# [ 한국어 자연어 처리 : KoNLPy ]
from konlpy.tag import Okt

okt = Okt() # Open Korean Text
text = '마음에 꽂힌 칼한자루 보다 마음에 꽂힌 꽃한송이가 더 아파서 잠이 오지 않는다'

# pos(text) : 문장의 각 품사를 태깅
# norm=True : 문장 정규화
# stem=True : 어간 추출 (보다, 보니, 보고 -> 어간 : 보)
okt_tags = okt.pos(text, norm=True, stem=True)
print(okt_tags)
# nouns(text) : 명사만 리턴
okt_nouns = okt.nouns(text)
print(okt_nouns)


print('\n[ 예제 2 ] -------------------------------------------------')

text ='나랏말이 중국과 달라 한자와 서로 통하지 아니하므로, \
우매한 백성들이 말하고 싶은 것이 있어도 마침내 제 뜻을 잘 표현하지 못하는 사람이 많다.\
내 이를 딱하게 여기어 새로 스물여덟 자를 만들었으니, \
사람들로 하여금 쉬 익히어 날마다 쓰는 데 편하게 할 뿐이다.'

okt = Okt()

#  morphs(text) : 텍스트를 형태소 단위로 나눔
okt_morphs = okt.morphs(text)
print('morphs():\n', okt_morphs)

# 명사만 추출
okt_nouns = okt.nouns(text)
print('nouns():\n', okt_nouns)

# phrases(text) : 어절 추출
okt_phrases = okt.phrases(text)
print('phrases():\n', okt_phrases)

# pos(text) : 품사를 태깅
okt_pos = okt.pos(text)
print('pos():\n', okt_pos)


print('\n[ Word Cloud ] ============================================')
from wordcloud import  WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image


# mask :
text = open('DATA/수업소스/test.txt' , encoding='utf-8').read()
okt = Okt()

sentences_tag = []
sentences_tag = okt.pos(text)

noun_adj_list = []
for word, tag in sentences_tag:
    if tag in ['Noun', 'Adjective']:
        noun_adj_list.append(word)

print(noun_adj_list)
counts = Counter(noun_adj_list)
tags = counts.most_common(50)
print(tags)
# 폰트 경로
path = "C:\Windows\Fonts\malgun.ttf"

img_mask = np.array(Image.open('DATA/수업소스/cloud.png'))
wc = WordCloud(font_path=path, width=400, height= 400,
               background_color='white', max_font_size=200,
               repeat=True,
               colormap='inferno', mask=img_mask)

# .generate_from_frequencies() : 빈도수 기반으로 단어 생성
cloud = wc.generate_from_frequencies(dict(tags))

if PASS:
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()


print('\n[ 영문 wordcloud 예제 ] ============================================')

from wordcloud import STOPWORDS

text = open('DATA/수업소스/alice.txt' , encoding='utf-8').read()
STOPWORDS.add('said')
print('STOPWORDS:', STOPWORDS)
# STOPWORDS: {'the', "he'd", 'up', "here's", "you'll", 'my', "you've", ...

img_mask = np.array(Image.open('DATA/수업소스/alice.png'))

wc = WordCloud(font_path=path, width=400, height= 400,
               background_color='white', max_font_size=200,
               stopwords=STOPWORDS,
               repeat=True,
               colormap='inferno', mask=img_mask).generate(text)

print(wc.words_)
# {'Alice': 1.0, 'little': 0.29508196721311475, 'one': 0.27595628415300544, ...
if PASS:
    plt.figure(figsize=(10,8))
    plt.axis('off')
    plt.imshow(wc)
    plt.show()


print('\n[ 네이버 뉴스 타이틀 Word Cloud ] ============================================')
# 크롤링 > Word Cloud
# 뉴스의 타이틀을 모아 구름을 만들기
import requests
import time
from bs4 import BeautifulSoup


def get_titles(start_num, end_num, search_word, title_list):
    # start ~ end_num 크롤링
    while start_num <= end_num:
        url = ('https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}&start={}'.format(search_word, start_num))

        req = requests.get(url)
        time.sleep(1)
        if req.ok:  # 정상적인 request 확인
            soup = BeautifulSoup(req.text, 'html.parser')
            news_titles = soup.find_all('a', attrs={'class':'news_tit'})
            for news in news_titles:
                title_list.append(news['title'])
        start_num += 10
        print('title 개수:', len(title_list))
        print(title_list)


def make_wordcloud(title_list, stopwords, word_count):
    """
    stopwords : 검색어 리스트
    word_count : 단어 수
    # 1. 형태소 분석하여 리스트 .pos()
    # 2. 형태소별 count
    # 3. 불용어 제거 .pop(stopword)
    #
    """
    okt = Okt()
    sentences_tag = []
    # 형태소 분석해 리스트로
    for sentence in title_list:
        morph = okt.pos(sentence)
        sentences_tag.append(morph)
        print(morph)
        print('-'*80)
        print(tags)

    noun_adj_list = []
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective']:
                noun_adj_list.append(word)

    # 형태소별 count
    counts = Counter(noun_adj_list)
    tags =  counts.most_common(word_count)
    print('-'*80)
    print(tags)

    tag_dict = dict(tags)

    # 검색어 제외 방법 2: dict에서 해당 검색에 제거

    for stopword in stopwords:
        if stopword in tag_dict:
            tag_dict.pop(stopword)
    print(tag_dict)

    # 글씨체 변경
    path = "C:/Windows/Fonts/malgun.ttf"

    img_mask = np.array(Image.open("DATA/수업 소스/cloud.jpg"))
    wc = WordCloud(font_path=path, background_color='white', mask=img_mask,
                   width=800, height=600, max_font_size=200, repeat=True,
                   colormap = 'inferno')
    cloud = wc.generate_from_frequencies(tag_dict)
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()

if  __name__ == "__main__":
    search_word = '코로나'
    title_list = []
    stopwords = [search_word, '데이터']

    get_titles(1, 200, search_word, title_list)

    make_wordcloud(title_list, stopwords, 50)
