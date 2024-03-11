# -------------------------------------------
# filter(func., iterables)
# - 조건(함수)에 맞는 데이터만 반환
# -------------------------------------------
# 5초과 10미만
import random
import functools
# from random import randint : randint만 가져오기

randList = [random.randint(1,10) for a in range(10)]
print(randList)

# 1. check 함수: 원하는 조건을 반환
def check(data):
    return data > 5 and data < 10

filterList = list(filter(check, randList))  # 각 원소를 T or F로 인식
print(filterList)                           # 불린 인덱싱

# 2. 람다!
filterList_L = list(filter(lambda x:5<x<10,randList))
print(filterList_L)


# Reduce : 누적 반복 함수
randList2 = [random.randint(1,10) for cnt in range(10)]
print(randList)

print(functools.reduce(lambda x,y:x+y, randList2))
# print(functools.reduce(lambda x:x**2, randList2))