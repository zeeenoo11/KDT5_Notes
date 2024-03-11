#

filename = 'message.txt'

with open(filename,mode='r', encoding='utf-8') as f:
    f.seek(5)                           # 처음부터 5칸을 이동
    print(f.read(10))                   # 거기서 10만큼 읽고 출력
    print(f'현재 위치: {f.tell()}')     # 현재 위치 : 17
    print(f.name, f.closed)             # message.txt False

    f.seek(0)                           # 처음으로 돌아감
    print(f.read(5))                    # PANDA
    print(f'현재 위치: {f.tell()}')     # 현재 위치: 5

print(f.name, f.closed)             # message.txt True

# .closed 차이 : with 밖을 나가면 닫힘; with 내외부 차이

# csv, json 등 다양한 파일을 읽어야함: 한줄씩 읽으면서 필요한 정보 빼내기
# 모듈 활용