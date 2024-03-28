
# food.txt 의 내용을 분류하여 저장하기

file = 'food.txt'

kor_food, chin_food = [], []
food = {}
kind,key = '', ''
with open(file, mode='r', encoding='utf-8') as f:
    data = f.readline()
    if not data.find('['):  # [ 를 포함한다면
        kind = '한식' if data[1:] == '한식' else '중식'
    else:
        if kind == '한식': kor_food.append(data)
        else: chin_food.append(data)

# 여러 분류가 있을 때
with open(file, mode='r', encoding='utf-8') as f:
    data = f.readline()
    for msg in data:
        if not data.find('['):  # [ 를 포함한다면
            key = data[1:]      # [ 이후의 문자열 전체를 키로 넣고
            food[data[1:]]=[]   # 딕셔너리에 키로 저장
        else:
            food[key].append(data[:-1])  # 저장한 키 값에 다음 [ 나오기 전까지의 문자 넣기
            # [:-1]하면 \n 제거
    print(data)