# ---------------------------------------------------------
# 파일 입출력 => [출력]; 읽기
# - 사용 내장 함수 : open()
# - Offset : 글을 읽는 지점
# ----------------------------------------------------------
# (1) Open
file = open('message.txt', encoding='utf8')
print(type(file)) # <class '_io.TextIOWrapper'>
print(file.name)  # message.txt

# (2) IO => .Read() : 파일 안의 모든 내용을 읽어옴
fdata = file.read()
print(type(fdata))    # <class 'str'>
print(fdata)          # 파일 내용이 그대로 출력됨

# (2-2) IO => .Read(n) : 지정된 수 만큼 문자를 읽어오기
fdata = file.read(5)  # PANDA     : 처음부터 5글자를 출력
print(type(fdata))
print(fdata)          # (2)에서 .read를 한 경우:
                      # 읽는 지점이 마지막으로 가 있어서 출력x

# (2-3) IO => .readline() : \n 기준 한 줄 읽어오기
datas = []
while True:          # 전체 출력: 반복문
    fline = file.readline()
    if not fline: break              # fline 끝나면(None) 반복 종료
    print(type(fline),fline,end='')  # \n 기준: end 해야 한번만 줄바꿈됨
    datas.append(fline)              # 데이터 활용 위해 저장
print(datas)

# (2-4) IO => readlines() : 한 줄씩 읽는 걸 한번에 모아줌
datas = file.readlines()
print(datas)  # ['PANDAS\n', 'BAMBOOS\n', '\n', '하늘 눈\n', '\n', '123456']

# <class 'str'> S
# <class 'str'> BAMBOOS
# <class 'str'>
# <class 'str'> 하늘 눈
# <class 'str'>
# <class 'str'> 123456
# print(datas) => ['S\n', 'BAMBOOS\n', '\n', '하늘 눈\n', '\n', '123456']


# (3) close
file.close()