# ------------------------------------------------------------
# 30장 : 네 과목의 점수를 입력하여 가장 높은/낮은 점수, 평균점수(실수)를 출력
# ------------------------------------------------------------
korean, english, mathematics, science = map(int, input().split())  # 교재 제시 : 네 과목 점수 입력

def get_min_max_score(*args):
    return min(args), max(args)               # 값들의 최소, 최대값 산정 및 반환

def get_average(**kwargs):
    return sum(kwargs.values())/len(kwargs)   # 키=값 형식으로 입력, 값의 합과 전체 갯수 나눔

# 아래 : 교재 제시
min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))


