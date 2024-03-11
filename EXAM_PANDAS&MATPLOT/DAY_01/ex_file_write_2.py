# --------------------------------------------------------
# 파일 입출력 => [출력]; 쓰기
# - 사용 내장 함수 : open(file, mode='a',encoding='지정')
# ---------------------------------------------------------
filename = 'mydata.txt'
existfile = 'message.txt'

# (1) open => 쓰기(a) 모드: append 모드; 마지막에 추가
file = open(filename, mode='a', encoding='utf-8') # mode 꼭 적어줘야함

# (2) write : mode='a' => 기존 파일 내용 맨 뒤에 입력!
file.write("123456")    # 실행 시 파일에 글 입력
file.write("123456789") # 다음 실행 시 파일 뒤에 입력
file.write('AAA\n')     # 줄바꿈도 직접해야한다
file.write("""AA
BB
CC""")                  # 입력 자체 줄바꿈은 인식

file.writelines(['1','2'])  # 리스트 형태로 입력 (더 번거롭)
                            # \n 도 직접해야한다

# (3) close
file.close()

