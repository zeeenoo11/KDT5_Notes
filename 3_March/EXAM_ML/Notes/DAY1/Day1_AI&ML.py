
# DAY1 폴더 내의 모든 문장을 한 파일에 저장하기


with open('DAY1/0', 'r', encoding='utf-8') as f:
    with open('total.py', 'a', encoding='utf-8') as a:
        file = f.read()
        a.write(file)

