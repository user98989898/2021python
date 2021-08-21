# 리스트
# 리스트_이름 = [요소 1, 요소 2, 요소 3, ...]

# 리스트 선언
Haedal_character = ["해달이", "시라용", "아리", "메기", "사스미"]

# 빈 리스트
mylist = []
print(mylist)

# 파이썬 리스트 특징 - 요소들의 자료형을 통일하지 않아도 됨
mylist = [1, 2, "해달이", True, ['a', 'b', 'c']]
print(mylist)

# 리스트 인덱싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[0]) #1
print(a[5]) #6
print(a[9]) #10

# 음수 인덱싱 #음수를 쓰면 뒤에서부터 -1로 시작
print(a[-1]) #10
print(a[-5]) #6

# 리스트 슬라이싱
print(a[0:3]) #1,2,3
print(a[1:3]) #2,3
print(a[:3]) #1,2,3
print(a[7:]) #8,9,10
print(a[:]) #전체
print(a[-4:-2]) #7,8 #음수는 뒤에서부터 그리고 -4에서 하나 빠져서 -3까지

# 리스트 수정 # 위에서 a는 변하지 않는데 이때 a 리스트에 자리를 바꾸는 법
a[0] = 100
print(a) #[100, 2, 3, ...]

# 리스트 삭제
del a[0]
print(a)
del a[0] # 이렇게 되면 바로 위의 a[0]이 삭제된걸 다시 a로 인식하고 거기서 다시 0번째 인덱스를 삭제한다
print(a)

del a[3:]
print(a) # 이것도 위에 40번째 줄의 a 리스트를 다시 a로 인식하고 다시 인식된 a의 0,1,2만 남기고 3부터는 다 삭제한다.

# 리스트 길이를 구하는 len()
a = [1, 2, 3, 4]
print(len(a)) # a의 전체 길이 = 안에 있는 변수 갯수로 생각 4개

# 리스트 값을 추가해주는 append()
mylist = ['a', 'b', 'c', 'd']
mylist.append('e')
print(mylist) # append 해주면 맨 마지막에 추가된다.

# 리스트의 값을 정렬해주는 sort()
mylist = [4, 2, 3, 1]
mylist.sort()
print(mylist) # 1, 2, 3, 4

mylist.sort(reverse=True)
print(mylist) # 4, 3, 2, 1
