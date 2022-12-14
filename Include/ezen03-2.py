# ezen03-2
# 파이썬 데이터 타입 (자료형)
# 문자열, 문자열 연산, 인덱싱, 슬라이싱

# 문자열 생성
str1 = "Happy new year"
str2 = "NiceYear"
str3 = """What is the name of this car?"""
str4 = '''Thank you!'''

# 문자열 타입 출력
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 문자열 인덱싱(indexing) : 문자열에 포함된 특정한 하나의 문자를 얻을 수 있음. 첫 번째 문자는 인덱스 0에 해당함
a= "Hello"
print(a[0])
print(a[3])

# 문자열 슬라이싱(slicing) : 부분 문자열 (substring)을 얻기 위해 사용
# - 슬라이싱은 두 개의 인덱스로 구성됨. 변수명[시작 인덱스 : 끝 인덱스]

a = "Hello World"
# 인덱스 3까지의 접두사를 가져오시오.
print(a[:4])

# 인덱스 2부터의 접미사 가져오시오.
print(a[2:])

# 중간에 있는 부분 문자열 가져오시오.
# orl
print(a[7:10])

# 문자열 인덱싱 시 범위를 벗어난 경우 오류 발생/ 슬라이싱의 경우 부드럽게 처리됨
# print(a[30])
print(a[2:50])

# 파이썬에서 문자열은 값을 변경할 수 없기 때문에, 불변(immutable) 객체라고도 함
a[3] = 'b' #오류 발생
