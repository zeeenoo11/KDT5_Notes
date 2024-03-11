

# ======== < 자연어 처리 라이브러리 > ========
from konlpy.tag import Okt

okt = Okt()
text = ''
# pos(text) : 문장의 각 품사를 태깅
# norm=True : 문장 정규화, stem=True : 어간 추출 (보다, 보니, 보고 -> 어간 : 보)
okt_tags = okt.pos(text, norm=True, stem=True)
# nouns(text) : 명사만 리턴
okt_nouns = okt.nouns(text)