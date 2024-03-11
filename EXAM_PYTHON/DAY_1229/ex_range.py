# -------------------------------------------------
# range()
# - 숫자의 범위를 생성해주는 함수
# - 반환값/결과값/리턴값 : range 타입
# -------------------------------------------------
nums = range(20)
print('nums =',nums, type(nums))  # range class; range(0, 20)으로 출력
print('nums[0] =',nums[0], type(nums[0]))
print('nums[1] =',nums[1], type(nums[1]))
print('길이:',len(nums))

#슬라이싱도 가능
print('nums[:5] ->',nums[:5],type(nums[:5])) # range(0, 5) 로 출력

# range -> list 형 변환
print('list(nums) ->',list(nums))

# ------------------------------------------------------
# range ([시작값=0,] 끝값)
print(list(range(3,101,3)))