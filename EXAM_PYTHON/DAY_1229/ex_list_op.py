
twoNums = list(range(2,10,2))

# 산술 연산 + *
print(twoNums + ["A", "B"])

datas = twoNums + ["A", "B"]
print(datas)

# list + str
# print(twoNums + "ABC")      # 에러 발생; 같은 리스트끼리만 가능
print(str(twoNums) + 'ABC')   # [1, 2, 3] 자체가 하나의 문자열이 됨!

# 곱셈: list * int ; int만큼 반복
print(twoNums * 3)

# -------------------------------------------------------------
# 멤버 연산 (not) in
# -------------------------------------------------------------
print('C' in datas)