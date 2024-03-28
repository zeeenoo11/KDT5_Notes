# -------------------------------------------------------
# 26장 : 양의 두 정수 입력, 두 수의 공약수를 세트 형태로 구하기
#        최종 결과는 공약수의 합으로 판단
# -------------------------------------------------------
inputA, inputB = map(int, input().split())
a = set(a for a in range(inputA,0,-1) if not inputA%a)     # a1의 약수 구하기
b = set(b for b in range(inputB,0,-1) if not inputB%b)     # b1의 약수 구하기

divisor = a & b         # a, b 에 모두 존재하는 원소만 divisor에 입력

result = 0
if type(divisor) == set:
    result = sum(divisor)   # divisor의 타입이 set라면 합계를 구함

print(result)