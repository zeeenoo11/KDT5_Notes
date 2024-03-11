# ------------------------------------------
# 파일 하나 선택 후 복사본 파일 생성하기
# - 예) message.txt ===> message_copy.txt
# ------------------------------------------

# with 안쓰고 해보기
# file_r = open('message.txt', mode='r',encoding='utf-8')
# file_copy = file_r.read()
#
# file_w = open('message_copy.txt', mode='w',encoding='utf-8')
#
# file_w.write(file_copy)

# with
with open('message.txt', mode='r',encoding='utf-8') as f_r:
    data = f_r.read()   # 내용 읽고 저장

with open('message_copy.txt', mode='w',encoding='utf-8') as f_w:
    f_w.write(data)     # 복사본에 내용 쓰기

# ----------------------------------------------------------------
# 원본 파일에 내용 읽은 후 저장 (한번에!)
with open('message.txt', mode='r',encoding='utf-8') as f_r:
    with open('message_copy.txt', mode='w', encoding='utf-8') as f_w:
        f_w.write((f_r.read()))
