import numpy as np

# numpy
# 현재의 배열의 차원을 변경하여 행렬을 반환하거나 하는 경우에 많이 이용
# Python 에서 과학 연산을 위한 가장 기본적인 패키지 중 하나
# Numeric Python 의 약자

# 배열의 슬라이싱
# 다차원 배열의 원소 중 복수 개를 접근하려면 일반적인 파이썬 슬라이싱과 comma 를 함께 사용

# 1) numpy reshape 예제
arr3 = np.arange(20).reshape(5,4) # 5행 4열의 다차원 배열로 반환
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]]
print(arr3)
print(arr3[0, :]) # [0 1 2 3]
print(arr3[1:3, 0:2]) 
# [[4 5]
#  [8 9]]
print(arr3[0:2, : 2])
# [[0 1]
#  [4 5]]
print(arr3[[2,1,0],:])
# [[ 8  9 10 11]
#  [ 4  5  6  7]
#  [ 0  1  2  3]]

a = [1,2,3,4,5,6,7,8]
print(a) # [1, 2, 3, 4, 5, 6, 7, 8]
b = np.reshape(a,(2,4)) # 2행 4열의 배열로 반환
c= np.reshape(a,(4,2)) # 4행 2열의 배열로 반환
print(b)
#[[1 2 3 4]
#  [5 6 7 8]]
print('\n')
print(c)
#[[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# numpy 와 ndarray 에 대한 설명

# numpy > 수치 해석용 python 패키지
# 다차원의 행렬 자료구조인 ndarray 를 지원하여 벡터와 행렬을 사용하는 선형대수 계산에 주로 사용
# numpy의 행렬 연산은 c로 구현된 내부 반복문을 사용하기 때문에 python 반복문에 비해 속도가 빠르다
# 행렬 인덱싱을 사용한 질의 기능을 이용하여 짧고 간단한 코드로 복잡한 수식을 계산할 수 있다.

# ndarray 클래스
# numpy 의 핵심은 ndarray 클래스
# ndarray 클래스는 다차원 행렬 자료 구조를 지원

# 2) ndarray의 type
a = np.array([0,1,2,3,4,5,6,7,8,9])
print(type(a)) # <class 'numpy.ndarray'>

# ndarray 와 list 객체의 차이

# python 리스트
# 1) 여러가지 타입의 원소
# 2) linked List 구현
# 3) 메모리 용량이 크고 속도가 느림
# 4) 벡터화 연산 불가

# NumPy ndarray
# 1) 동일 타입의 원소
# 2) contiguous memory layout
# 3) 메모리 최적화, 계산 속도 향상
# 4) 벡터화 연산 가능

# 원소 모두를 제곱하기 위해서는 반복문을 이용해 원소를 각각 제곱할 필요 없이 객체 자체를 제곱하는 
# 것만으로도 원하는 결과를 얻을 수 있다.
a = np.array([0,1,2,3,4,5,6,7,8,9])
a2 = a**2
print(a2) # array([ 0  1  4  9 16 25 36 49 64 81], dtype=int32)

# 행렬의 차원 및 크기는 ndim 속성과 shape 속성으로 알 수 있다.
print(a)
# [0 1 2 3 4 5 6 7 8 9]
print(b)
#[[1 2 3 4]
#  [5 6 7 8]]
print(c)
#[[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

print(a.ndim) # 1
print(a.shape) # (10,)
print(b.ndim) # 2
print(b.shape) # (2,4)
print(c.ndim) # 2
print(c.shape)  # (4,2)

# a, b, C 배열 코드 추가 안 하여 오류 뜸, 일단 주석처리
# print(c[0,0,:])
# print(c[0,0,1:])


