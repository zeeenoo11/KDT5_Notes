

# <파일과 예외 처리> 파이썬 보충
# --------------------------------------------------------
# 1. 위치 표시자
#   - 파일의 입출력 동작이 발생하는 위치를 나타냄
#   - 파일 끝엔 항상 EOF(End of  File)이 있음
#   - EOF를 만나면 '' 를 반환

# 2. .read() 사용
#
'''
filename1 = input("원본 파일 이름을 입력하시오: ")
filename2 = input("복사 파일 이름을 입력하시오: ")

infile = open(filename1, "rb")
outfile = open(filename2, "wb")

# 입력 파일에서 1024 바이트씩 읽어서 출력 파일에 쓴다.
# 파일의 마지막 부분에서는 읽어 들인 바이트 수만큼 파일에 저장
while True:
    copy_buffer = infile.read(1024)
    print(len(copy_buffer)) # 실제 읽어온 바이트 수 출력
    if not copy_buffer: # 파일의 끝인 경우, empty byte를 리턴
        break
    outfile.write(copy_buffer)

infile.close()
outfile.close()
print(filename1+"를 " + filename2 +"로 복사하였습니다. ")
'''
# 3. pickle 모듈
# - 객체를 읽고 쓰는 모듈
# -  어떤 형식이든 바이너리 변환 후 딕셔너리 형태로 저장
# - pickle.dump :
# - pickle.load

# 4. 예외 처리
# try:
#   예외 발생 가능 문장
# except (---- Error):
#   예외를 처리하는 문장 ex. print('0으로 나누는 에러')

# Exception : 최상위 에러문
'''
x=2; y=0
try:
    z = x / y
except ZeroDivisionError as e:
    print(e)
'''
# 4-2. IOError
#   - 파일명을 못 찾는 오류


filename = input("파일명을 입력하세요: ").strip()
infile = open(filename,	"r")

freqs =	{}	  #	딕셔너리 생성

# 파일의 각 줄에서 문자를 추출한 다음 각 문자를 dict에 추가
for	line in	infile:
    for	char in line.strip():
        if	char in freqs:
            freqs[char]	+=	1  # 딕셔너리에 key(char)가 있으면 증가
        else:
            freqs[char]	= 1  # 딕셔너리에 key(char)가 없으면 추가
print(freqs)
infile.close()