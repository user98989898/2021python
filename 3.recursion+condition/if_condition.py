# 조건문 : 특정 조건을 만족할 때 명령어를 수행하자.
# if, if-elif-else

# 시험 점수에 따른 과락 분류
score = int(input('점수를 입력하세요    ')) # input으로 우리가 정보 입력 가능
if score>=70:
    result = '통과'
else:
    result = '과락'
print(result)


# if문의 구조
# if 조건문 :
#     실행할 코드1
#     실행할 코드2
# if문 탈출 후 코드1
