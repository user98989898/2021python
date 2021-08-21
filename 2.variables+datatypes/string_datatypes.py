# 기본 문자열
s2 = 'Hello, Haedal!'
print(s2)

S2 = "Hello, Haedal!"
print(S2)

s6 = '''Hello, Haedal!'''
print(s6)

S6 = """Hello, Haedal!"""
print(S6)
# 각 문자열이 실제로 의미하는 것(?)은 각각 다르나 출력은 동일하게 된다.

# 문자열 안에 엔터를 칠 수 있는가? -> 이스케이프 코드
# 이스케이프 코드 \n, \t, \\, \', \"
longtext1 = """Hello, Haedal!
My name is Programming.""" #큰따움표 세개는 문자열 내에서 그냥 enter을 쳐도 먹는다.
print(longtext1)

longtext2 = 'Hello, Haedal!\nMy name is Programming.' #작은 따움표 일때는 enter가 안먹는다. 그래서 대신 \n을 쳐줘야한다.
print(longtext2)

# String Interpolation
a = 123
new_q = f'{a}'
print(new_q)

# 문자열 옛날 방식
# f'%s %s' % ('one', 'two')
print(f'%s %s' % ('one', 'two'))

# pyformat
# '{}' '{}'. format('one', 'two')
print('{} {}'. format('one', 'two'))

# f-string
a, b = 'one', 'two' #변수를 한꺼번에 선언 가능
# f'{a}, {b}'
print(f'{a} {b}')
print(f'{b} {a}')


# example
name = "줴윤"
eng_name = "Jae Yun"
print("안녕하세요. {1}입니다. My name is {0}". format(eng_name, name))
print("안녕하세요. {}입니다. My name is {}". format(name, eng_name))
print(f'안녕하세요. {name}입니다.')

# 문자열 인덱싱
a = "Hello, Haedal!"
print(a[1]) #a[0]은 H이고 a[1]은 e라서 e가 출력된다.

# 문자열 슬라이싱
a = "Hello, Haedal!"
print(a[4:9]) #4부터 8까지 출력

# 문자열의 길이를 구하는 len()
a = "Hello, Haedal!"
print(len(a))

# 문자열의 최대, 최소를 구하는 max(), min()
# 아스키코드를 따른다
a = '312'
b = 'bac'
print(min(a))
print(max(a))
print(min(b))
print(max(b))
print(a+b) #문자열에서 +는 문자열을 그대로 붙인다.
print(min(a+b)) #아스키코드에서 숫자가 더 앞에 있어서(부여된 값이 더 작아서) min하면 1이 나온다.
print(max(a+b))

# 소문자, 대문자로 변환해주는 lower(), upper()
a = 'This is Apple'
print(a.upper())
print(a.lower())

# 문자열을 구분자에 따라 나누는 split()
a = "안녕,나는,해달이야"
print(a.split(sep=',')) #split하게 되면 해당하는 문자마다 잘라서 리스트 요소들로 저장

b = "안녕 나는 해달이야"
print(b.split()) #빈칸으로 두게 되면 띄어쓰기에서 split한다.

# 여러개의 문자열 사이에 구분자를 넣어주는 join()
mylist = ['안녕', '나는', '해달이야']
mystring = ['_'.join(mylist)]
print(mystring)
