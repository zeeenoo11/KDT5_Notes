import matplotlib.pyplot as plt 
import koreanize_matplotlib

plt. plot ([-1, 0, 1, 2])
plt.title('그래프 제목', fontweight="bold")
plt.xlabel('간단한 그래프')
plt. show()

# -----------------------------------------
# csv 파일 함수
import csv

f = open('Daegu-utf8.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter=',')
print(data)
f.close()