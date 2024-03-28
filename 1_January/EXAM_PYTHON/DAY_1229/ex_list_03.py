# --------------------------------------------------------
# list의 원소 데이터 변경 및 삭제
# --------------------------------------------------------
# "Merry Christmas"의 문자 1개 1개를 원소로 가지는 리스트
wordlist = list("Merry Christmas")
print('wordlist :', wordlist)

# ' ' 를 '***'로 변경
wordlist[wordlist.index(' ')] = '***'
print('replaced list :', wordlist)


# 삭제 -> del element 또는 del(element)
del wordlist[5]              # *** 삭제
del(wordlist[5])             # C 삭제
print('deleted list :', wordlist)
del wordlist                                 # 리스트 자체 지우기도 가능