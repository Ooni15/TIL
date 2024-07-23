# Python 06

날짜: 2024년 7월 23일

# 비시퀀스 데이터 구조

## 딕셔너리

고유한 항목들의 정렬되지 않은 컬렉션 (Key 중복이 되지 않음 + 순서 X)

### 딕셔너리 메서드

| 메서드 | 설명 |
| --- | --- |
| D.clear() | 딕셔너리 D의   모든 키/값 쌍을 제거 |
| D.get(k) | 키 k에   연결된 값을 반환 (키가 없으면 None을 반환) |
| D.get(k,   v) | 키 k에   연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환 |
| D.keys() | 딕셔너리 D의   키를 모은 객체를 반환 |
| D.values() | 딕셔너리 D의   값을 모은 객체를 반환 |
| D.items() | 딕셔너리 D의   키/값 쌍을 모은 객체를 반환 |
| D.pop(k) | 딕셔너리 D에서   키 k를 제거하고 연결됐던 값을 반환 (없으면   오류) |
| D.pop(k,   v) | 딕셔너리 D에서   키 k를 제거하고 연결됐던 값을 반환 (없으면   v를 반환) |
| D.setdefault(k) | 딕셔너리 D에서   키 k와 연결된 값을 반환 |
| D.setdefault(k,   v) | 딕셔너리 D에서   키 k와 연결된 값을 반환     k가   D의 키가 아니면 값 v와   연결한 키 k를 D에   추가하고 v를 반환 |
| D.update(other) | other 내 각 키에 대해 D에   있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체.  other에 있는 각 키에 대해 D에   없는 키면 키/값 쌍을 D에   추가 |

```python
# clear
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person) # {}

# get
# .get(key[,defualt])
# 키 연결된 값을 반환하거나 키가 없으면 None 혹은 기본 값을 반환 (dict[key]와 다른 포인트)
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))  # Alice
print(person.get('country')) # None
print(person.get('country', 'unknown')) # unknown (반환값 설정)
#print(person['country']) # KeyError: 'country'

# keys
# 딕셔너리 키를 모은 객체를 반환
person = {'name': 'Alice', 'age': 25}
print(person.keys()) # dict_keys(['name', 'age'])

for item in person.keys() : 
    print(item) 

'''
name
age

'''

# values
person = {'name': 'Alice', 'age': 25}
print(person.values()) # dict_values(['Alice', 25])

for item in person.values() :
    print(item)
'''
Alice
25
'''

# items
# 딕셔너리 키/값 쌍을 모은 객체를 반환 -> 튜플 형태로 나옴
person = {'name': 'Alice', 'age': 25}
print(person.items()) # dict_items([('name', 'Alice'), ('age', 25)])

# 언패킹 하기
for key, value in person.items() :
    print(key,value)

'''
name Alice
age 25
'''
    

# pop
# .pop(key[,default])
# 키를 제거하고 연결됐던 겂을 반환 (없으면 에러나 default를 반환)
person = {'name': 'Alice', 'age': 25}
print(person.pop('age')) # 25
print(person) # {'name': 'Alice'}
print(person.pop('country',None)) # None
#print(person.pop('country')) # KeyError: 'country'

# setdefault
# .setdefualt(key[,default])
# 키와 연결된 값을 반환
# 키가 없다면 defualt와 연결된 키를 딕셔너리에 추가하고 defualt를 반환
# 이거를 알면 조건문 없이 딕셔너리 추가 가능
person = {'name': 'Alice', 'age': 25} 
print(person.setdefault('country', 'KOREA')) # KOREA
print(person) # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

# update
# .update([other])
# other가 제공하는 키/값 쌍으로 딕셔너리를 갱신
# 기존 키는 덮어씀
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

person.update(age = 100, country = 'KOREA')
print(person) # {'name': 'Jane', 'age': 100, 'gender': 'Female', 'country': 'KOREA'}

# 깊은 복사가 되는가?

a = {} # a와 b 각각 메모리 주소를 갖고 출동
b = {'name': 'Alice', 'age': 25} 

a.update(b)
print(a) # {'name': 'Alice', 'age': 25}
b['name'] = 'Harry'

print(a) # {'name': 'Alice', 'age': 25}
```

## 세트

고유한 항목들의 정렬되지 않은 컬렉션 (중복, 순서 X)

### 세트 메서드

| 메서드 | 설명 |
| --- | --- |
| s.add(x) | 세트 s에 항목   x를 추가. 이미   x가 있다면 변화 없음 |
| s.clear() | 세트 s의   모든 항목을   제거 |
| s.remove(x) | 세트 s에서   항목 x를 제거. 항목   x가 없을 경우 Key error |
| s.pop() | 세트 s에서   랜덤하게 항목을 반환하고,   해당 항목을 제거 |
| s.discard(x) | 세트 s에서   항목 x를 제거 |
| s.update(iterable) | 세트 s에   다른 iterable 요소를   추가 |

```python
# add
# 순서 없는 거 확인하기
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set) # {'b', 1, 2, 3, 4, 'c', 'a'}

my_set.add(4)
print(my_set) # {'b', 'a', 3, 2, 1, 'c', 4} 4가 두번 추가 되지는 않음

# clear
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set) # set()

# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2) # {1, 3, 'a', 'c', 'b'}
print(my_set)

# my_set.remove(10)
# print(my_set) # KeyError: 10

# pop
# 세트에서 임의의 요소를 제거하고 반환
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element) # 1 랜덤으로 빠짐

# discard
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set) # {1, 3, 'c', 'a', 'b'}
my_set.discard(10) # 오류가 발생하지 않는다.

# update
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5])
print(my_set) # {1, 2, 3, 'b', 4, 5, 'c', 'a'
```

### 세트의 집합 메서드

| 메서드 | 설명 | 연산자 |
| --- | --- | --- |
| set1.difference(set2) | set1에는 들어있지만 set2에는      없는   항목으로 세트를 생성 후 반환 | set1   – set2 |
| set1.intersection(set2) | set1과 set2 모두   들어있는 항목으로 세트를   생성 후 반환 | set1   & set 2 |
| set1.issubset(set2) | set1의 항목이 모두 set2에 들어있으면 True를   반환 | set1   <= set2 |
| set1.issuperset(set2) | set1가 set2의   항목을 모두 포함하면 True를   반환 | set1   >= set2 |
| set1.union(set2) | set1 또는 set2에(혹은   둘 다) 들어있는 항목으로   세트를 생성 후 반환 | set1   | set2 |

```python
# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) # {0, 2, 4}
print(set1.intersection(set2)) # {1, 3}
print(set1.issubset(set2)) # False
print(set3.issubset(set1)) # True
print(set1.issuperset(set2))  # False
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}
```

# 해시 테이블

해시 함수를 사용하여 변환한 값을 색인(index)으로 삼아 키(Key)와 데이터(Value)를 저장하는 자료구조

→ 데이터를 효율적으로 저장하고 검색하기 위해 사용

## 해시 테이블 원리

- 키를 해시 함수를 통해 해시 값으로 변환하고, 이 해시 값을 인덱스로 사용하여 데이터를 저장하거나 검색
    - 데이터 검색이 매우 빠르게 이루어짐
    - 파이썬이 재실행 할 때마다 갱신

## 해시 (Hash)

- 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것
- 이렇게 생성된 고유한 값은 주로 해당 데이터를 식별하는 데 사용될 수 있음
    - 일종의 “지문”과 같은 역할
    - 데이터를 고유하게 식별
- 파이썬에서는 해시 함수를 사용하여 데이터를 해시 값으로 변환하며, 이 해시 값은 정수로 표현됨
- 임의의 길이의 데이터를 입력 받아 고정된 길이의 데이터(해시 값)를 출력하는 함수
- 주로 해시 테이블 자료구조에 사용되며, 매우 빠른 데이터 검색을 위한 컴퓨터 소프트웨어에서 유용하게 사용

## set의 요소 & dictionary의 키와 해시테이블 관계

- 파이썬에서 세트의 요소와 딕셔너리 키는 해시 테이블을 이용하여 중복되지 않는 고유한 값을 저장함
- 세트 내의 각 요소는 해시 함수를 통해 해시 값으로 변환되고, 이 해시 값을 기반으로 해시 테이블에 저장됨
- 마찬가지로 딕셔너리의 키는 고유해야 하므로, 키를 해시 함수를 통해 해시 값으로 반환하여 해시 테이블에 저장

## 파이썬에서의 해시 함수

- 파이썬에서 해시 함수의 동작 방식은 객체의 타입에 따라 달라짐
- 자료 구조 상 순서가 존재 하려면 해시함수가 없어야함
- pop()은 해시 테이블 상의 순서로 진행 됨

## 파이썬에서의 해시 함수 - 정수

- 같은 정수는 항상 같은 해시 값을 가짐
- 해시 테이블에 정수를 저장할 때 효율적인 방법
- 예를 들어, hash(1)과 hash(2)는 항상 서로 다른 해시 값을 갖지만, hash(1)은 항상 동일한 해시 값을 갖게 됨

```python
# 정수
my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set)
# 정수는 왜 빠지는 순서가 똑같지?
'''
1
2
3
100
4
39
9
10
52
87
set()
'''
```

## 파이썬에서의 해시 함수 - 문자열

- 문자열은 가변적인 길이를 갖고 있고, 문자열에 포함된 각 문자들의 유니코드 등을 기반으로 해시 값을 계산
- 이로 인해 문자열의 해시 값은 실행 시마다 다르게 계산됨

```python
# 문자열
my_str_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())

# 실행할 때마다 바뀜
'''
d
g
b
c
a
1
1
'''
```

## set의 pop 메서드의 결과와 해시 테이블의 관계

- set의 pop()에서 임의의 요소를 제거하고 반환
- 실행할 때 마다 다른 요소를 얻는다는 의미에서 ‘무작위’가 아니라 “임의”라는 의미에서 “무작위”
    
    ⇒ 해시 테이블에 나타나는 순서대로 반환하는 것
    

## hashable

- hash() 함수의 인자로 전달해서 결과를 반환 받을 수 있는 객체
- 대부분의 불변형 데이터 타입은 hashable
- 단, tuple의 경우 불변현이지만

## hashable과 불변성 간의 관계

- 해시 테이블의 키는 불변해야 함
    - 객체가 생성된 후에 그 값을 변경할 수 없어야 함
- 불변 객체는 해시 값이 변하지 않으므로 동일한 값에 대해 일관된 해시 값을 유지할 수 있음
- 단, ‘hash 가능하다 ≠ 불변하다’

## 가변형 객체가 hashable 하지 않은 이유

- 값이 변경될 수  있기 때문에 동일한 객체에 대한 해시 값이 변경될 가능성이 있음

## hashable 객체가 필요한 이유

1. 해시 테이블 기반 자료 구조 사용
    1. set와 dict의 key
    2. 중복 값 방지
    3. 빠른 검색과 조회
2. 불변성을 통한 일관된 해시 값
3. 안정성과 예측 가능성 유지

# 파이썬 문법 규격

## BNF

프로그래밍 언어의 문법을 표현하기 위한 방법

## EBNF

BNF를 확장한 표기법

### 메타기호 [] 사용 예시

pop(key[,default])