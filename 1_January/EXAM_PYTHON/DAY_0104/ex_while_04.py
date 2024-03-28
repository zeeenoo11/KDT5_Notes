# -----------------------------------------------
# continue
# - 키워드 아래 코드는 실행 안됨
# - 반복 상단으로 이동
# -----------------------------------------------
# 1~30 요소의 리스트 중 짝수만 화면에 출력
numlist = list(range(1,31))

for data in numlist:
    if not data%2:
        print(data)  # 짝수일때만 실행
print()

for data in numlist:
    if data%2:
        continue    # 홀수면 for로 돌아간다
    print(data)     # continue 지나면 여기로 안옴!
print()

# while로 풀어보기
index = 0
while index < 30:
    if numlist[index]%2:
        index += 1
        continue
    print(numlist[index])
    index += 1