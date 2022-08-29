# 도미dataSet http://bit.ly/bream_lsit
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

# 여러개의 종류(클래스) 중 하나를 구별 <- 분류(classification)
# 2개의 클래스 중 하나를 고르는 문제 <- 이진분류(binary classification)
# 데이터의 특징 <- 특성
# 산점도 <- x,y축으로 이루어진 좌표계에 두 변수(x,y)의 관계를 표현하는 방법이다.
# matplotlib <- 파이썬에서 과학계산용 그래프를 그리는 대표적인 패키지
# import <- 미리 만들어둔 파이썬 패키지(함수 묶음)을 사용하기 위해 불러오는 명령어
import matplotlib.pyplot as plt # matplotlib의 pyplot함수를 plt로 줄여서 명명

plt.scatter(bream_length, bream_weight)
plt.xlabel("length") # x축은 길이
plt.ylabel("weight") # y축은 무게
plt.show()
# 산점도 그래프가 일직선에 가까운 형태로 나타나는 경우 <- 선형적(linear)이라 한다.

# 빙어dataSet http://bit.ly/smelt_list
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel("length")
plt.ylabel("weight")
plt.show()