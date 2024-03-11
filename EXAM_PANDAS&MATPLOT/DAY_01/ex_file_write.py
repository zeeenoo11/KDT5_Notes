# --------------------------------------------------------
# 파일 입출력 => [출력]; 쓰기
# - 사용 내장 함수 : open(file, mode='w',encoding='지정')
# ---------------------------------------------------------
filename = 'mydata.txt'
existfile = 'message.txt'

# (1) open => 쓰기(w) 모드: 파일이 없으면 생성, 있으면 모든 내용 지움
file = open(filename, mode='w', encoding='utf-8') # mode 꼭 적어줘야함

# (2) write
file.write("123456")    # 실행 시 파일에 글 입력
file.write("123456789") # 다음 실행 시 파일 뒤에 입력
file.write('AAA\n')     # 줄바꿈도 직접해야한다
file.write("""AA
BB
CC""")                  # 입력 자체 줄바꿈은 인식

file.writelines(['7' for _ in range(10)])  # 리스트 형태로 입력 (더 번거롭)