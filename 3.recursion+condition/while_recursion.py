# for와 while의 차이
# for문은 정해진 횟수만큼 돌린다.
# while문은 정해진 조건이 참인 경우만큼 돌린다.


# while문 기초
it = 0
while it < 5:
    it += 1     #it이 1부터 하나씩 커질텐데 5보다 작을때까지 while문을 돌린다.
    print(it)


# while문 구조
# while 조건:
#     반복할 명령어1
#     반복할 명령어2


# while 무한루프
it = 0
while True:
    it += 1
    print(it)   #실행 끝낼려면 ctrl+c


# while 무한루프 + break
ti = 0
while True:
    ti += 1
    print(ti)
    if ti>500:
        break   # 위에 it는 ctrl+/로 주석처리해서 비활성화하고 돌려야겠지?