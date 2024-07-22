# Python 05

날짜: 2024년 7월 22일
다중 선택: No

# 자료 구조

- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠  놓은 ㄳ

## 데이터 구조의 활용

- 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 메서드를 호출하여 다양한 기능을 활용하기

# 메서드(method)

객체에 속한 함수 → 객체의 상태를 조작하거나 동작을 수행

## 메서드 특징

- 메서드는 클래스(class) 내부에 정의되는 함수
- 클래스는 파이썬에서 ‘타입을 표현하는 방법’이며 이미 은연중에 사용해왔음
- 예를 들어 help 함수를 통해 str을 호출해보면 class 였다는 것을 확인 가능

**메서드는 어딘가(클래스)에 속해 있는 함수 이며, 각 데이터 타입 별로 다양한 기능을 가진 메서드가 존재**

## 메서드 호출 방법

데이터 타입 객체. 메서드()

```python
'hello'.capitalize()
```

### 메서드 호출 예시

```python
# 문자열 메서드 예시
print('hello'.capitalize()) # Hello

# 리스트 문자열 예시
numbers = [1,2,3]
numbers.append(4)

print(numbers) # [1, 2, 3, 4]
```

# 시퀀스 데이터 구조

## 문자열

### 문자열 조회/ 탐색 및 검증 메서드

| 메서드 | 설명 |
| --- | --- |
| s.find(x) | x의   첫 번째 위치를 반환. 없으면,   -1을 반환 |
| s.index(x) | x의   첫 번째 위치를 반환. 없으면,   오류 발생 |
| s.isupper() | 대문자 여부 |
| s.islower() | 소문자 여부 |
| s.isalpha() | 알파벳 문자 여부      *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함) |

```python
# find
text = 'banana'
print('banana'.find('a')) # 1
print('banana'.find('z')) # -1

# index
print(text.index('a')) # 1
print(text.index('z')) # substring not found

# isupper
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper()) # True
print(string2.isupper()) # False

# islower
print(string1.islower()) # False
print(string2.islower()) # False

# isalpha
string1 = 'Hello'
string2 ='123heis98576ssh'
print(string1.isalpha()) # True
print(string2.isalpha()) # False
```

### 문자열 조작 메서드 ( 새 문자열 반환)

| 메서드 | 설명 |
| --- | --- |
| s.replace(old,   new[,count]) | 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 |
| s.strip([chars]) | 공백이나 특정 문자를 제거 |
| s.split(sep=None,   maxsplit=-1) | 공백이나 특정 문자를 기준으로 분리 |
| 'separator'.join(iterable) | 구분자로 iterable의 문자열을 연결한 문자열을 반환 |
| s.capitalize() | 가장   첫 번째   글자를   대문자로   변경 |
| s.title() | 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로,      나머지는 소문자로 변환 |
| s.upper() | 모두   대문자로 변경 |
| s.lower() | 모두   소문자로 변경 |
| s.swapcase() | 대↔소문자 서로 변경 |

**중요 포인트**

```python
#replace
# .replave(old, new[,count]) 
# 필수 인자는 old, new -> count는 선택 인자
# 바꿀 대상 글자를 새로운 글자로 바꿔서 전환
text = 'Hello, world! world world'
new_text = text.replace('world','python')
print(new_text) # Hello, python! python python

# 갯수를 넣치 않으면 전체를 다 바꿔버림
text = 'Hello, world! world world'
new_text = text.replace('world','python', 1)
print(new_text) # Hello, python! world world

# strip
# .strip([chars]) -> 선택 인자구나
# 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
text = '  Hello, world!  '
new_text = text.strip()
print(new_text) # Hello, world!

# split
# .split(sep=None, maxsplit=-1)
# 지정한 문자를 구분자로 문자열을 분리하여 문자열의 리스트로 반환
text = 'Hello, world!'
words = text.split(',')
words2 = text.split()
print(words) # ['Hello', ' world!'], world 앞에 공백 주의
print(words2) # ['Hello,', 'world!'], python 뒤에 , 붙음

# join
# 'sperator'.join(iterable)
# iterable의 문자열을 연결한 문자열을 반환
# split과 반대의 동작 수행
words = ['Hello', 'world!']
new_text = '-'.join(words) # Hello-world!
print(new_text)
```

**참고 포인트**

```python
# capitalize
text = 'heLLo, woRld!' 
new_text1 = text.capitalize()
print(new_text1) # Hello, world! -> 맨 앞을 대문자로 변경 후 뒤는 소문자로 변경

# title
new_text2 = text.title()
print(new_text2) # Hello, World! w도 대문자 처리함 -> 공백 기준으로 대문자

# upper
new_text3 = text.upper()
print(new_text3) # HELLO, WORLD!

# lower
new_text4 = text.lower()
print(new_text4) # hello, world!

# swapcase
new_text5 = text.swapcase()
print(new_text5) # HEllO, WOrLD!
```

## 리스트

| 메서드 | 설명 |
| --- | --- |
| L.append(x) | 리스트   마지막에 항목 x를   추가 |
| L.extend(m) | Iterable m의   모든 항목들을 리스트 끝에 추가 (+=과   같은 기능) |
| L.insert(i,   x) | 리스트   인덱스 i에 항목 x를 삽입 |
| L.remove(x) | 리스트   가장 왼쪽에 있는 항목(첫 번째)   x를   제거     항목이 존재하지 않을 경우,   ValueError |
| L.pop() | 리스트   가장 오른쪽에 있는 항목(마지막)을   반환 후 제거 |
| L.pop(i) | 리스트의 인덱스 i에   있는 항목을 반환 후 제거 |
| L.clear() | 리스트의 모든 항목 삭제 |

### 리스트 메소드 예시

```python
# append
# .append 
# 리스트 마지막에 항목 x를 추가
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # [1, 2, 3, 4]
print(my_list.append(4)) # None -> append의 반환 값이 없음

# extend
# .extend(iterable)
# 리스트에 반복 가능한 객체의 모든 항목을 추가
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6]

# my_list.extend(5) 
# print(my_list) # 'int' object is not iterable -> 오류 발생

my_list.extend([5])
print(my_list) # [1, 2, 3, 4, 5, 6, 5]

my_list.append([9, 9, 9])
print(my_list) # [1, 2, 3, 4, 5, 6, 5, [9, 9, 9]]

# my_list.append([9,9,9], 1, 2)
# print(my_list) # list.append() takes exactly one argument (3 given) 

# insert
# .insert(i, x)
# 리스트의 지정한 인덱스 i 위치에 항목 x를 삽입
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list) # [1, 5, 2, 3]

# remove
# .remove(x)
# 리스트에서 첫 번째로 일치하는 항목을 삭제
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list) # [1, 3, 2, 2, 2]

# pop
# .pop(i)
# 리스트에서 지정한 인덱스의 항목을 제거하고 반환
# 작성하지 않을 경우 마지막 항목을 제거
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
print(item1) # 5
print(my_list) # [1, 2, 3, 4]

item2 = my_list.pop(0)
print(item2) # 1
print(my_list) # [2, 3, 4]

# clear
# .clear()
# 리스트이 모든 항목을 삭제
my_list = [1, 2, 3]
my_list.clear()
print(my_list) # [] 
```

### 리스트 탐색 및 정렬 메서드

| 문법 | 설명 |
| --- | --- |
| L.index(x) | 리스트에   있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 |
| L.count(x) | 리스트에서 항목   x의 개수를 반환 |
| L.reverse() | 리스트의 순서를 역순으로 변경 (정렬 X) |
| L.sort() | 리스트를 정렬 (매개변수   이용가능) |

### 예시

```python
# index
my_list = [1, 2, 3]
index = my_list.index(3)
print(index) # 2

# count
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print((counting_number)) # 3

# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list.reverse()) # None -> reverse의 반환값은 없음
print(my_list) # [1, 3, 2, 8, 1, 9]

# sort
# .sort()
# 원본 리스트를 오름차순으로 정렬
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list) # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse= True)
print(my_list) # [100, 3, 2, 1]
```

# 복사

## 데이터 타입과 복사

- 파이썬에서는 데이터에 분류에 따라 복사가 달라짐
- “변경 가능한 데이터 타임”과 “변경 불가능한 데이터 타입”을 다르게 다룸

## 복사 유형

- 할당
- 얕은 복사
- 깊은 복사

### 할당

```python
# 할당
# 가변데이터 예시
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a) # [100, 2, 3, 4]
print(b) # [100, 3, 2, 1]

# 불변 데이터 예시
a = 20 
b = a
b = 10 

print(a) # 20 
print(b) # 10
```

### 얕은 복사 & 깊은 복사

```python
# 얕은 복사
a = [1, 2, 3]
b = a[:]
c = a.copy()

b[0] = 100 
c[0] = 999
print(a) # [1, 2, 3]
print(b) # [100, 2, 3]
print(c) # [999, 2, 3]

# 얕은 복사의 한계
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
b[2][1] = 100 # 중첩된 리스트 주소 값은 걍 변해버림
print(a) # [1, 2, [3, 100, 5]] 
print(b) # [999, 2, [3, 100, 5]]

# 깊은 복사
# 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함
import copy
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100
print(a) # [1, 2, [3, 4, 5]]
print(b) # [1, 2, [3, 100, 5]]

```

# 문자 유형 판별 메소드

## 문자열에 포함된 문자들의 유형을 판별하는 메서드

| isdecimal() | isdigit() | isnumeric() | 예시 |
| --- | --- | --- | --- |
| True | True | True | "038",   "੦੩੮",   "０３８" |
| False | True | True | "⁰³⁸", "🄀⒊⒏", "⓪③⑧" |
| False | False | True | "⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "壹貳參" |
| False | False | False | "abc", "38.0", "-38" |

```python
# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal()) # True
print("'123.45'.isdecimal():", '123.45'.isdecimal()) # False
print("'-123'.isdecimal():", '-123'.isdecimal()) # False
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal()) # False
print("'½'.isdecimal():", '½'.isdecimal()) # False
print("'²'.isdecimal():", '²'.isdecimal()) # False
print()

# isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit()) # True
print("'123.45'.isdigit():", '123.45'.isdigit())  # False
print("'-123'.isdigit():", '-123'.isdigit()) # False
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit()) # False
print("'½'.isdigit():", '½'.isdigit()) # False
print("'²'.isdigit():", '²'.isdigit()) # True # 지수표현 
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric()) # True
print("'123.45'.isnumeric():", '123.45'.isnumeric()) # False
print("'-123'.isnumeric():", '-123'.isnumeric()) # False
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric()) # True
print("'½'.isnumeric():", '½'.isnumeric()) # True
print("'²'.isnumeric():", '²'.isnumeric()) # True

```

### 문자열 조회/탐색 및 검증 메서드

| 메서드 | 설명 |
| --- | --- |
| s.find(x) | x의   첫 번째 위치를 반환. 없으면,   -1을 반환 |
| s.index(x) | x의   첫 번째 위치를 반환. 없으면,   오류 발생 |
| s.isupper() | 대문자 여부 |
| s.islower() | 소문자 여부 |
| s.isalpha() | 알파벳 문자 여부      *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함) |

### 문자열 조작 메서드 (새 문자열 반환)

| 메서드 | 설명 |
| --- | --- |
| s.replace(old,   new[,count]) | 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 |
| s.strip([chars]) | 공백이나 특정 문자를 제거 |
| s.split(sep=None,   maxsplit=-1) | 공백이나 특정 문자를 기준으로 분리 |
| 'separator'.join(iterable) | 구분자로 iterable의 문자열을 연결한 문자열을 반환 |
| s.capitalize() | 가장   첫 번째   글자를   대문자로   변경 |
| s.title() | 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로,      나머지는 소문자로 변환 |
| s.upper() | 모두   대문자로 변경 |
| s.lower() | 모두   소문자로 변경 |
| s.swapcase() | 대↔소문자 서로 변경 |

과제 2문제/ level 1,2,3 → 2가지 방법