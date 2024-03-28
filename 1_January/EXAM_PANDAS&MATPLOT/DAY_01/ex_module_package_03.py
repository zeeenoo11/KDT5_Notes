# --------------------------------------
# 패키지 사용법
# --------------------------------------
# import 패키지명.모듈명
import urllib.request as req          # 패키지에서 모듈 가져오기 + 별칭

# from 패키지명 import 모듈명
from urllib import error, parse
from http.client import HTTPResponse  # HTTPResponse : class만 가져온 것

dataObj = req.urlopen("https://www.google.co.kr/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")

print(dataObj)