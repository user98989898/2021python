# for문 속 for문 / 이중 for문

for i in range (5):
    for j in range(1, 11):
        print(j, end=" ") # 5번째줄 이 print는 j for문에 적용
    print() # 6번째줄 이 print는 i for문에 적용
