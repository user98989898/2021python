# for문 무작정 따라해보기
for i in range (1, 11): # i의 범위는 1부터 10까지 반복
    if(i%2 == 0):
        print(i, "은/는 짝수입니다.")
    else:
        print(i, "은/는 홀수입니다.")
# for, if, else 뒤에는 :을 붙여야한다.

# for문의 구조
# for i in 범위:
#     반복할 명령어1
#     반복할 명령어2

# for문 with list
mylist = ['해달이', '사스미', '메기']
for i in mylist:
    print(i)
print("반복 끝")

# for문 with range
print(range(1, 11)) #range(1,11)이 그대로 출력된다. 1부터 11까지의 수가 보고싶으면 아래처럼 list 사용 필요
print(list(range(1, 11)))
print(list(range(10))) # 시작점을 설정안해주면 0부터 시작
print(list(range(1, 20, 3))) # 1부터 19까지 3칸씩 띄어가면서
print(list(range(20, 0, -3))) # 20부터 1까지 반대로 -3칸씩 띄어가면서

# for문 with range
for i in range(1, 11):
    print(i, end=" ") # 1부터 range범위 끝까지 space 한칸 띄우면서 (1부터 10까지)
print('반복 끝')
