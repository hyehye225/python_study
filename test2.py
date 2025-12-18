# count, index, sort, range & arange

# 1) count > 원소의 갯수를 반환
a = [10,20,30,40,50,10,20,30,40]
print(a.count(10))

# 2) s.index > 원소의 위치를 반환
print(a.index(10))

# 3) s.append : 원소를 리스트의 뒷쪽에 삽입
a= [10, 20]
print(list(a))
a.append(30)
print(list(a))

# 4) s.sort : 원소를 정렬 
# 매우 중요
a = [9,5,3,2,6,7,1,8,4,6]
a.sort()
print(list(a))

# 5) sort와 sorted 의 차이
# sort, sorted > 기본적으로 오름차순으로 정렬
# sort > 리스트형의 메소드, 리스트 원본 값을 직접 수정
# sorted > 내장 함수, 리스트 원본 값은 그대로이고 정렬 값을 반환
# 내림차 순으로 정렬하려면 reverse 옵션에 True 값을 설정

list2 = ['a','y','d','x','k','f']
list2.sort(reverse = True)
print(list2)


# numpy 학습
import numpy as np

# numpy의 array 는 동일한 타입으로만 이루어진다. 
# > numpy의 연산을 매우 빠르게 진행하기 위한 것
# 배열은 NumPy 라이브러리의 중앙 데이터 구조


# 6) numpy 의 arange & python의 range 함수의 차이
range_array = np.arange(10)
print(range_array)

a = np.array([1,2,3,4,5])
print(a)

# numpy.arange() > 지정된 범위 내에서 일정한 간격으로 숫자를 생성하는 함수
# python의 range 함수와 유사하지만, 실수 단위의 간격도 사용할 수 있다.

# ex > 간격 설정
arr = np.arange(1,10,2)
print(arr)

arr = np.arange(0,1,0.1)
print(arr)


