# 23장 -----------------------------------------------
# 문제 : 2차원 리스트의 가로(col)와 세로(row)가 입력
#        그 다음 줄부터 문자가 리스트의 요소로 입력됨
#        * : 지뢰, . : 지뢰가 아님
#        지뢰가 아닌 요소엔 인접한 지뢰의 개수를 출력하는 프로그램
# -----------------------------------------------------
col, row = map(int, input().split())              # 1. 행과 열의 크기를 입력합니다.

matrix = []                                      # 2. 지뢰의 위치를 '.' 과 '*'로 입력합니다.
for i in range(row):
    matrix.append(list(input()))
print()

memory_index = []                            # 3.2.1 "*" 주변 8칸의 인덱스를 기록합니다.
for row_memory in range(row):
    for col_memory in range(col):            # 하나씩 검사
        if matrix[row_memory][col_memory] == '*':     # "*" 이라면
            memory_index += [(a,b) for a in range(row_memory-1,row_memory+2) for b in range(col_memory-1,col_memory+2)]
            # 주변 8칸의 인덱스를 저장; (-1,-1),(-1,0),(-1,+1),...

for row_final in range(row):                 # 3.2.2 "." 에 카운팅 수 입력
    for col_final in range(col):
        if matrix[row_final][col_final] == '.':
            matrix[row_final][col_final] = memory_index.count((row_final,col_final))

print("<지뢰 찾기 결과>")    # 4 표현하기
for i in range(row):
    for b in matrix[i]:
        print(b,end=' ')
    print()